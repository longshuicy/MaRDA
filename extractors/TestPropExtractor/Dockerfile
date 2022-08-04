# Base image is an Ubuntu based
FROM python:3

# Creating workdir
WORKDIR /home/clowder

# # RUN + any shell command
# RUN apt-get -qq -y update && apt-get install -qq -y libsndfile-dev sox
# # RUN apt-get install ffmpeg

# Install pyClowder and any other python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Adding necessary code to container under workdir
COPY TestPropExtractor.py extractor_info.json /home/clowder/

# Command to be run when container is run
# Can add heartbeat to change the refresh rate
CMD python3 TestPropExtractor.py --heartbeat 30

ENV MAIN_SCRIPT="TestPropExtractor.py"