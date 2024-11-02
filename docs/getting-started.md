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

**Note**: Poetry is recommended as it simplifies version management and ensures
reproducible builds.

## Configuration

- **Backend**: Navigate to the `config.json` file located in the `backend`
  directory. Update the file by replacing `{your_token_here}` and
  `{your_api_url_here}` with your actual token and API URl in the following
  format:

  **Example `backend/config.json` content:**
  ```json
  {
    "token": "{your_token_here}",
    "api_url": "{your_api_url_here}"
  }
  ```

- **Frontend (Patient)**: Navigate to the `config.json` file located in the
  `patient/` directory. Update the file by replacing `{your_api_url_here}` with
  your actual API URL in the following format:

  **Example `patient/config.json` content:**
  ```json
  {
    "apiUrl": "{your_api_url_here}"
  }
  ```

- **Frontend (Monitor)**: Navigate to the `config.json` file located in the
  `monitor/` directory. Update the file by replacing `{your_api_url_here}` and
  `{your_web_url_here}` with your actual API URL and web URL in the following
  format:

  **Example `monitor/config.json` content:**
  ```json
  {
    "apiUrl": "{your_api_url_here}",
    "webUrl": "{your_web_url_here}"
  }
  ```

- Open `config.json` located in the `backend` directory and replace
  `{your_token_here}` with your actual token. The format should resemble:

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
