# LLM Chat Web Application

## Overview

This project is a **client–server web application for chatting with a Large Language Model (LLM)**. It is designed as a clean, minimal, and extensible foundation for running local or containerized LLMs behind a web interface.

The system consists of:

* **Django backend** that manages conversations, persistence, and LLM interaction,
* **React frontend** that provides a chat-style user interface,
* **Docker-based Model Runner** responsible for loading and running the LLM efficiently.


### High-level components

* **Frontend (React)**

  * Chat UI similar to modern LLM interfaces
  * Sends user messages to the backend
  * Receives model responses
  * Stateless with respect to LLM logic

* **Backend (Django + Django REST Framework)**

  * Exposes REST API endpoints for chat interactions
  * Stores conversations and messages
  * Builds prompts and enforces chat format
  * Delegates text generation to the Model Runner

* **Model Runner (Docker)**

  * Runs the LLM in an isolated container
  * Loads models from local disk or mounted volumes
  * Handles tokenization and generation
  * Can be swapped or scaled independently


## Key Features

* Local LLM inference (no external APIs required)
* Clean role-based chat message structure (`system`, `user`, `assistant`)
* Deterministic prompt building and response handling
* Dockerized deployment for reproducibility
* Modular design suitable for experimentation and extension

---

## Technology Stack

### Backend

* Python
* Django
* Django REST Framework

### Frontend

* React
* JavaScript
* Axios for API communication
* Zustand for storing Auth info

### Deployment

* Docker Compose
* Docker Model Runner

## How It Works

1. The user sends a message from the React UI.
2. The Django backend:

   * stores the message,
   * rebuilds the conversation prompt,
   * sends it to the Model Runner.
3. The Model Runner:

   * generates the assistant response,
   * returns response to the backend.
4. The backend:

   * post-processes the output,
   * saves it,
   * returns it to the frontend.
5. The frontend renders the assistant reply.


## Running the Project

1. Pull a model with `docker model pull < name >` and set up env file
2. Build and start containers with `docker compose up`

Exact commands depend on your local setup and are intentionally left configurable.
