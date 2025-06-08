# Python Toolkit

A curated collection of Python scripts and small-scale projects for automation, rapid prototyping, experimentation, and daily utility.

---

## 📁 Project Structure

```
.
├── .venv/ or .venv-env/    # Virtual environment (git-ignored)
├── jupyter-notebooks/      # Interactive notebooks for data analysis and demos
├── scripts/                # Independent automation or utility scripts
├── projects/               # Larger prototypes or modular apps
├── requirements.txt        # Common dependencies (for quick setup)
└── README.md               # This file
```

## 📚 Scripts

| Script                     | Description                                               |
|---------------------------|-----------------------------------------------------------|
| `intent_bot.py`           | A simulated AI assistant that mimics JARVIS's personality and speaking style. Uses pattern matching and intent detection to understand user queries and generate JARVIS-style responses. Features include time/date queries, jokes, and simulated note-taking capabilities. |
| `stt.py`                  | Implements continuous speech-to-text conversion using Google's speech recognition service. Features real-time voice input processing, ambient noise adjustment, and continuous listening mode until the user says "bye". |
| `tts.py`                  | Synthesizes text to speech using the TTS library with a pre-trained VCTK model. It is designed to produce human-like voice synthesis and is part of a proof of concept for an AI voice assistant project. |

_Note: See individual script docstrings for more._

---

## 🧪 Projects

| Project                   | Description                                               |
|--------------------------|-----------------------------------------------------------|
| `rag/`                   | A Retrieval-Augmented Generation (RAG) system using Langchain. Combines document retrieval with LLM generation for context-aware responses. Features include document processing, vector storage, and integration with Langchain's utilities. |
| `rasa_dialogue_system/`  | A conversational AI system using Rasa framework. Features JARVIS-like personality with capabilities for time/date queries, weather information, note creation, reminders, and natural conversation. Implements NLU, dialogue management, and custom actions. |

_Note: Each project has its own README. Navigate to the project folder for more._

---

## 📦 Dependency Management

- For scripts, shared dependencies live in `requirements.txt`.
- For projects, consider using `Pipfile`, `pyproject.toml`, or project-level `venv`.
- Some projects may require additional setup (e.g., Ollama for RAG project, Rasa for dialogue system).

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
