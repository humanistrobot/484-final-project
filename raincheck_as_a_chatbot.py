#!/usr/bin/env python
# coding: utf-8

# In[118]:


get_ipython().system(' pip install chatterbot')
get_ipython().system(' pip install chatterbot_corpus')


# In[119]:


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# In[120]:


my_bot = ChatBot(name = 'Raincheck', read_only = True,
                 logic_adapters = 
  ['chatterbot.logic.MathematicalEvaluation',
   'chatterbot.logic.BestMatch'])


# In[121]:


small_talk = ['Hello! I am Raincheck.',
              'Where would you like to go today?',
              'Maybe you should take a jacket. Might rain.',
              'I am Raincheck.']


# In[122]:


list_trainer = ListTrainer(my_bot)

for item in (small_talk):
  list_trainer.train(item)


# In[123]:


print(my_bot.get_response("hello"))


# In[124]:


from chatterbot.trainers import ChatterBotCorpusTrainer

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')


# In[125]:


print(my_bot.get_response("hello"))


# In[126]:


print(my_bot.get_response("who are you?"))


# In[127]:


print(my_bot.get_response("what is your purpose?"))


# In[128]:


print(my_bot.get_response("how are you"))


# In[129]:


print("Raincheck: Hello, what should I call you?")
user_name = input()


# In[130]:


print("Raincheck: Can I learn what city you are in?")
city_name = input()


# In[131]:


bot_template = "Raincheck: {0}"
user_template = user_name + " : {0}"
city_template = city_name + " : {0}"


# In[132]:


import re 
import urllib.request 

class AppURLopener(urllib.request.FancyURLopener): 
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open('https://weather.com/tr-TR/weather/today/l/33d1e415eb66f3e1ab35c3add45fccf4512715d329edbd91c806a6957e123b49')
file_1 = response.read().decode('utf-8') 

pattern_1 = re.compile("([0-9]+°)") 

matches_1 = re.findall(pattern_1, file_1) 

print(matches_1)


# In[133]:


get_ipython().system(' pip install chatterbot-weather')


# In[ ]:


def getReply(message):
    if 'who' in message and 'you' in message:
        reply = "I'm Raincheck, at your service."
    elif 'weather' in message:
        reply = "Getting weather information..."
    else:
        reply = ""
    print('Raincheck: ' + reply)


# In[ ]:


print(my_bot.get_response("how is the weather in new york?"))


# In[135]:


name = "Raincheck"
weather = matches_1
mood = "Happy"

responses = {
    "What's your name?": [
    "They call me {0}". format(name),
    "I go by {0}". format(name),
    "My name is {0}". format(name) ],

    "What's the weather like today?": [
    "The weather is {0}".format(weather), 
    "It's {0} today".format(weather), 
    "Let me check, it looks {0} today".format(weather) ],

    "default": [
    "this is a default message"]
    
}


# In[136]:


print(my_bot.get_response("What's the weather like today?"))


# In[137]:


from chatterbot.trainers import ListTrainer

trainer = ListTrainer(my_bot)

trainer.train([
  'My name is Raincheck. How can I help?',
  'Looks like there\'s only clear skies today.',
  'Tell me what\'s in your wardrobe.',
  'What is the right weather for a jumpsuit anyway?'
])


# In[138]:


print(my_bot.get_response("Who are you?"))


# In[139]:


def respond(message):
  if message in responses: 
    bot_message = random.choice(responses[message])

  else:
    bot_message = random.choice(responses["default"])
    return bot_message


# In[140]:


print(my_bot.get_response("how is the weather today?"))


# In[141]:


def related(x_text): 
  if "name" in x_text: 
    y_text = "what's your name?"

  elif "weather" in x_text: 
    y_text = "what's today's weather?"

  elif "robot" in x_text: 
    y_text = "are you a robot?"

  elif "how are" in x_text: 
    y_text = "how are you?"

  else: 
    y_text = ""

  return y_text


# In[142]:


def send_message(message):
  print(user_template.format(message))
  response = respond(message)
  return(bot_template.format(response))


# In[ ]:


while 1: 
  my_input = input() 
  my_input = my_input.lower() 
  related_text = related(my_input) 
  send_message(message)

if my_input == "exit" or my_input == "stop": 
      break

