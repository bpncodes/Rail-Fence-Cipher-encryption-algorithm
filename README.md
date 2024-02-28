
# INCS 741 Rail Fence Cipher Tool

This document provides instructions on how to set up and use the INCS 741 Rail Fence Cipher tool using Docker.

Authors: Bipin Karki, April Zhou

Date: 2024/2/26

## Prerequisites

Before you begin, make sure Docker is installed on your machine. If it is not installed, follow the installation instructions for your specific operating system on the [Docker official website](https://www.docker.com/get-started).

## Getting Started

Follow these steps to get the Rail Fence Cipher tool running:

### 1. Download the Docker Image

Pull the Docker image from the Docker Hub:

```bash
docker pull kaptainbpn/bpns_741_rail_fence:v1
```

### 2. Run the Docker Container

Run the following command to start a container from the image:

a. Click "run" in Docker Desktop, put **8080** in "**Host port"** field, or

b. Use this command to map port 8080 of the container to port 8080 on your host machine.

```bash
docker run -p 8080:8080 kaptainbpn/bpns_741_rail_fence:v1
```

### 3. Access the Tool

Open your web browser and navigate to:

```
http://localhost:8080/
```

### 4. Use the Tool

Once the web interface is loaded, you can start using the tool:

1. Choose whether you want to **Encrypt** or **Decrypt**.
2. Input the text and the key in the respective fields.
3. Click **Submit** to process the input.

### 5. View the Result

The result of the encryption or decryption will be displayed on the screen.

## Support

For any issues or questions, please refer to the documentation or contact support.
