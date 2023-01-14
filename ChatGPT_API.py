from chatgpt_wrapper import ChatGPT

bot = ChatGPT()
# response = bot.ask("Hello, world!")
response = bot.ask("Given this task, do you find any bug in the following code?")
print(response)  # prints the response from chatGPT