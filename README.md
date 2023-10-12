# Phonetic Transcription API

This is a simple Flask-based API for generating phonetic transcriptions using transliteration. The API accepts text input and provides a phonetic transcription in the Ukrainian language.

## Getting Started

These instructions will help you set up and run the project locally for development and testing purposes.

### Prerequisites

- Python 3.x
- Flask
- Flask-CORS
- Transliterate

### Installing

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/grey-box/project_codex_features
   ```

2. Change into the project directory.

    ```bash
    cd project_codex_features
    ```

3. Create and activate a virtual environment.

    ```bash
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate  # For Windows
    ```

4. Install the required dependencies.

    ```bash
    pip install -r requirements.txt
    ```

### Running the API

To start the API, run the following command:

    ```bash
    python app.py
    ```
The API will be available at http://localhost:5000.


### Usage 

You can access the API by sending a GET request to the following endpoint:

http://localhost:5000/api/phonetic-transcription/<text>

Replace <text> with the text you want to transcribe. The API will respond with a JSON object containing the phonetic transcription.


## Acknowledgments

## License