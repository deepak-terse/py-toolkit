# Rasa Dialogue System

This project implements a conversational AI system using Rasa, an open-source framework for building contextual AI assistants and chatbots. The system is designed to handle various user interactions with a JARVIS-like personality, providing a sophisticated and engaging conversational experience.

## Overview

The dialogue system works by:
1. Processing user input through Natural Language Understanding (NLU)
2. Managing conversation flow using dialogue management
3. Executing custom actions when needed
4. Generating contextual responses

## Features

- Natural language understanding for intent classification
- Contextual dialogue management
- Custom action server for dynamic responses
- Multiple response variations for natural conversation
- Support for various functionalities:
  - Time and date queries
  - Weather information
  - Note creation
  - Reminder setting
  - Basic calculations
  - Information search
  - Jokes and general conversation

## Technologies Used

- Rasa: Open-source conversational AI framework

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Setup

1. Clone this repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv_rasa
   source .venv_rasa/bin/activate  # On Windows: .venv_rasa\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install rasa
   ```

## Usage

1. Train the model:
   ```bash
   rasa train
   ```

2. Start the Rasa server:
   ```bash
   rasa run
   ```

3. In a separate terminal, start the action server:
   ```bash
   rasa run actions
   ```

4. To test the bot, use:
   ```bash
   rasa shell
   ```

## Project Structure

```
rasa_dialogue_system/
├── actions/          # Custom action server code
├── data/            # Training data and NLU examples
├── models/          # Trained model files
├── tests/           # Test cases
├── config.yml       # Model configuration
├── credentials.yml  # API credentials
├── domain.yml      # Bot domain and responses
└── endpoints.yml   # Endpoint configurations
```

## Customization

The bot can be customized by:
1. Modifying `domain.yml` to add new intents and responses
2. Adding training examples in `data/` directory
3. Creating custom actions in the `actions/` directory
4. Adjusting the pipeline in `config.yml`

## Further Reading

- [Rasa Documentation](https://rasa.com/docs/rasa/) - Complete guide to Rasa framework
- [Rasa OS Documentation](https://legacy-docs-oss.rasa.com/docs/rasa/) - Core documentation for Rasa Open Source, covering NLU, dialogue management, and custom actions.
- [CALM Overview](https://rasa.com/docs/learn/concepts/calm/) - Guide to Rasa's Conversational AI Language Model for building natural dialogue systems. 