FROM python:3.12-slim

WORKDIR /workspace

# Install system dependencies for PaddleOCR and OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt /workspace/.devcontainer/
RUN pip install \
    --upgrade pip \
    --no-cache-dir \
    -r /workspace/.devcontainer/requirements.txt

# Run any command to initialize the container
CMD ["bash"]
