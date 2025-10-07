import streamlit as st
import pandas as pd
from dotenv import load_dotenv

# Import the necessary LangChain classes
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# Function to create the AI agent
def create_agent(df: pd.DataFrame):
    """Creates an AI agent powered by a Hugging Face chat model."""
    
    # Load environment variables (for the Hugging Face API token)
    load_dotenv()

    # Define the model repository ID
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2"

    # 1. Initialize the standard Hugging Face LLM endpoint
    llm = HuggingFaceEndpoint(
        repo_id=repo_id,
        temperature=0.2,
        max_new_tokens=512,
    )

    # 2. Wrap the LLM in a ChatHuggingFace object to match API expectations
    chat_model = ChatHuggingFace(llm=llm)

    # 3. Create the pandas DataFrame agent
    agent = create_pandas_dataframe_agent(
        chat_model,
        df,
        verbose=True,
        allow_dangerous_code=True,
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
                # Invoke the agent and get the response
                response = agent.invoke(user_question)
                st.write("Answer:", response["output"])

# Entry point for the script
if __name__ == "__main__":
    main()