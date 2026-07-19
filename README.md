# Multi-Provider LLM Chat CLI

A command-line chat application that connects to multiple LLM providers through a single, consistent interface. Pick a provider, chat across multiple turns, switch providers mid-conversation, and resume exactly where you left off — even after closing the program.

## Features

- **Multi-provider support** — chat with Microsoft Phi-4 (via GitHub Models / Azure AI Inference) or an open-weight model via Groq, from the same CLI
- **Persistent conversation history** — every message is saved to a local JSON file and reloaded automatically the next time you run the program
- **Provider-agnostic design** — switch providers mid-conversation without losing context
- **Fail-fast credential checks** — missing API keys raise a clear, custom error instead of a confusing crash deep in a third-party library

## How it works

```
Press C to continue and E to exit: c
Available Models are
 1. microsoft/Phi-4
 2. openai/gpt-oss-120b
What model would you like to use
Enter 1 or 2: 1
Enter your message: hello
Hello! How can I assist you today?
```

## Setup

1. Clone this repo and install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the project root (see `.env.example` for the expected format):
   ```
   AZURE_API_KEY=your_github_models_token
   GROQ_API_KEY=your_groq_api_key
   ```
   - Get a free GitHub Models token from your GitHub account settings (Personal access tokens, with Models access).
   - Get a free Groq API key at [console.groq.com](https://console.groq.com).

3. Run it:
   ```
   python main.py
   ```
