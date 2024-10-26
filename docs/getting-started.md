# Installation

1. Set your token: First, navigate to the `config.json` file located in the
   `backend` directory. Update the file by replacing `{your_token_here}` with
   your actual token in the following format:

    ```json
    {
      "token": "{your_token_here}"
    }
    ```

2. Run your server: Open your terminal and execute the following commands:

    ```bash
    poetry install
    python -m uvicorn main:app --reload
    ```

   This will install the necessary dependencies using Poetry and start your
   server using Uvicorn with automatic reloading enabled. With these steps
   completed, your server should be up and running, ready to handle requests.
