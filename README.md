# RK9 Checker

RK9 Checker is a Python script that automates the process of checking a registration page for a specific message and sends an email notification when the message changes. This script utilizes Selenium WebDriver to interact with the web page and SMTP for sending email notifications.
**NOTE: Be aware that this code might work for ANY OTHER SITE that requires some sort of log in (including SSO with Google) and requires to search for a message inside a //div//**

## Prerequisites

- Python 3.6 or newer.
- Selenium WebDriver.
- A Gmail account for sending email notifications.
- Google Chrome browser.

## Setup

1. **Install Python:**  
   If you don't have Python installed, download and install Python 3.6 or newer from [python.org](https://www.python.org/downloads/).

2. **Install PIP (Python's package installer):**  
   Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer.
   Open a command prompt from within the Start menu, navigate to the folder containing `get-pip.py`, and run:
   ```bash
   python get-pip.py

3. **Install Selenium WebDriver:**
   Open a command prompt or terminal and run:
   ```bash
   pip install selenium

## Clone this repository:
Create a new folder for your project and open a command prompt within the folder.

```bash
mkdir rk9-checker
cd rk9-checker
git clone https://github.com/YourGitHubUsername/rk9checker.git .
```

## Additional Instructions

## Generate an App Password:
1. Go to [Google Account Security](https://myaccount.google.com/security).
2. Under "Signing in to Google," select "App Passwords."
3. Generate a new app password for the script.

## Setup Chrome Profile:
1. Find your Chrome user data directory (usually `C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data`).
2. In `rk9.py`, replace the `--user-data-dir` argument with the path to your Chrome user data directory.

## Usage

### First Run (Login):
1. Run `rk9.py`.
2. When the Chrome window opens, log in to the website.
3. Close the script once you are logged in.

### Subsequent Runs (Checking):
1. Run `rk9.py` again.
2. The script will now check the page for the specified message every 10 seconds and send an email notification if the message changes.

## Email Notification:
1. Update the `send_email` function in `rk9.py` with your Gmail account, app password, and recipient email addresses.

## Contributing
Feel free to fork this project, make changes, and submit pull requests. Any contributions are welcome!
