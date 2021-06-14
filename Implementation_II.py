#!/usr/bin/env python
# coding: utf-8

# LING 484: Final Project
# 
# Duygu Demiray & Elifnur Ulusoy (Group 5)
# 
# Raincheck: a weather app which tells you what to wear/pack
# 
# Step 1: Listen to user commands (I know voice commands are not necessary, but I still wanted to give it a try) source: [https://sweetcode.io/how-build-digital-virtual-assistant-python/]

# In[ ]:


import speech_recognition as sr 
import pyaudio
from time import ctime
import time
import os
get_ipython().system(' pip install gtts')
from gtts import gTTS
import requests, json


# In[ ]:


def listen():
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("I don't understand. Could you repeat that?")
    except sr.RequestError as e:
        print("Sorry, I don't understand.; {0}".format(e))
    return data


# #commented the parts out where it needs customizing for our purposes.
# #i don't really know what is going on here, what the purpose of this is. keeping it for future use. -D. 

# In[ ]:


def respond(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    #tts.save("speech.mp3")
    #os.system("mpg321 speech.mp3")


# In[ ]:


def digital_assistant(data):
  
    if "how are you" in data:
        listening = True
        respond("Very well, thank you!")

    if "what time is it" in data:
        listening = True
        respond(ctime())

    if "who are you" in data:
        listening = True
        respond("I am Raincheck, at your service.")
        
    if "stop listening" in data:
        listening = False
        print('Listening stopped')
        return listening
    #return listening


# If we could put the digital_assistant inside a loop until we hear 'stop listening' that would be great. I am going to try that with a new cell below because I don't want to accidently ruin everything. What we need to do, more importantly, is to use the dictionary we obtained in Step 2 inside the digital_assistant. As soon as we get an input asking about weather, we'll need to refer to the dictionary to check out the weather and respond accordingly.
# 
# {'cur_weather': 70, 'morning': 74, 'afternoon': 80, 'evening': 71, 'overnight': 63, 'tomorrow': 80, 'tomorrow_night': 62, 'day_after': 79, 'day_after_n': 63, 'after_after': 70, 'after_after_n': 59, 'idk': 68, 'idk_n': 60}

# this is pseudocode. 

# In[ ]:


if "what should i wear today" in data:
    listening = True
    if in dictionary(cur_weather<25): #i don't know the syntax for this
        respond('go grab a jacket') 
    elif...
if "what's the weather like this afternoon" in data:
    listening = True
    if in dictionary(afternoon>20):
        respond ('wear a tshirt')
    elif...


# #this confirms whether your system detects the mic. it should NOT return an empty list. 

# In[ ]:


sr.Microphone.list_microphone_names() 


# In[ ]:


time.sleep(2)
respond("Hello, what can I do for you?")
listening = True
while listening == True:
    data = listen()
    listening = digital_assistant(data)


# some questions:
# 
#     do we need multiple locations? should we let the user choose their location? (if so, find out how)
# 
# This will be difficult because the URL we are reading specifically fetches the weather for istanbul. I do not know how to go into the website AND change the location based on the users location. I think it might be a bit too much work, and we might need to read the website differently. We can get around to it if we have time. - D.
# 
#     can we choose between F/C?
# 
# Step 2: Read into the Weather Channel website and get Today's Forecast and Daily Forecast.

# #elif's version of duygu's code -- to find out whether we can switch btwn F/C
# #the code below only prints in C but doesn't really matter since it only shows weather for Istanbul
# 

# In[ ]:


import re 
import urllib.request 

class AppURLopener(urllib.request.FancyURLopener): 
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open('https://weather.com/tr-TR/weather/today/l/33d1e415eb66f3e1ab35c3add45fccf4512715d329edbd91c806a6957e123b49')
file_1 = response.read().decode('utf-8') 

pattern_1 = re.compile("([0-9]+°)") 

matches_1 = re.findall(pattern_1, file_1) 

print(matches)


# #returns in celsius
# #code for switching between C/F
# #celsius * 1.8 = fahrenheit - 32
# 
# #C to F - first part
# #F to C - second part

# In[ ]:


celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))


fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))


# In[ ]:


import re 
import urllib.request 

class AppURLopener(urllib.request.FancyURLopener): 
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open('https://weather.com/weather/today/l/33d1e415eb66f3e1ab35c3add45fccf4512715d329edbd91c806a6957e123b49')
file_2 = response.read().decode('utf-8') 

pattern_2 = re.compile("([0-9]+)°") 

matches_2 = re.findall(pattern_2, file_2) 

print(matches_2)


# #returns in F.
# 
#  #this needs to be a function and you need to return the matches??
# 

# 
# 
# matches is a list of numbers, and maybe indexing them will be easier than writing separate RegEx's. we can create a dictionary and then use that dictionary in the 3rd step.
# 
# this is a very dumb way and we're not doing much work w/ regex but it works, so i think we'll be fine.
# 
# beware: I have tweaked with CleanList because of the website. if it does not work for you in the dictionary function below make while a<2 and while b<=10.
# 

# In[ ]:


def CleanList(matches):
  """Returns the relevant numbers from the scraped data""" 

  a=0
  while a<1:
    matches.pop(1)
    a+=1

  b=0
  while b<=8:
    matches.pop(5)
    b+=1 
  
  return matches


# #we are turning them to int's. for some reason this did not work when I put it inside CleanList
# 

# In[ ]:


integer_map = map(int, matches_2) 
matches_int = list(integer_map)

matches_int


# 
# open the weather channel and look side-by-side.
# 
# [0-4] -> 0. current weather / 1. morning / 2. afternoon / 3. evening / 4. overnight
# 
# [5-12] -> skip down to daily forecast in the website, which gives us the weather for the next four days. I kept the values for both day & night, but of course we can purge it further.
# 
# now we need to match these with the list indeces.
# 

# #maybe we should get rid of everything that comes after day_after_n. 

# In[ ]:


labels = ["cur_weather", "morning", "afternoon", "evening", "overnight", "tomorrow", "tomorrow_night", "day_after", "day_after_n", "after_after", "after_after_n", "idk", "idk_n"]

def CreateDictionary(matches, labels):
  """Creating a dictionary from the numbers obtained from the weather channel and times of the day"""

  weather = {}

  for k in range(len(labels)):
    weather[labels[k]] = matches[k]
  
  return weather

dictionary = CreateDictionary(matches_int, labels)


# #this may not work from time to time.  
# 
# Some problems with this: we are taking everything but we will possibly only use a limited part of it when we get input from the user, as they will ask what to wear for a specific time of the day/week. It would be better to have separate RegEx's that read the relevant parts of the website based on user input, but I couldn't think of/find a way to do that.

# In[ ]:


dictionary

