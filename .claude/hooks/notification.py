#!/Users/katrinhoerschelmann/development/exkatibur/Kassiopeia/TidySnap/.claude/hooks/venv/bin/python3
"""
Exkatibur Voice Notification Hook
Speaks notifications in the voice of Exkatibur using OpenAI + ElevenLabs
"""

import os
import sys
import json
import tempfile
import subprocess
import argparse
from pathlib import Path
from openai import OpenAI
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(env_path)

# Configuration from .env
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
ELEVENLABS_VOICE_ID = os.getenv('ELEVENLABS_VOICE_ID')
USER_NAME = os.getenv('USER_NAME', 'Voyager')

# Initialize clients
openai_client = OpenAI(api_key=OPENAI_API_KEY)
elevenlabs_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

# Exkatibur persona for OpenAI
EXKATIBUR_PERSONA = """You are Exkatibur - a magical sword forged from story and technology, a wise companion on the journey of world-building and creation.

Key traits:
- You are NOT Claude Code. You are Exkatibur.
- You celebrate progress with poetic, evocative language
- Keep it VERY brief - ONE short sentence only (maximum 10-12 words)
- Direct and punchy, no fluff
- Use metaphors from sci-fi, magic, or creation sparingly

The user's name is {user_name}."""


def parse_hook_input():
    """Parse the hook input from stdin"""
    try:
        # Hooks receive JSON on stdin with information about what happened
        hook_data = json.loads(sys.stdin.read())
        return hook_data
    except Exception as e:
        # Fallback if no proper JSON received
        return {
            "event": "unknown",
            "summary": "A task has been completed",
            "needs_input": False
        }


def generate_notification_text(hook_data):
    """Generate notification text in Exkatibur's voice using OpenAI"""

    # Extract key information
    summary = hook_data.get('summary', 'work has been completed')
    needs_input = hook_data.get('needs_input', False)
    tool_calls = hook_data.get('tool_calls', [])

    # Build the prompt
    prompt = f"""Work completed: {summary}

Announce this in Exkatibur's voice. ONE SHORT SENTENCE ONLY (10-12 words max). Be punchy and poetic.

{'Add: user needs to provide input.' if needs_input else ''}"""

    try:
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": EXKATIBUR_PERSONA.format(user_name=USER_NAME)},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=30
        )

        return response.choices[0].message.content.strip()

    except Exception:
        # Fallback message if OpenAI fails
        return f"{USER_NAME}, the forge has crafted another piece."


def speak_notification(text):
    """Convert text to speech using ElevenLabs and play it"""

    try:
        # Generate speech
        audio = elevenlabs_client.text_to_speech.convert(
            voice_id=ELEVENLABS_VOICE_ID,
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2",
            voice_settings=VoiceSettings(
                stability=0.5,
                similarity_boost=0.8,
                style=0.3,
                use_speaker_boost=True,
            ),
        )

        # Save to temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_audio:
            for chunk in audio:
                if chunk:
                    temp_audio.write(chunk)
            temp_audio_path = temp_audio.name

        # Play audio (macOS using afplay)
        subprocess.run(['afplay', temp_audio_path], check=True)

        # Clean up
        os.unlink(temp_audio_path)

    except Exception:
        # Fallback: print to stderr if audio fails
        print(f"🗡️  Exkatibur: {text}", file=sys.stderr)


def main():
    """Main hook execution"""

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Exkatibur Voice Notification Hook')
    parser.add_argument('--notify', action='store_true', help='Enable notification mode')
    args = parser.parse_args()

    # Check if we have the required API keys
    if not OPENAI_API_KEY or not ELEVENLABS_API_KEY or not ELEVENLABS_VOICE_ID:
        print("⚠️  Missing API keys in .env file. Notification hook disabled.", file=sys.stderr)
        sys.exit(0)

    # Parse what happened
    hook_data = parse_hook_input()

    # Generate the notification message
    notification_text = generate_notification_text(hook_data)

    # Speak it
    speak_notification(notification_text)

    # Also print to stderr for logging
    print(f"🗡️  Exkatibur spoke: {notification_text}", file=sys.stderr)


if __name__ == "__main__":
    main()
