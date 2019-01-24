#!/usr/bin/python
import requests

# Check README.md file to create a Webhook URL
url = "WEBHOOK_URL"

# The message to post - JSON format
payload = '{"text": "Hello! _Message from Python Script_, Surprised?"}'

headers = {
  'content-type': "application/json"
}

# Post the message to Webhook URL
response = requests.request("POST", url, data=payload, headers=headers)

# Response will be `ok` when successfully posted to SLACK
print(response.text)
