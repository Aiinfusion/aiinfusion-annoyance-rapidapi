# Import the config file
import yaml
with open('./config.yml') as f:
    config = yaml.safe_load(f)

# Import external libs
from payload import Payload
import requests
import json

# Instantiate the payload.
payload = Payload (
    text = "you are a fucking shit",
    external_id = "my_external_id"
)

# Set the header Post request.
headers = dict()
headers['content-type'] = config['content-type']
headers['x-rapidapi-host'] = config['x-rapidapi-host']
headers['x-rapidapi-key'] = config['x-rapidapi-key']

# Invoke the endpoint and print the response.
response = requests.request("POST", config['url'], data=json.dumps(payload.__dict__), headers=headers)
print(response.json())