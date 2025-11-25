# Career Guidance Chatbot Setup Process

This document outlines the step-by-step process executed to set up and run the Career Guidance Chatbot using Streamlit and Gemini API.

## Prerequisites
- Python 3.13 installed
- Internet connection for API calls and package installations
- Virtual environment (venv) in the project directory

## Step-by-Step Execution Log

### 1. Initial Directory Listing
Command: `list_files` on current directory
- Listed all files in c:/Users/ADMIN/OneDrive/Desktop/career -bot
- Found: .env, careerBot.py, LICENSE, README.md, requirements.txt, Screenshot.png, __pycache__/, Career-Guidance-ChatBot-main/

### 2. Attempted CMake Installation (Optional)
Command: `winget install cmake`
- This was attempted but failed with exit code 1602
- Not required for the chatbot functionality

### 3. Initial Python Execution Attempt
Command: `python careerBot.py`
- Failed due to missing modules: streamlit, requests, dotenv
- Error: ModuleNotFoundError

### 4. Package Installations
Installed the following packages sequentially to resolve dependencies:

- `pip install protobuf` - Required for Google API protobuf handling
- `pip install typing-extensions` - Required for type hints in newer Python versions
- `pip install cachetools` - Required for Streamlit caching
- `pip install requests` - For HTTP API calls to Gemini
- `pip install python-dotenv` - For loading environment variables from .env file
- `pip install click` - Required for Streamlit CLI
- `pip install tornado` - Web server for Streamlit
- `pip install toml` - Configuration file parsing
- `pip install packaging` - Package version handling

### 5. Final Streamlit Execution
Command: `streamlit run careerBot.py`
- Successfully launched the Streamlit app
- Local URL: http://localhost:8501
- Network URL: http://192.168.8.170:8501
- App is now running and accessible in browser

## Dependencies Summary
The following packages were installed:
- protobuf
- typing-extensions
- cachetools
- requests
- python-dotenv
- click
- tornado
- toml
- packaging

## Notes
- The app requires a valid GEMINI_API_KEY in the .env file or Streamlit secrets
- Internet connection is required for API calls to Google's Gemini service
- The app uses Gemini 2.0 Flash model for generating career guidance responses
- All installations were done in the virtual environment (venv)

## Troubleshooting
If the app fails to start:
1. Ensure all dependencies are installed
2. Check that GEMINI_API_KEY is properly set
3. Verify internet connectivity for API calls
4. Restart the Streamlit server if needed

## Current Status
✅ App is successfully running on http://localhost:8501
⚠️ API calls may fail if there's no internet connection (DNS resolution error observed)
