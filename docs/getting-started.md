# Getting Started

This guide will walk you through setting up the Patient Intake/Output Recorder (PIOR) project. Follow the steps below to install dependencies, configure settings, and start the server.

## Installation

### Install Dependencies

Patient Intake Output Recorder can be set up with either Poetry (recommended) or pip. Open a terminal in the project directory and install the dependencies:

=== "Using Poetry"

    ```sh
    poetry install
    ```

=== "Using pip"

    ```sh
    pip install -r requirements.txt
    ```

**Note**: Poetry is recommended as it simplifies version management and ensures reproducible builds.

## Configuration

### Set your token

- Open `config.json` located in the `backend` directory and replace `{your_token_here}` with your actual token. The format should resemble:

    ```json
    {
      "token": "{your_token_here}"
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

This command launches the server with hot-reloading enabled, which automatically restarts the server upon code changes. With these steps completed, your server should be up and running, ready to handle requests.
