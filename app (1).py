import os
import streamlit as st
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
from apikey import apikey
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType

apikey = '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'

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = apikey

# Define Streamlit app
def app():
    # Title and description
    st.title("CSV Query App")
    st.write("Upload a CSV file and enter a query to get an answer.")
    file = st.file_uploader("Upload CSV file", type=["csv"])
    if not file:
        st.stop()

    df = pd.read_csv(file)
    st.write("Data Preview:")
    st.dataframe(df.head())

    # agent = create_pandas_dataframe_agent(
    #     OpenAI(temperature=0,model="gpt-3.5-turbo-0613"),
    #     df,
    #     tools=["pandas"],
    #     tool_names=["pandas"],  # Provide the DataFrame as 'df' variable in the prompt
    #     verbose=True
    # )
    agent = create_pandas_dataframe_agent(
    OpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
    df,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    query = st.text_input("Enter a query:")

    if st.button("Execute"):
        answer = agent.run(query)
        st.write("Answer:")
        st.write(answer)


if __name__ == "__main__":
    app()
