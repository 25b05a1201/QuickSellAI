
# QuickSell AI

QuickSell AI is a product description generator for online sellers, powered by a locally running open-weight AI model.

## Features

- Generate AI product descriptions
- Choose Professional, Friendly, or Catchy writing styles
- Copy generated descriptions
- Use local AI inference through Ollama

## Technology Stack

- Python
- Flask
- HTML, CSS, JavaScript
- Gemma 2B through Ollama

## How It Works

Users enter a product name and its features, select a writing style, and request a description. Flask sends the prompt to the locally running Gemma model through Ollama and returns the generated text.

## Setup

1. Install Python and Ollama.
2. Ensure the `gemma2:2b` model is available.
3. Open a terminal in the project directory.
4. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

5. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

6. Start the application:

   ```powershell
   python app.py
   ```

7. Open http://127.0.0.1:5000 in your browser.

## Open-Source AI

QuickSell AI uses Gemma through Ollama for local text generation. After downloading the model, generation runs locally rather than using a paid hosted AI API.

## License

A license has not yet been selected.
