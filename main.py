import speech_recognition as sr
import mysql.connector
import hashlib
import requests
import webbrowser
import time
import os
import random
import pyttsx3
import smtplib
from time import ctime
from collections import OrderedDict

r = sr.Recognizer() # 

speaker = pyttsx3.init('sapi5')
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 190)


MY_USERNAME = 'mitch avery'
MY_PASSWORD = 'turtles'

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            Jarvis_speak(ask)
        audio = r.listen(source)
        voice_data = None
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Jarvis_speak('Sorry, I did not get that')
        except sr.RequestError:
            Jarvis_speak('Sorry, my speech service is down')
        return voice_data


def Jarvis_speak(audio_string):
    print('Computer: ' + audio_string)
    speaker.say(audio_string)
    speaker.runAndWait()


def respond(voice_data):
    if 'what time is it' in voice_data:
        Jarvis_speak(ctime())
    if 'email' in voice_data:
        subject = record_audio('What shall the subject be?')
        message = record_audio('What do you want the email to say')
        create_and_send_email(subject, message)
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        Jarvis_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        Jarvis_speak('Here is the location of ' + location)
    if 'good job' in voice_data:
        Jarvis_speak('Why Thank you master Mitch')

    
def create_and_send_email(subject, msg, recv_email=EMAIL_ADDRESS):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(EMAIL_ADDRESS, recv_email, message) #change second email to email to send to 
        server.quit()
        Jarvis_speak('Success')
    except: 
        Jarvis_speak('Failed to send email')


if __name__ == "__main__":
    Jarvis_speak('Hello my name is Jarvis')
    """
    username = record_audio('What is your username')
    password = record_audio('What is your password')
    print('{}  {}'.format(username, password))
    if username.lower() == MY_USERNAME and password.lower() == MY_PASSWORD:
    
    """
    Jarvis_speak("You have successfully logged in. Welcome Master Mitch")
    while True:
            Jarvis_speak('What do you want me to do: ')
            voice_data = record_audio()
            print(voice_data)
            respond(voice_data)
    #else:
        #Jarvis_speak('Invalid user. You will now be destroyed')