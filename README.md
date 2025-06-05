# Python Toolkit

A curated collection of Python scripts and small-scale projects for automation, rapid prototyping, experimentation, and daily utility.

---

## 📁 Project Structure

```
.
├── .venv/ or .venv-env/    # Virtual environment (git-ignored)
├── scripts/                # Independent automation or utility scripts
├── projects/               # Larger prototypes or modular apps
├── requirements.txt        # Common dependencies (for quick setup)
└── README.md               # This file
```

## 📚 Scripts

| Script                     | Description                                               |
|---------------------------|-----------------------------------------------------------|
| `tts.py`                  | Synthesizes text to speech using the TTS library with a pre-trained VCTK model. It is designed to produce human-like voice synthesis and is part of a proof of concept for an AI voice assistant project. |

_Note: See individual script docstrings for more._

---

## 🧪 Projects

| Project                   | Description                                               |
|--------------------------|-----------------------------------------------------------|
| `rag/`                   | A Retrieval-Augmented Generation (RAG) system using Langchain. Combines document retrieval with LLM generation for context-aware responses. Features include document processing, vector storage, and integration with Langchain's utilities. |

_Note: Each project has its own README. Navigate to the project folder for more._

---

## 📦 Dependency Management

- For small scripts, shared dependencies live in `requirements.txt`.
- For large projects, consider using `Pipfile`, `pyproject.toml`, or project-level `venv`.

---
