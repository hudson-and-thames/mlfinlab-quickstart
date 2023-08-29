# MLFinlab Quickstart 🚀 

This repository is a way to get up and running with `mlfinlab` quickly via Docker.

Executing `python start.py` executes a `docker compose up` command that pulls
down our `mlfinlab-base` image from DockerHub, injects your MLFinlab API key from
your local environment, validates the key, and then remotely install MLFinlab,
before finally launching a JupyterLab instance.

All of this takes place and executes inside of the Docker container, isolating
your system from any Python virtual environments or dependencies that you may
have installed.

## Requirements

- Docker and docker-compose are installed.
- Any version of Python

## Instructions

- Make sure your `MLFINLAB_API_KEY` environment variable is set.
- Clone this repository
- Execute `python start.py` from the within the project directory.
- You are now up and running with MLFinlab!
