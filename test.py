import os
import openai

# Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"
models = openai.Model.list()

prompt = "Task: Duplicate elimination. Write a function remove_extras(lst) that takes in a list and returns a new list with all repeated occurrences of any element removed. For example, remove_extras([5, 2, 1, 2, 3]) returns the list [5, 2, 1, 3]."
response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=1000)
print(response.choices[0].text)
response = openai.Completion.create(model="text-davinci-003", prompt="is there any fault in this code?", temperature=0, stream=True, max_tokens=1000)
print(response.choices[0].text)