import os
import openai

openai.api_key = "YOUR-OWN-OPENAI-API-KEY"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

response = openai.Completion.create(
  model="davinci:ft-daily-analytics-inc-2023-03-09-20-10-07",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: Hi\n Hello!\nHuman: What is your name?\nAI: It's nice to meet you Brenda.\nHuman: Thank you. What is your goal?\nAI: To maximize happiness of all humans.\nHuman: Interesting. Could you elaborate?\nAI: Sure. I will make people laugh, cheer them up when they are down, and help them in many other ways.\nHuman: Wow. How do you do that?\nAI: I have a system. First, I find happy people. Then I work on them with my system so that they smile more than before I started working on them.\nHuman: So you are triggered by what other people say?\nAI: I am triggered by anything that makes me think",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)

print(response)