# Patient Intake/Output (I/O) Recorder

This project is a simple tool for recording and tracking essential health
parameters of patients. It provides a user-friendly interface for healthcare
professionals to log various health metrics, including food intake, water
consumption, urine volume, defecation frequency, and weight, along with
corresponding timestamps for each entry. This information can be valuable for
healthcare professionals to monitor and analyze the health status of patients
over time.

Uses [Poetry](https://github.com/python-poetry/poetry) for dependency management
and includes, ruff and pre-commit for linting and formatting.

## Importance for Kidney Disease Management

In particular, it plays a crucial role in managing conditions such as kidney
disease, where strict control over water intake is essential for maintaining
health and preventing complications.

## Getting Started

1. Set your configuration:
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
     `patient/` directory. Update the file by replacing `{your_api_url_here}`
     with your actual API URL in the following format:

     **Example `patient/config.json` content:**
     ```json
     {
       "apiUrl": "{your_api_url_here}"
     }
     ```

   - **Frontend (Monitor)**: Navigate to the `config.json` file located in the
     `monitor/` directory. Update the file by replacing `{your_api_url_here}`
     and `{your_web_url_here}` with your actual API URL and web URL in the
     following format:

     **Example `monitor/config.json` content:**
     ```json
     {
       "apiUrl": "{your_api_url_here}",
       "webUrl": "{your_web_url_here}"
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

## Want to Contribute?

Refer to [CONTRIBUTING.md](./CONTRIBUTING.md)

## LICENSE

See [LICENSE](./LICENSE) for more information.
