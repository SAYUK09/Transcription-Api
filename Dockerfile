# Use the official Ubuntu base image
FROM ubuntu:latest

# Set environment variables
ENV DEBIAN_FRONTEND noninteractive

# Install necessary dependencies
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app    
COPY . .

# Install OpenAI Whisper
# RUN pip3 install -U openai-whisper

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


# Copy the Python-Flask script to the working directory
COPY main.py .
RUN python3 -c "import whisper; whisper.load_model('base')"

# Expose the port on which the Flask app will run
EXPOSE 8000

# Run the Python-Flask script
CMD ["python3", "main.py"]
