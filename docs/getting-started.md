# Getting Started

This guide will walk you through setting up the Patient Intake/Output Recorder
(PIOR) project. Follow the steps below to install dependencies, configure
settings, and start the server.

## Installation

### Install Dependencies

Patient Intake Output Recorder can be set up with either Poetry (recommended) or
pip. Open a terminal in the project directory and install the dependencies:

=== "Using Poetry"

    ```sh
    poetry install
    ```

=== "Using pip"

    ```sh
    pip install -r requirements.txt
    ```

!!! Note

    Poetry is recommended as it simplifies version management and ensures
    reproducible builds.

## Configuration

### Backend

1. In the `backend` directory, create a new `config.json` file.
2. Replace `{your_token_here}` and `{your_api_url_here}` with your actual token
   and API URL.

**Example content:**

```json title="backend/config.json"
{
  "token": "{your_token_here}",
  "api_url": "{your_api_url_here}"
}
```

### Frontend (Patient)

1. In the `patient` directory, create a new `config.json` file.
2. Replace `{your_api_url_here}` with your actual API URL.

**Example content:**

```json title="patient/config.json"
{
  "apiUrl": "{your_api_url_here}"
}
```

### Frontend (Monitor)

1. In the `monitor` directory, create a new `config.json` file.
2. Replace `{your_api_url_here}` and `{your_web_url_here}` with your actual API
   URL and web URL.

**Example content:**

```json title="monitor/config.json"
{
  "apiUrl": "{your_api_url_here}",
  "webUrl": "{your_web_url_here}"
}
```

## Running the server

Once installed and configured, you can start the server with Uvicorn.

=== "Using Poetry"

    ```sh
    poetry run uvicorn main:app --reload
    ```

=== "Using Python"

    ```sh
    python -m uvicorn main:app --reload
    ```

This command launches the server with hot-reloading enabled, which automatically
restarts the server upon code changes. With these steps completed, your server
should be up and running, ready to handle requests.
