# How to use Aiinfusion Text Moderation by Annoyance Analysis API with RapidApi

> In this project, we are going to integrate the Aiinfusion text moderation by annoyance analysis api in a `Python` project.
> The text moderation analysis service is provided by [AIINFUSION LTD  ](https://www.aiinfusion.co.uk/) and it is available via RapidAPI. 

### What it is a Text moderation by annoyance analysis api.  

The aiinfusion text moderation analysis, has the aim to automatically identify negative behaviours, like toxic comments that might be perceived as rude and disrespectful.
Toxic comments are the comments that are rude, offensive, or unfair and usually cause many users to exit the conversation. 


> With this project you can moderate and analyse your messages.
> You will get two labels: an Annoyance (toxicity) and Neutral percentage of your message for an easy detection of offensive, not healthy post to moderate.




### Requirements

1) Sign Up for a free account at [RapidAPI.com](https://rapidapi.com/aiinfusion-ltd-aiinfusion-ltd-default/api/annoyance-analysis/)
2) Subscribe to the [Annoyance Analysis API](https://rapidapi.com/aiinfusion-ltd-aiinfusion-ltd-default/api/annoyance-analysis/) – It is free to use up to 10,000 API calls per month. Here is the full pricing table for the API:

<img width="1103" alt="aiinfusion plan " src="https://user-images.githubusercontent.com/97127125/148459729-6fe8b462-12f4-49e4-a116-bffb4b8eaac3.png">



4) Connect to Annoyance Analysis API using the language of your choice from the API Endpoints page.  


# __Let's start...__ 🛫

This project use Python and [Anaconda](https://www.anaconda.com/products/individual) as package manager. Install Anaconda from [HERE](https://www.anaconda.com/products/individual) 

Use your terminal and copy and paste the following steps:

```bash
$ conda create --name annoyance-analysis python=3.9
$ conda activate annoyance-analysis
$ conda install pyyaml
$ conda install requests
```

### Download the example project from the repository


In the project folder, you will find three different files: config.yml, payload.py and main.py


### Set the YML Config File with the RapidApi key

Open the `yaml config` file _config.yml_ with your editor and replace the below parameters with the RapidApi ones has provided.

```yml
x-rapidapi-host : annoyance-analysis.p.rapidapi.com
x-rapidapi-key : 7264**********
content-type : application/json
url : https://annoyance-analysis.p.rapidapi.com/v1/annoyance


```


### Run the main.py. 

```bash
$ python main.py

```

### This will be the result.

```json
{id": "608a2d8e-62b3-11ec-94d7-0242ac110002",
"external_id": "my_external_id", 
"annoyance": 0.9940999746322632, 
"neutral": 0.009399999864399433, 
"winner": "annoyance", 
"timestamp": "2021-12-21T23:11:49.997993"}
```


\
&nbsp;
\
&nbsp;



# Project description


### payload.py

The file `payload.py` describe the `Payload` class. `Payload` is the data model expected by the Aiinfusion Text moderation analysis API.
It takes as parameters the text id and the text to moderate.   

```python
# payload.py
class Payload:
    def __init__(self, text:str, external_id:str):
        self.text:str = text
        self.external_id:str = external_id
```

### main.py

Load the `config.yml` to set the RapidApi paramenters.

```python
# main.py
import yaml
with open('config.yaml') as f:
    config = yaml.safe_load(f)
```   

Import external libs.

In the `main.py`, import the `requests` and `json` libraries and the `Payload` class.

```python
# main.py
from payload import Payload
import requests
import json
```

Instantiate the payload with the text and the unique text id.

```python
# main.py
payload = Payload(
    text = "you are a fuc**** S***t",
    external_id = "my_external_id"
)
```

Set the header for the Post request.

```python
# main.py
headers = dict()
headers['content-type'] = config['content-type']
headers['x-rapidapi-host'] = config['x-rapidapi-host']
headers['x-rapidapi-key'] = config['x-rapidapi-key']
```

Invoke the Aiinfusion Annoyance api endpoint and print the response.

```python
# main.py
response = requests.request("POST", config['url'], data=json.dumps(payload.__dict__), headers=headers)
print(response.json())
```



### This will be the result.

```json
{id": "608a2d8e-62b3-11ec-94d7-0242ac110002",
"external_id": "my_external_id", 
"annoyance": 0.9940999746322632, 
"neutral": 0.009399999864399433, 
"winner": "annoyance", 
"timestamp": "2021-12-21T23:11:49.997993"}
```

## That's all! 🛬
