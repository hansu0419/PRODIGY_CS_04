# Keylogger Web Interface

## Description
The Keylogger Web Interface is a Python-based web application designed to capture and log keystrokes from a user's keyboard. This tool enables real-time tracking of key presses and provides functionality to download the logged data for further review. It features a user-friendly web interface for enabling or disabling logging, checking the latest key press, and downloading the log file.

## Features

- **Web Interface:** A simple and intuitive interface for managing the keylogger. Users can easily enable or disable logging and check the most recent key press via their web browser.

- **Real-time Logging:** Captures each key press in real-time when logging is enabled. Data is written to a file immediately, ensuring accurate recording of user input.

- **Download Log File:** Provides an option to download the key press log file for offline access and analysis.

- **Toggle Logging:** Allows users to enable or disable keylogging through the web interface, providing control over when keystrokes are recorded.

- **Instant Key Press Check:** Retrieve the most recent key press from the server instantly.

- **Responsive Design:** The web interface is designed to be accessible and functional across various devices, ensuring a consistent user experience on different screen sizes.

## Requirements

- Python 3.x
- Flask
- Keyboard

### Install Dependencies
To install the required Python packages, run:
```bash
$ pip install flask
$ pip install keyboard
```

### Running the Web App Locally
To run the web application locally and open it in your browser:
```bash
$ python app.py
```

After running the command, open the application by navigating to [http://127.0.0.1:9090/](http://127.0.0.1:9090/) in your web browser.

## DEMO

Explore the web application to interact with its features. Use the interface to control logging and download the key press log file. Ensure that you use this tool responsibly and only on devices and systems where you have appropriate permission to log keystrokes.

**Note:** Always adhere to ethical guidelines and legal regulations when using or deploying keylogging software. Unauthorized keylogging can be illegal and unethical.
