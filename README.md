# csv-chat-agent

# Conversational CSV Data Analyst 📊🤖

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.33-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.1-green.svg)
![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-API-yellow.svg)

A web application that allows you to have a conversation with your data. Upload any CSV file and ask questions in plain English to get instant insights, powered by a Large Language Model and the LangChain agent framework.

## 🚀 Live Demo

Before you can see a demo here, you'll need to create a `demo.gif` file of your app in action and place it in your project's root directory.

![App Demo GIF](demo.gif)

## ✨ Features

* **Natural Language Queries:** Ask complex questions about your data in plain English.
* **Dynamic Code Generation:** An AI agent writes and executes Python (Pandas) code on the fly to find answers.
* **Interactive UI:** A simple and clean web interface built with Streamlit for uploading files and chatting.
* **Flexible and Powerful:** Supports any CSV file structure and leverages powerful open-source LLMs (like Mistral-7B) from Hugging Face.

---

## 🛠️ Tech Stack

* **Backend:** Python, LangChain (Agents)
* **Frontend:** Streamlit
* **LLM Provider:** Hugging Face (Inference API)
* **Data Handling:** Pandas

---

## ⚙️ Setup and Installation

Follow these steps to run the project locally.

**1. Clone the repository:**
```bash
# !!! IMPORTANT: Replace this URL with your own repository URL !!!
git clone [https://github.com/architpr/csv-chat-agent.git)
cd csv-chat-agent
```

**2. Create and activate a virtual environment:**
```bash
# Create the environment
python -m venv .venv

# Activate on Windows
.venv\Scripts\activate
```

**3. Create and install requirements:**
First, create a `requirements.txt` file by running this command in your terminal. This file lists all the necessary libraries for the project.
```bash
pip freeze > requirements.txt
```
Then, install the libraries from this new file.
```bash
pip install -r requirements.txt
```

**4. Create a `.env` file:**
Create a file named `.env` in the root of the project folder and add your Hugging Face Access Token.
```
HUGGINGFACEHUB_API_TOKEN="hf_YourSecretTokenGoesHere"
```

---

## 🏃‍♀️ How to Run the Application

Once the setup is complete, run the following command in your terminal:

```bash
streamlit run app.py
```

Your web browser will open a new tab with the running application.

### Usage

1.  Open the application in your browser.
2.  Click the "Browse files" button to upload a CSV file from your computer.
3.  Once the data preview appears, type your question into the text box.
4.  Press Enter and wait for the AI agent to generate the answer.

---

## 🤖 How It Works

This project uses an **Agentic AI** approach. Instead of just answering questions from a knowledge base, the agent is a "doer" that uses tools to find new information.

1.  **The Goal:** The agent receives your question in English.
2.  **The Tool:** It has access to the uploaded CSV file via the Pandas library.
3.  **Reasoning & Action:** The LLM (the agent's "brain") thinks about the question, writes the correct Pandas code to analyze the data, and executes it.
4.  **Response:** The agent takes the result from the code and formulates a final, human-readable answer.
