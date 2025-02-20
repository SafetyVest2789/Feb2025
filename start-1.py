import requests
import json 

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3.2",
    "prompt": "Tell me how to write an API using JSON notation in Python.",
}

response = requests.post(url, json=data, stream=True)


# check response status
if response.status_code == 200:
    print("Generated Text:", end=" ", flush=True)
    #Iterating over streaming response
    for line in response.iter_lines():
        if line:
            # Decode line and parse JSON
            decoded_line = line.decode("utf-8")
            result = json.loads(decoded_line)
            #Get text from response
            generated_text = result.get("response", "")
            print(generated_text, end="", flush=True)
else:
    print("Error:", response.status_code, response.text)