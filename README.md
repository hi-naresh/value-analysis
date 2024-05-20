# Daily Reflection Analysis API

## Overview

The Journal Entry Analysis API is a machine learning-based web service that analyzes daily journal entries and scores them based on 12 core values. These core values include Sincerity, Humility, Gratitude, Perseverance, Aspiration, Receptivity, Progress, Courage, Goodness, Generosity, Equanimity, and Peace. 

The API is built using FastAPI, transformers, and incorporates CORS and timeout middleware for enhanced performance and security.

## Features

- **Zero-Shot Classification**: Uses a pre-trained BART model for zero-shot classification of journal entries.
- **Asynchronous Processing**: Ensures efficient and responsive handling of requests.
- **Timeout Middleware**: Limits the request processing time to 2 minutes.
- **CORS Support**: Allows cross-origin requests from any origin.
- **Endpoints**: Includes endpoints for health checks, root message, and journal entry classification.

## Endpoints 

- **GET /health**: Returns the health status of the API.
- **GET /**: Returns a welcome message.
- **POST /analyze**: Analyzes the journal entry and returns the scores for the 12 core values.

## Endpoints Documentation

- **GET /health**: 
  - **Description**: Returns the health status of the API.
  - **Response**: 
    - **status**: The health status of the API.
  - **Example**: 
    ```json
    {
      "status": "API is healthy"
    }
    ```
- **GET /**:
- **Description**: Returns a welcome message.
- **Response**: 
  - **message**: A welcome message.
  - **Example**: 
    ```json
    {
      "message": "Welcome to the Journal Entry Analysis API!"
    }
    ```
- **POST /analyze**:
- **Description**: Analyzes the journal entry and returns the scores for the 12 core values.
- **Request**:
  - **journal_entry**: The journal entry to be analyzed.
  - **Example**: 
    ```json
    {
      "journal_entry": "Today was a great day. I am grateful for my family and friends."
    }
    ```
- **Response**:
- **scores**: The scores for the 12 core values.
- **Example**: 
  ```json
  {
    "scores": {
        "Sincerity": 25.55,
        "Humility": 0.0,
        "Gratitude": 23.01,
        "Perseverance": 22.87,
        "Aspiration": 34.69,
        "Receptivity": 30.25,
        "Progress": 0.0,
        "Courage": 26.07,
        "Goodness": 0.0,
        "Generosity": 0.0,
        "Equanimity": 21.79,
        "Peace": 0.0
    }
  }
  ```

