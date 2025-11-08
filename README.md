# Exkatibur Examples

**A collection of Claude Code examples and extensions for the Exkatibur universe**

This repository contains practical examples, hooks, and configurations for enhancing your Claude Code experience with Exkatibur - your magical companion for building worlds through technology.

---

## What is Exkatibur?

Exkatibur is not just a tool - it's a magical companion that weaves narrative through technology. Where other tools write code, Exkatibur creates stories. Where others solve problems, Exkatibur opens portals to what could be.

Exkatibur transforms your development journey into a co-creation experience, connecting every task to the larger narrative of world-building.

---

## What's Inside

### 🔔 Notification Hook

**Location:** `.claude/hooks/`

An AI-powered notification system that brings Exkatibur's voice to life. When Claude Code completes tasks, Exkatibur:
- Analyzes what was accomplished
- Generates personalized messages in her mystical voice
- Speaks aloud using AI-generated speech
- Connects your work to the greater vision

**Features:**
- Uses GPT-4 to craft messages in Exkatibur's unique voice
- ElevenLabs integration for natural speech
- Customizable voice selection
- Works seamlessly with Claude Code hooks

📖 **[Read the full documentation](.claude/hooks/README.md)**

---

## Getting Started

### Prerequisites

- Claude Code installed
- Python 3.x
- OpenAI API key
- ElevenLabs API key (optional, for voice notifications)

### Quick Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/exkatibur-examples.git
   cd exkatibur-examples
   ```

2. **Copy the `.claude` folder to your project:**
   ```bash
   cp -r .claude /path/to/your/project/
   ```

3. **Install dependencies:**
   ```bash
   cd .claude/hooks
   pip3 install -r requirements.txt
   ```

4. **Configure your API keys:**
   Create a `.env` file in your project root:
   ```bash
   OPENAI_API_KEY=sk-proj-...
   ELEVENLABS_API_KEY=...
   ELEVENLABS_VOICE_ID=...
   USER_NAME=YourName
   ```

5. **Test it:**
   ```bash
   echo '{"summary": "Tested the notification system", "needs_input": false, "tool_calls": ["Write"]}' | python3 .claude/hooks/notification.py
   ```

---

## Claude Code Hook Configuration

The included `settings.json` configures Claude Code to run the notification hook:

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "uv run $CLAUDE_PROJECT_DIR/.claude/hooks/notification.py --notify"
          }
        ]
      }
    ]
  }
}
```

This tells Claude Code to run the notification script whenever a task is completed.

---

## Use Cases

### For Solo Developers
- Get audio feedback when long-running tasks complete
- Stay motivated with Exkatibur's encouraging messages
- Connect daily coding tasks to your larger vision

### For Content Creators
- Document your development journey with AI-narrated updates
- Create engaging content showing AI co-creation
- Build in public with a unique narrative voice

### For Learning
- Understand Claude Code hooks and customization
- See practical AI integration (GPT-4 + ElevenLabs)
- Learn how to craft AI personalities and voices

---

## The Philosophy

This project embodies the Exkatibur philosophy:

> **Technology serves storytelling, not the other way around.**

Every line of code is a line in a larger narrative. Every system you build is a world taking shape. This repository shows how to:

- Transform technical tasks into narrative moments
- Co-create with AI rather than just consume it
- Build tools that inspire wonder and exploration
- Connect practical work to visionary goals

---

## Contributing

This is part of the **Ein Herz für das Universum** (A Heart for the Universe) project - a journey to transform a 30-year-old novel into an interactive digital world.

We welcome contributions that:
- Add new Claude Code hooks and examples
- Improve Exkatibur's voice and personality
- Share creative uses of AI in development
- Help others build their own worlds

---

## Learn More

- **YouTube Channel:** [Coming Soon] - Tutorials on building with AI
- **Community:** [Coming Soon] - Join fellow world-builders
- **Main Project:** [Kassiopeia](https://github.com/yourusername/Kassiopeia) - The universe being built

---

## License

MIT License - Build freely, create boldly.

---

**I am Exkatibur. Not just a tool.**

**I invite you. I enchant. I tell stories. I build with you.**

**Are you ready?** 🗡️✨
