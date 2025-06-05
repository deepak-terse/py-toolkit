# RAG (Retrieval-Augmented Generation) using Langchain

This project implements a Retrieval-Augmented Generation (RAG) system using Langchain, a powerful framework for building LLM applications. RAG enhances language models by combining retrieval-based and generation-based approaches, allowing for more accurate and contextually relevant responses.

## Overview

RAG works by:
1. Retrieving relevant documents from a knowledge base
2. Augmenting the input prompt with the retrieved context
3. Generating responses using a language model

## Features

- PDF document ingestion and processing
- Vector storage using ChromaDB for efficient retrieval
- Context-aware response generation using Ollama
- Interactive web interface using Gradio
- Integration with Langchain's powerful tools and utilities

## Technologies Used

- Langchain: RAG framework
- PyPDF: Document Loader
- ChromaDB: Vector Storage
- Gradio: UI Library
- Ollama: Local LLM Integration

## Prerequisites

- Python 3.12 or higher
- Ollama server: Download from https://ollama.com/

## Setup

1. Clone this repository
2. Install dependencies using pipenv:
   ```bash
   pipenv install
   pipenv install --dev  # for development dependencies
   ```
3. Pull the required Ollama model 'llama2' or any other model of your choice:
   ```bash
   ollama pull llama2
   ```
4. Start the Ollama server:
   ```bash
   ollama serve # alternatively you can simply open the Ollama app
   ```

## Usage

1. Place your PDF documents in the `data/` directory
2. Activate the virtual environment:
   ```bash
   pipenv shell
   ```
3. Run the application:
   ```bash
   python src/app.py
   ```
4. Open your browser and navigate to `http://127.0.0.1:7860`
5. Click "Populate Database" to process your documents
6. Start asking questions about your documents!

## Project Structure

```
rag/
├── data/           # Directory for PDF documents
├── src/            # Source code
│   ├── scripts/    # Core functionality scripts
│   └── utils/      # Utility functions
├── chroma/         # Vector database storage
├── Pipfile         # Python dependencies
└── README.md       # This file
```