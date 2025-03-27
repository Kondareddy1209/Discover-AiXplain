# Multi-Agent Deployment with aiXplain

This repository provides a step-by-step guide to setting up and running multiple AI agents using aiXplain's framework. It includes installation, setup, and execution details to help you deploy and manage agents efficiently.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Agents](#running-the-agents)
5. [Deployment](#deployment)
6. [Troubleshooting](#troubleshooting)

## Introduction
This project demonstrates how to set up and manage multiple AI agents using aiXplain. The agents can interact, process tasks, and execute AI-based workloads.

## Installation
Ensure you have Python installed (version 3.8 or higher). Then, install the required dependencies:
```bash
pip install aixplain-sdk
```

## Configuration
To authenticate with aiXplain, set up your API key as an environment variable:
```bash
export AIXPLAIN_API_KEY='your_api_key_here'
```
**Note:** Never expose your API key publicly.

## Running the Agents
Create and execute a Python script to initialize and run multiple agents:
```python
import aixplain as axp

# Initialize multiple agents
agent1 = axp.Agent("agent_id_1")
agent2 = axp.Agent("agent_id_2")

# Perform tasks
data = "Sample input data"
output1 = agent1.process(data)
output2 = agent2.process(data)

print("Agent 1 Output:", output1)
print("Agent 2 Output:", output2)
```
Run the script:
```bash
python run_agents.py
```

## Deployment
To deploy the agents on a cloud platform, use Docker or a cloud function:

1. **Create a Dockerfile:**
```Dockerfile
FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "run_agents.py"]
```

2. **Build and run the container:**
```bash
docker build -t multi-agent .
docker run -e AIXPLAIN_API_KEY=$AIXPLAIN_API_KEY multi-agent
```

## Troubleshooting
- Ensure your API key is correctly set.
- Check Python dependencies.
- Use `docker logs` to debug container issues.

This project is a foundation for scaling multi-agent AI solutions using aiXplain. Feel free to contribute!

