# Audiogram Python Transcription API

## Powering subtitles for [Audiogram](https://github.com/SAYUK09/Audiogram)
A Python Transcription API that leverages the power of OPENAI Whisper to generate subtitles from audio files. 
The API generates subtitles for audio clips.

## Features

- **Transcription:** Utilizes OPENAI Whisper for accurate and efficient audio-to-text transcription.
- **Subtitle Generation:** Automatically generates subtitles from the transcribed text.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- OPENAI API key for Whisper

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SAYUK09/Transcription-Api.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

Run the API server:

```bash
python main.py
```
The API should be up and running now.

### CLI Usage

*Alternately if you want to use it via CLI:*

Make a POST request to the transcription endpoint:

 ```bash
 curl -X POST -H "Content-Type: application/json" -d '{"audio_url": "https://example.com/audio.mp3"}' http://localhost:5000/transcribe
  ```

Replace the `audio_url` with the URL of the audio file you want to transcribe.

The API will respond with a link to SRT File.

### Usefull Links
- [Audiogram](https://github.com/SAYUK09/Audiogram)
- [Audiogram Nodejs BE](https://github.com/SAYUK09/Audiogram-Backend)



## Acknowledgments

- OPENAI for providing the powerful Whisper API.
