from chatgpt_wrapper import ChatGPT
from chatgpt_wrapper.core.config import Config

config = Config()
config.set('chat.model', 'gpt4')
bot = ChatGPT(config)
success, response, message = bot.ask("Hello, world!")
print(message)