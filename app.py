import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv

# Import the necessary LangChain classes
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# Function to create the AI agent
def create_agent(df: pd.DataFrame):
    """Creates an AI agent powered by a Hugging Face chat model."""
    
    # Load environment variables (for local development)
    load_dotenv()

    # Try to get the API key from environment variables (local) or Streamlit secrets (cloud)
    api_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN") 
    if not api_token and "HUGGINGFACEHUB_API_TOKEN" in st.secrets:
        api_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
        os.environ["HUGGINGFACEHUB_API_TOKEN"] = api_token

    if not api_token:
        st.error("Hugging Face API token is missing! Please configure it in your Streamlit Cloud Secrets.")
        st.stop()

    # Define the model repository ID
    # Using Qwen 2.5 72B which is supported by Hugging Face's serverless inference API
    repo_id = "Qwen/Qwen2.5-72B-Instruct"

    # 1. Initialize the standard Hugging Face LLM endpoint
    llm = HuggingFaceEndpoint(
        repo_id=repo_id,
        temperature=0.2,
        max_new_tokens=512,
        huggingfacehub_api_token=api_token
    )

    # 2. Wrap the LLM in a ChatHuggingFace object to match API expectations
    chat_model = ChatHuggingFace(llm=llm)

    # 3. Create the pandas DataFrame agent
    agent = create_pandas_dataframe_agent(
        chat_model,
        df,
        verbose=True,
        allow_dangerous_code=True,
        agent_executor_kwargs={"handle_parsing_errors": True},
    )
    
    return agent

# Main function to define the Streamlit app's UI
def main():
    """Defines the Streamlit user interface and handles the main logic."""
    
    st.set_page_config(page_title="Talk to Your CSV 📊")
    st.title("Talk to Your CSV 📊")
    st.write("Upload a CSV file and ask questions about your data!")

    # Allow the user to upload a CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the uploaded file into a pandas DataFrame
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.write(df.head())
        
        # Create the agent
        agent = create_agent(df)

        # Create a text input for the user's question
        user_question = st.text_input("Ask a question:")

        if user_question:
            # Display a spinner while the agent is working
            with st.spinner("Thinking..."):
                try:
                    # Invoke the agent and get the response
                    response = agent.invoke(user_question)
                    st.write("Answer:", response["output"])
                except Exception as e:
                    # Catch the HfHubHTTPError and other exceptions to display a clear error message
                    st.error(f"An error occurred while communicating with the Hugging Face API: {str(e)}")
                    st.info("If this is an HTTP or authentication error, verify that your Hugging Face API key is correct and has access to the model, or check if the model is currently experiencing downtime.")

# Entry point for the script
if __name__ == "__main__":
    main()