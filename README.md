# ai-text-completion-project
# AI Text Completion App

This is a simple command-line application that leverages the Cohere API to generate AI-powered text completions based on your prompts. The app allows you to specify the creativity (temperature) of the responses, giving you control over how imaginative or focused the results are.

## Features

- **Interactive CLI**: Enter prompts and receive AI-generated completions in real-time.
- **Adjustable Creativity**: Choose the "creativity" (temperature) of the AI's responses.
- **Error Handling**: Gracefully handles invalid input and API errors.
- **Environment Variables**: Uses a `.env` file for secure API key management.

## Requirements

- Python 3.7+
- [Cohere Python SDK](https://docs.cohere.com/docs/quickstart)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kim-one/ai-text-completion-project.git
   cd ai-text-completion-project
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your Cohere API key:**
   - Create a `.env` file in the project root:
     ```
     API_KEY=your-cohere-api-key-here
     ```
   - You can obtain an API key from [Cohere](https://dashboard.cohere.com/api-keys).

## Usage

Run the application with:

```bash
python text_completion_app.py
```

You will see a welcome message and be prompted to set the creativity for your text generation, or proceed with the default setting.

- **To set creativity**: Type `Y` and enter a float between 0 and 1 (e.g., `0.3` for focused, `0.9` for creative).
- **To exit**: Type `exit` when prompted.

Example interaction:

```
##################################################
    Welcome to the text completion app
##################################################
Type 'exit' to exit the program

Would you like to set the creativity of the text?
Y/N: Y
To set creativity, enter a float between 0 and 1: 0.5
Enter a prompt: Write a story about a robot
AI Response:  Once upon a time...
```

## Notes

- The app uses Cohere's `command-a-03-2025` model for chat completions.
- If you type `exit` at the prompt, the app will close.
- Make sure your API key is valid and active.
