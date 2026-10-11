# Internet Speed Test ⚡

A simple internet speed test website built using Python and Flask. It measures download speed, upload speed, and ping using the `speedtest-cli` library.

## Features

- Measure download speed in Mbps
- Measure upload speed in Mbps
- Display ping in milliseconds
- Simple, responsive user interface
- Loading animation while the test runs
- Error handling for failed speed tests

## Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript
- speedtest-cli

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/internet-speed-test.git
cd internet-speed-test
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## How It Works

Flask connects the browser interface to the Python speed-test code. The application measures download speed, upload speed, and ping, then displays the results on the webpage.

## Limitations

Results depend on the selected test server, network conditions, and the speedtest library. When deployed to a remote server, the test measures the server's connection rather than the visitor's connection.

## Future Improvements

- Better test progress indicators
- Test history
- Improved error messages
- Live website deployment

