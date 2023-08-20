import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
from dotenv import load_dotenv
import whisper
from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
load_dotenv()

# Configure Cloudinary
cloudinary.config(
    cloud_name=os.getenv("cloud_name"),
    api_key=os.getenv("api_key"),
    api_secret=os.getenv("api_secret")

)
# Load OpenAI Whisper
model = whisper.load_model("base")

@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/transcribe", methods=["POST"])
@cross_origin()
def transcribe_audio():
    # Get the audio file URL from the request
    audio_url = request.json["audio_url"]
    print(audio_url)

    # Extract audio clip name
    audio_clip_name = audio_url.split('/')[-1]

    # Use OpenAI Whisper to transcribe the audio file
    transcribe = model.transcribe(audio_url)

    # Get current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    segments = transcribe['segments']
    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

        # Generate unique SRT filename
        srtFilename = os.path.join(
            "SrtFiles", f"{audio_clip_name}_{timestamp}.srt")

        # Write segment to SRT file
        with open(srtFilename, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)

    # Upload the SRT file to Cloudinary
    uploaded_file = cloudinary.uploader.upload(
        srtFilename, resource_type="raw", folder="/audiogram/srt")
    srt_url = uploaded_file["secure_url"]

    print(srt_url)

    return srt_url


if __name__ == '__main__':
    app.run(debug=True, port=8000)
