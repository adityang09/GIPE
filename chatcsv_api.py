import requests
import json
import pandas as pd
import os
apikey = os.getenv("sk_zz3ZJWw2Uy99JTiNibydDfkBUP")
def post_request(msg: str):
    # Convert DataFrame to CSV string
    # csv_data = df.to_csv(index=False)
    
    messages = [
        {
            "role": "user",
            "content": "whats your name"
        },
        {
            "role": "assistant",
            "content": "bob"
        },
        {
            "role": "user",
            "content": f"{msg}"
        }
    ]  # Define your list of messages here

    headers = {
        "accept": 'text/event-stream',
        "Content-Type": 'application/json',
        "Authorization": 'Bearer sk_3ZJWw2Uy99JTiNibydDfkBUP'  # Replace `your_chatcsv_api_key` with your actual API key
    }
    payload = {
        "messages": messages,
        "files": [
            "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        ]
    }

    try:
        response = requests.post("https://www.chatcsv.co/api/v1/chat", json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 4xx, 5xx)

        # Check if response content is empty
        if response.text:
            # If not empty, print response content
            print(response.json())
        else:
            print("Response content is empty.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")

    return response.text

# Example usage:
# Assuming df is your DataFrame
# post_request("Message", df)
