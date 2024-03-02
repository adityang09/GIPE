import streamlit as st
import pandas as pd
import os
import io
import matplotlib.pyplot as plt
import re
st.title("CSV ChatBot")

from chatcsv_api import post_request

# File Upload
# uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
uploaded_file = True
# Load CSV data if a file is uploaded
if uploaded_file:
    # st.success("File uploaded successfully!")
    # df = pd.read_csv(uploaded_file)

    # Create CSV Agent
    # agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True,return_intermediate_steps=True,include_df_in_prompt=True) 

    # Chatbot Interaction
    conversation_history = st.session_state.get("conversation_history", [])
    for entry in conversation_history:
        with st.chat_message("User"):
            st.write(entry['user'])
        with st.chat_message("Bot"):
            st.write(entry['chatbot'])
        st.write("")
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    user_question = st.chat_input("Ask a question:")
    
    if user_question:
        
        with st.chat_message("User"):
            st.write(user_question)
       
       
        with st.chat_message("Bot"):
            with st.spinner("Generating..."):
                # response = agent(user_question)
                response = post_request(user_question)
                # st.write(response["intermediate_steps"][0][1])
                # # if "graph" in user_question.lower():
                # st.pyplot()
                st.write(response)
                # Regular expression pattern to extract the link
                pattern = r'\(https?://[^\s()]+\)'

                # Using findall to extract all URLs matching the pattern
                urls = re.findall(pattern, response)

                # Extracting the first URL (assuming there's only one URL in the string)
                if urls:
                    extracted_link = urls[0][1:-1]  # Removing parentheses from the extracted link
                    st.image(extracted_link)
                else:
                    print("No URL found in the string.")

                

        # Optionally, you can do more processing or visualization based on the response
        # For example, if the response is a command to plot a graph, you can add code here to plot it.

        # Store the conversation for reference
        conversation_history.append({"user": user_question, "chatbot": response})
        st.session_state["conversation_history"] = conversation_history
        if st.button("Reset Conversation"):
            st.session_state["conversation_history"] = []
            st.success("Conversation history cleared.")

