# Automatic Form Submission Script

This script automates the submission of forms on a specified platform using Python and the `requests` library.

## Setup

1. **Installation:** Ensure Python is installed on your system. If not, download it from [python.org](https://www.python.org/).

2. **Dependencies:** Install required dependencies using pip:
    ```
    pip install requests
    ```

3. **Credentials:** Provide your login credentials in the `creds` list at the script's start.

## Usage

Run the script to automate form submissions. It will cycle through provided credentials, sleeping for random intervals between submissions.

## Features

- **Login:** Authenticates users with provided credentials.
- **Information Retrieval:** Retrieves necessary information for form submission.
- **Form Building:** Constructs form payload using a `formBuilder` object.
- **Randomization:** Generates random values for form fields to simulate human input.
- **Submission:** Sends form data to the platform's API for processing.
- **Error Handling:** Detects and handles errors during submission.

## Example

```python
python form_submission_script.py
```

## Usage with Task Scheduler or Cron Job

For optimal automation, integrate this script with a task scheduler (Windows) or cron job (Unix-like systems). These tools allow scheduling script execution at specified intervals without manual intervention.

### Windows Task Scheduler

1. **Open Task Scheduler:** Search for "Task Scheduler" in the Start menu and open it.

2. **Create Task:** Click "Create Task" in the right-hand sidebar.

3. **General Settings:** Provide a name and description for the task. Ensure "Run whether user is logged on or not" is selected.

4. **Triggers:** Add a trigger to specify when the task should run (e.g., daily, weekly, etc.).

5. **Actions:** Add an action to start a program. Specify the Python executable (`python.exe`) path and the script's file path.

6. **Conditions and Settings:** Customize additional settings as needed, such as power management options.

7. **Save and Test:** Save the task and test it to ensure it runs as expected.

### Unix-like Systems (Linux, macOS)

1. **Edit Crontab:** Open the crontab editor by running `crontab -e` in the terminal.

2. **Schedule Task:** Add an entry to the crontab file specifying the schedule and the command to run the script. For example:
   ```
   0 15 * * * /usr/bin/python3 /path/to/form_submission_script.py
   ```
   This example schedules the script to run every day at 8:00 AM.

3. **Save and Exit:** Save the changes and exit the crontab editor.

4. **Verify:** Use `crontab -l` to verify that the entry was added correctly.

Automate script execution according to your desired schedule, saving time and ensuring timely form submissions.
