# ChatBox Using Gemini

A simple command-line chatbot powered by Google's Gemini API. This project allows you to interact with an AI assistant using natural language.

## Features

- Conversational AI using Gemini 2.5 Flash model
- Maintains chat history for context-aware responses
- Handles empty input and safety filtering
- Easy setup with environment variables

## Setup

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies**:
   ```sh
   pip install google-generativeai python-dotenv
   ```

3. **Set up your API key**:
   - Create a `.env` file in the `ChatBox Using Gemini` directory.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

Run the chatbot from the terminal:

```sh
python ChatBox.py
```

Type your message and press Enter to chat. Type `exit` to end the conversation.

## File Structure

- `ChatBox.py`: Main chatbot script
- `.env`: Stores your Google API key (do not share this file)
- `README.md`: Project documentation

