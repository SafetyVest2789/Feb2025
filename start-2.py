import ollama


response = ollama.list()
# print(response)

# *** Chat example ***

res = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Can you explain common API usage?"},
    ],
)
# print(res["message"]["content"])

# ** Chat example streaming **
res = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "What common syntax problems are there in an API?",
        },
    ],
    stream=True,
)
for chunk in res:
#    print(chunk["message"]["content"], end="", flush=True)






res = ollama.generate(
    model="llama3.2"
    prompt="what is JSON notation?",
)

# show
#print(ollama.show("llama3.2"))



# Create new model with modelfile
modelfile = """
FROM llama3.2
SYSTEM You are a very smart coding assistant who knows everythin about APIs
PARAMETER temperature 0.1
"""

ollama.create(model="knowitall", modelfile=modelfile)

res = ollama.generate(model="knowitall", prompt="What can make an API function properly?")
print(res["response"])