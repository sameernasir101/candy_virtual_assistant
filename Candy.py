from email.mime.base import MIMEBase
from os import system
import requests
import time

def isUserConnectedToInternet():
    system('cls')
    candy = 'Candy: Virtual Assistant'
    string = 'Made By: Sameer Nasir'
    print(f"{candy:-^50}")
    print(f"{string:-^50}\n")
    time.sleep(0.5)
    print("Checking Internet Connectivity.... Please Wait...")
    url = "http://www.kite.com"
    try:
        requests.get(url, timeout=5)
        time.sleep(0.8)
        print("Internet Connection OK!")
        time.sleep(0.5)
        print("Launching Candy Virtual Assitant...")
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False

if isUserConnectedToInternet() == True:
    import os
    import wmi
    import sys
    import time
    import psutil
    import random
    import smtplib
    import getpass
    import pyjokes
    import pyttsx3
    import requests
    import datetime
    import operator
    import pyautogui
    import speedtest
    import wikipedia
    import webbrowser
    import instaloader
    import pywhatkit as kit
    from requests import get
    from email import encoders
    from selenium import webdriver
    import speech_recognition as sr
    from email.mime.text import MIMEText
    from instadownloader import instaloader
    from email.mime.multipart import MIMEMultipart 
    from selenium.webdriver.chrome.options import Options 

# Set Current Directory
    CURRENT_DIR = str(os.getcwd()) + ("\\")

# Set current Username
    CURRENT_USER = getpass.getuser()


# Set Windows and Program Files Directories
    SYSTEM32_PATH = 'C:\\Windows\\System32\\'
    PROGRAMFILES_PATH = 'C:\\Program Files\\'
    PROGRAMFILES86_PATH = 'C:\\Program Files (x86)\\'

# Set Default Browser
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(PROGRAMFILES_PATH + "Google\\Chrome\\Application\\chrome.exe"))
    except Exception:
        print("\nChrome Browser is not installed in your system. Install the program. Then run Candy Virtual Assistant.")
        exit()
        
# Set Voice Engine
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

# Text To Speech
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

# Print and speak strings
    def printSpeak(senetence):
        print(senetence)
        speak(senetence)

# Greet Me
    def greetMe():
        hour = int(datetime.datetime.now().hour)

        if(hour >= 0 and hour < 12):
            printSpeak("Good Morning Sir.")
        elif(hour >= 12 and hour < 18):
            printSpeak("Good Afternoon Sir.")
        else:
            printSpeak("Good Evening Sir.")
        printSpeak("My name is 'Candy'. I am your personal assistant. How can I help you?")

# Take Input(Voice) From User
    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:    
                print("\nListening...")
                r.pause_threshold = 0.8
                # r.adjust_for_ambient_noise(source, 1)
                r.energy_threshold = 1500
                # r.dynamic_energy_threshold = True
                audio = r.listen(source, timeout = 5, phrase_time_limit = None)
                print("Recognizing....")
                query = r.recognize_google(audio, language = 'en-in')
                print(f"You said: {query}")
                query = str(query).lower()
                return query
            except Exception:
                return ''
# Take Permission
    def takePermission():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:    
                r.pause_threshold = 0.8
                r.energy_threshold = 1500
                audio = r.listen(source, timeout = 5, phrase_time_limit = None)
                query = r.recognize_google(audio, language = 'en-in')
                query = str(query).lower()
                return query
            except Exception:
                return ''


# Tell some news - FUNCTION
    def news():
        url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=632c27d93d084a728d327fa5d1973060'

        mainPage = requests.get(url).json()
        articles = mainPage["articles"]
        head = []
        day = ["first", "second", "third"]
        for art in articles:
            head.append(art["title"])
        for i in range(0,len(day)):
            printSpeak(f"Today's {day[i]} news is: {head[i]}")
            time.sleep(0.5)

# Twitter Account Info - FUNCTION
    def getTwitterAccountInfo():
        file_path = CURRENT_DIR + "account\\account.txt"
        with open(file_path, "r") as f:
            credentials = f.readlines()
            username = credentials[0]
            password = credentials[1]
            return username, password

# Set an alarm - FUNCTION
    def addAlarm(alarm_hour, alarm_min):
        if alarm_hour < 0 or alarm_hour > 23 or alarm_min < 0 or alarm_min > 59:
            printSpeak("\nSorry, you have enetred invalid time format.")
        else:
            printSpeak("\nAlarm set successfully.")
            strTime = str(alarm_hour) + ':' + str(alarm_min)
            printSpeak(strTime)
            alarm_hour = int(alarm_hour)
            alarm_min = int(alarm_min)
            alarmRing = False
            while alarmRing != True:
                current_hour = int(datetime.datetime.now().strftime("%H"))
                current_min = int(datetime.datetime.now().strftime("%M"))
                time.sleep(5)
                if alarm_hour == current_hour:
                    if alarm_min == current_min:
                        alarmRing = True
            printSpeak("\nWake Up Sir!")
        

# Main Program Starts Here...
    def tasks():
        system('cls')
        greetMe()
        cycle = True
        count = 0
        while cycle:

            askForMore = True
                        
            try:
                query = takeCommand()
            except Exception:
                pass

            if query != None:

# Open Notepad
                if 'open notepad' in query or 'write something in notepad' in query:
                    try:
                        path = SYSTEM32_PATH + "notepad.exe"
                        os.startfile(path)
                        speak("Notepad opened for you.")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not find the app you are looking for.")

# Close Notepad
                elif 'close notepad' in query or 'quit notepad' in query:
                    try:
                        speak("Closing Notepad.")
                        os.system("taskkill /f /im notepad.exe")
                        count = 0
                    except Exception:
                        printSpeak("\nNo such Application is running.")

# Open CMD
                elif 'open command prompt' in query or 'open cmd' in query:
                    try:
                        path = SYSTEM32_PATH + "cmd.exe"
                        os.startfile(path)
                        speak("Command Prompt opened for you.")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not find the app you are looking for.")

# Close CMD
                elif 'close cmd' in query or 'quit cmd' in query or 'close command prompt' in query or 'quit command prompt' in query:
                    try:
                        speak("Closing Command Prompt.")
                        os.system("taskkill /f /im cmd.exe")
                        count = 0
                    except Exception:
                        printSpeak("\nNo such Application is running.")
                
# Open Google Chrome
                elif 'open chrome' in query or 'open browser' in query or 'open google' in query or 'open google chrome' in query:
                    try:
                        path = PROGRAMFILES_PATH + "Google\\Chrome\\Application\\chrome.exe"
                        os.startfile(path)
                        speak("Google Chrome opened for you.")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not find the app you are looking for.")

# Close Google Chrome
                elif 'close google chrome' in query or 'quit google chrome' in query or 'close chrome' in query or 'quit chrome' in query or 'close browser' in query or 'quit browser' in query:
                    try:
                        speak("Closing Google Chrome.")
                        os.system("taskkill /f /im chrome.exe")
                        count = 0
                    except  Exception:
                        printSpeak("\nNo such Application is running.")

# Open Visual Studio Code
                elif "let's code" in query or 'open visual studio code' in query or 'open visual studio' in query or 'open coding program' in query:
                    try:
                        path = "C:\\Users\\samee\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                        os.startfile(path)
                        speak("Visual Studio Code opened for you.")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not find the app you are looking for.")

# Close Visual Studio Code
                elif 'close visual studio code' in query or 'quit visual studio code' in query or 'close coding program' in query or 'quit coding program' in query:
                    try:
                        speak("Closing Visual Studio Code.")
                        os.system("taskkill /f /im Code.exe")
                        count = 0
                    except Exception:
                        printSpeak("\nNo such Application is running.")

# Open Shareit
                elif 'open share it' in query or 'share something' in query:
                    try:
                        path = PROGRAMFILES86_PATH + "SHAREit Technologies\\SHAREit\\SHAREit.exe"
                        os.startfile(path)
                        speak("I opened share it for you.")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not find the app you are looking for.")
                        
# Close Shareit
                elif 'close share it' in query or 'quit share it' in query:
                    try:
                        speak("Closing Share it.")
                        os.system("taskkill /f /im SHAREit.exe")
                        count = 0
                    except Exception:
                        printSpeak("\nNo such Application is running.")

# Open WinRAR
                elif 'open winrar' in query or 'winrar' in query or 'compress something' in query:
                    try:
                        path = PROGRAMFILES_PATH + "WinRAR\\WinRAR.exe"
                        os.startfile(path)
                        speak("I opened WinRAR for you.")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not find the app you are looking for.")

# Close WinRaR
                elif 'close winrar' in query or 'quit winrar' in query:
                    try:
                        speak("Closing WinRaR.")
                        os.system("taskkill /f /im WinRAR.exe")
                        count = 0
                    except Exception:
                        printSpeak("\nNo such Application is running.")

# Search From Wikipedia
                elif 'wikipedia' in query:
                    try:
                        printSpeak("\nSearching Wikipedia...")
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        printSpeak("\nAccording to wikipedia:")
                        printSpeak(results)
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, No results found")

# Open Youtube
                elif 'open youtube' in query or 'search youtube' in query:
                    try:
                        webbrowser.get('chrome').open('www.youtube.com')
                        speak("Youtube opened for you in google chrome")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not open that link.")

# Close Youtube
                elif 'close youtube' in query or 'quit youtube' in query:
                    try:
                        speak("Closing YouTube.")
                        os.system("taskkill /f /im chrome.exe")
                        count = 0
                    except Exception:
                        printSpeak("\nNo such Application is running.")

# Open Facebook
                elif 'open facebook' in query or 'open fb' in query or 'check my facebook' in query or 'check my fb' in query:
                    try:
                        webbrowser.get('chrome').open('www.facebook.com')
                        speak("Facebook opened for you in google chrome")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not open that link.")

# Close Facebook
                elif 'close facebook' in query or 'quit facebook' in query:
                    try:
                        speak("Closing FaceBook.")
                        os.system("taskkill /f /im chrome.exe")
                        count = 0
                    except Exception:
                        printSpeak("\nNo such Application is running.")

# Open Instagram
                elif 'open instagram' in query or 'open insta' in query or 'check my instagram' in query:
                    try:
                        webbrowser.get('chrome').open('www.instagram.com')
                        speak("Instagram opened for you in google chrome")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not open that link.")

# Close Instagram
                elif 'close instagram' in query or 'quit instagram' in query:
                    try:
                        speak("Closing Instagram.")
                        os.system("taskkill /f /im chrome.exe")
                        count = 0
                    except Exception:
                        printSpeak("\nNo such Application is running.")
                
# Open Twitter
                elif 'open twitter' in query or 'check my twitter' in query:
                    try:
                        webbrowser.get('chrome').open('www.twitter.com')
                        speak("Twitter opened for you in google chrome")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not open that link.")

# Close Twitter
                elif 'close twitter' in query or 'quit twitter' in query:
                    try:
                        speak("Closing Twitter.")
                        os.system("taskkill /f /im chrome.exe")
                        count = 0
                    except Exception:
                        printSpeak("\nNo such Application is running.")

# Twitter Bot
                elif 'tweet for me' in query or 'open twitter bot' in query:
                    try:
                        system('cls')
                        printSpeak("\nLaunching Twitter Bot...")
                        time.sleep(1)
                        print('\nBot Initialized.')
                        system('cls')

                        username, password = getTwitterAccountInfo()

                        print("\nEnter the text you want to tweet: ", end = '')
                        speak("\nEnter the text you want to tweet: ")
                        tweet = input()

                        option = Options()
                        option.add_argument("start-maximized")
                        driver = webdriver.Chrome(CURRENT_DIR + "driver\\chromedriver.exe")
                        driver.get("https://twitter.com/login")

                        username_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
                        password_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
                        loginButton_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span'

                        time.sleep(5)
                        driver.find_element_by_xpath(username_xpath).send_keys(username)
                        driver.find_element_by_xpath(password_xpath).send_keys(password)
                        driver.find_element_by_xpath(loginButton_xpath).click()

                        messageBox_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
                        tweetButton_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span'

                        time.sleep(10)
                        driver.find_element_by_xpath(messageBox_xpath).click
                        driver.find_element_by_xpath(messageBox_xpath).send_keys(tweet)
                        driver.find_element_by_xpath(tweetButton_xpath).click()
                        count = 0
                    except Exception:
                        printSpeak("\nSorry I couold not tweet for you.")

# Open Stack Overflow
                elif 'open stack overflow' in query or 'check stack overflow' in query:
                    try:
                        webbrowser.get('chrome').open('www.stackoverflow.com')
                        speak("Stack Overflow opened for you in google chrome")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not open that link.")

# Close Stack Overflow
                elif 'close stack overflow' in query or 'quit stack overflow' in query:
                    try:
                        speak("Closing Stack Overflow.")
                        os.system("taskkill /f /im chrome.exe")
                        count = 0
                    except Exception:
                        printSpeak("\nNo such Application is running.")

# Open Whatsapp
                elif 'open whatsapp' in query or 'check my whatsapp' in query:
                    try:
                        webbrowser.get('chrome').open('web.whatsapp.com')
                        speak("Whatsapp opened for you in google chrome")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not open that link.")

# Close Whatsapp
                elif 'close whatsapp' in query or 'quit whatsapp' in query:
                    try:
                        speak("Closing Whatsapp.")
                        os.system("taskkill /f /im chrome.exe")
                        count = 0
                    except Exception:
                        printSpeak("\nNo such Application is running.")

# Search Something on Google
                elif 'search on google' in query or 'search on internet' in query or 'search something' in query or "search google" in query:
                    try:
                        printSpeak("\nWhat You want to search on internet?")
                        command = str(takeCommand())
                        command.lower()
                        url = "www.google.com/search?q={}".format(command)
                        webbrowser.get('chrome').open(url) 
                        speak("I searched that on google and found these results.")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not open that link.")

# Close Google Chrome
                elif 'close google chrome' in query or 'quit google chrome' in query or 'close chrome' in query or 'quit chrome' in query or 'close browser' in query or 'quit browser' in query or 'close google' in query or 'quit google' in query:
                    try:
                        speak("Closing Google Search.")
                        os.system("taskkill /f /im chrome.exe")
                        count = 0
                    except Exception:
                        printSpeak("\nNo such Application is running.")

# Play Music
                elif 'play music' in query or 'play songs' in query:
                    try:
                        musicDir = "C:\\Users\\" + CURRENT_USER + "\\Music"
                        songs = os.listdir(musicDir)
                        i = random.randint(0, len(songs))
                        os.startfile(os.path.join(musicDir, songs[i]))
                        printSpeak(f"\nMedia: {songs[i]} is playing now.")
                        count = 0
                    except Exception:
                        printSpeak(f"\nNo Media found in Music Folder")

# Stop Music
                elif 'stop music' in query or 'stop the song' in query or 'stop the music' in query:
                    count = 0
                    name = 'Music.UI.exe'
                    f = wmi.WMI()
                    printSpeak("\nStopping Media...")
                    try:
                        for process in f.Win32_Process():
                            if process.name == name:
                                process.Terminate()
                                printSpeak("\nMedia Stopped Successfully.")
                            count+=1
                    except Exception:
                            printSpeak("\nSorry, No media player is running right now")
                    finally:
                        count = 0

# Tell a Joke
                elif 'tell me a joke' in query or 'i want to laugh' in query or 'i am sad':
                    try:
                        joke = pyjokes.get_joke()
                        speak("Here is a joke for you")
                        printSpeak("\n"+joke)
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, no jokes to tell right now.")

# Check Instagram Profile and Profile Picture Downloader
                elif 'check instagram profile' in query or 'check instagram account' in query or 'open instagram profile' in query or 'open instagram account' in query:
                    try:
                        print("\nPlease Enter the username of instagram profile you want to check: ",end = '')
                        speak("\nPlease Enter the username of instagram profile you want to check: ")
                        username = input()
                        url = 'www.instagam.com/' + username
                        webbrowser.get('chrome').open(url)
                        speak("Instagram Profile opened for you.")
                    except Exception:
                        printSpeak("\nSorry I could not open profile for you...")
                    time.sleep(3)
                    printSpeak("\nDo you want to download the profile picture of this account?")
                    try:
                        query = takeCommand()
                        query = str(query).lower()
                        if 'yes' in query:
                            mod = instaloader.Instaloader()
                            mod.download_profile(username, profile_pic_only=True)
                            printSpeak("\nProfile Picture Downloaded Successfully.")
                        else:
                            pass
                    except Exception:
                        printSpeak("\nSorry I could not download the profile picture of this account.")
                    finally:
                        count = 0

# Check Internet Speed
                elif  'internet speed' in query:
                    try:
                        printSpeak("\nGetting Speed Test Results for you...")
                        st = speedtest.Speedtest()
                        download = st.download()
                        download = round(download/1048576, 1)
                        upload = st.upload()
                        upload = round(upload/1048576, 1)
                        printSpeak("\nSpeed Test Results:")
                        printSpeak(f"Download: {download} MBPS")
                        printSpeak(f"Upload: {upload} MPBS")
                        count = 0
                    except Exception as e:
                        print(e)
                        printSpeak("\nSorry I could not fetch speedtest details of your internet.")

# Volume Up, Volume Down and Mute
                elif 'volume up' in query:
                    pyautogui.press('volumeup')
                    pyautogui.press('volumeup')
                    pyautogui.press('volumeup')
                    pyautogui.press('volumeup')
                    pyautogui.press('volumeup')
                    count = 0
                elif 'volume down' in query:
                    pyautogui.press('volumedown')
                    pyautogui.press('volumedown')
                    pyautogui.press('volumedown')
                    pyautogui.press('volumedown')
                    pyautogui.press('volumedown')
                    count = 0
                elif 'mute' in query or 'unmute' in query:
                    pyautogui.press('volumemute')
                    count = 0
                        

# Tell Time
                elif 'what is the time' in query or 'tell me time' in query or "what's the time" in query or 'tell me the time' in query:
                    try:
                        timeNow = datetime.datetime.now().strftime("%I:%M %p")
                        printSpeak(f"The time is {timeNow}")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not tell the time.")

# Send Whatsapp Message
                elif 'send whatsapp' in query or 'send messaage' in query or 'send a whatsapp' in query or 'send a message' in query:
                    try:
                        numDict = {'FIRST_PERSON':'PHONE_NO', 'SECOND_PERSON':'PHONE_NO', 'THIRD_PERSON':'PHONE_NO'} # ADD AS MANY PERSONS AS YOU LIKE
                        printSpeak("\nWho is the person you want to send a message to?")
                        person = takeCommand()
                        person.lower()
                        if person in numDict.keys():
                            phoneNo = numDict.get(person)
                            printSpeak("\nWhat is the message for this person?")
                            message = takeCommand()
                            hr = int(datetime.datetime.now().strftime("%H"))
                            min = int(datetime.datetime.now().strftime("%M"))
                            min+=1
                            kit.sendwhatmsg(phoneNo, message,hr,min)
                        else:
                            printSpeak("\nMessage sending failed due to an error.")
                        count = 0
                    except Exception:
                        printSpeak("\nMessage sending failed due to an error.")

# Close Whatsapp
                elif 'close whatsapp' in query or 'quit whatsapp' in query:
                    try:
                        speak("Closing Whatsapp.")
                        os.system("taskkill /f /im chrome.exe")
                        count = 0
                    except Exception:
                        printSpeak("\nNo such Application is running.")

# Play a song video on YouTube
                elif 'play song on youtube' in query or 'play youtube' in query or 'play video on youtube' in query:
                    try:
                        printSpeak("\nWhich song you want to play on YouTube?")
                        video = takeCommand()
                        kit.playonyt(video)
                        speak(f"Playing {video} on YouTube")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not play the requested video")

# Close Youtube
                elif 'close youtube' in query or 'quit youtube' in query:
                    try:
                        speak("Closing YouTube.")
                        os.system("taskkill /f /im chrome.exe")
                        count = 0
                    except Exception:
                        printSpeak("\nNo such Application is running.")
            
# Send Email
                elif 'send an email' in query or 'send email' in query:
                    printSpeak("\nDo you want to attach a file with you email?")
                    query = takeCommand()
                    query = str(query).lower()
                    GMAIL_ID = # ADD YOUR GMAIL ID HERE
                    GMAIL_PASS = # ADD YOUR GMAIL PASSWORD HERE
                    if 'yes' in query:
                        try:
                            print("\nPlease Enter the email address of who you want to send: ", end = '')
                            speak("\nPlease Enter the email address of who you want to send: ")
                            to = input() 
                            printSpeak("\nWhat's the subject of your email?")
                            sub = takeCommand()
                            printSpeak("\nWhat's the message you want to send?")
                            message = takeCommand()
                            printSpeak("\nMake sure that you have zipped and placed the attachment file in the 'attachments' folder as 'attachment.zip'.")
                            file_location = CURRENT_DIR + "attachments\\attachment.zip"

                            printSpeak("\nPlease wait while I send the email...")

                            # Formatting Email
                            msg = MIMEMultipart()
                            msg['From'] = GMAIL_ID
                            msg["To"] = to
                            msg["Subject"] = sub
                            msg.attach(MIMEText(message, 'plain'))

                            # Formatting File (Encoding)
                            fileName = os.path.basename(file_location)
                            attachment = open(file_location, 'rb')
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload(attachment.read())
                            encoders.encode_base64(part)
                            part.add_header('Content-Disposition', 'attachment; filename = %s' %fileName)

                            # Add the attachment to the Email
                            msg.attach(part)

                            # Email Sending form Server
                            s = smtplib.SMTP('smtp.gmail.com', 587)
                            s.starttls()
                            s.login(GMAIL_ID, GMAIL_PASS)
                            msg = msg.as_string()
                            s.sendmail(GMAIL_ID, to, msg)
                            s.quit()
                            printSpeak("\nEmail has been sent successfully.")
                        except Exception:
                            printSpeak("\nSorry, Email was not sent.")      

                    else:
                        try:
                            printSpeak("\nWhat's the subject of your email?")
                            sub = takeCommand()
                            printSpeak("\nWhat's the message you want to send?")
                            msg = takeCommand()
                            printSpeak("\nPlease Enter the email address of who you want to send: ")
                            to = input()
                            s = smtplib.SMTP('smtp.gmail.com', 587)
                            s.starttls()
                            s.login(GMAIL_ID, GMAIL_PASS)
                            s.sendmail(GMAIL_ID, to, msg)
                            s.quit()
                            printSpeak("\nEmail has been sent successfully.")
                        except Exception:
                            printSpeak("\nSorry, Email was not sent.")
                    count = 0

# Calculations
                elif 'do some calculations' in query or 'calculate' in query:
                    try:
                        def get_operator_fn(op):
                            return{
                                '+' : operator.add,
                                '-' : operator.sub,
                                'x' : operator.mul,
                                '/' : operator.__truediv__,
                            }[op]
                
                        def eval_binary_expression(op1, op, op2):
                            op1, op2 = int(op1), int(op2)
                            return get_operator_fn(op)(op1, op2)

                        printSpeak("\nWhat you want me to calculate?")
                        print("Example: 3 plus 3 || 3 divided by 3 || 3 multiplied by 3 || 3 minus 3")
                        query = takeCommand()
                        result = eval_binary_expression(*(query.split()))
                        printSpeak(f"Your Result is: {result}")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry I could not complete the desired calculations.")

# I Love You
                elif 'i love you' in query or 'do you love me' in query:
                    try:
                        printSpeak("\nI Love You Too but only as a friend")
                        count = 0
                    except Exception:
                        printSpeak("Sorry, I dont have any answer for this right now.")

# Sleep (Force)
                elif 'go to sleep' in query or 'shut up' in query or 'sleep candy' in query:
                    try:
                        printSpeak("\nOk I am going for a short nap. Call me when you need me. Have a good time")
                        cycle = False
                        count = 0
                    except Exception:
                        printSpeak("\nI cannot go to sleep. I justs woke up.")

# What is your Name?
                elif 'what is your name' in query or 'tell me your name' in query or "what's your name" in query:
                    try:
                        printSpeak("\nMy Name is Candy. What is your name?")
                        askForMore = False
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I dont have any answer to this right now.")

# My Name
                elif 'my name is' in query or 'myself' in query:
                    try:
                        printSpeak("\nThat's a very cute name")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I dont have any answer to this right now.")

# Respond to Hello
                elif 'hello' in query or 'hi' in query:
                    try:
                        printSpeak("\nHello my friend...!")
                        askForMore = False
                        count = 0
                    except Exception:
                        printSpeak("\nSorry I have no answer for that right now.")

# Respond to How are you
                elif 'how are you' in query or 'what about you' in query:
                    try:
                        printSpeak("\nI am good as new. What about you?")
                        askForMore = False
                        count = 0
                    except Exception:
                        printSpeak("\nSorry I have no answer for this right now.")

# Respond to I am Fine
                elif 'i am fine' in query or 'i am great' in query or 'i am good' in query:
                    try:
                        printSpeak("\nGlad to hear that.")
                        printSpeak("Can we talk about some work now?")
                        askForMore = False
                        count = 0
                    except:
                        printSpeak("\nSorry I have no answer for this right now.")

# Tell me IP Adress
                elif 'my ip address' in query:
                    try:
                        ip = get('https://api.ipify.org').text
                        printSpeak(f"\nYour IP Address is: {ip}")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry I could not fetch your IP Address.")

# Check Weather
                elif 'what is the weather' in query or 'check weather' in query or 'tell me the weather' in query or 'is it raining outside' in query or 'how is the weather' in query:
                    BaseURL = 'https://api.openweathermap.org/data/2.5/weather?q='
                    API_KEY = '66919647fbb645654e0b8ee9a13cf9e8'

                    ipAddress = requests.get('https://api.ipify.org').text
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAddress + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = str(geo_data['city'])

                    url = BaseURL + city + '&appid=' + API_KEY
                    response = requests.get(url)
                    count = 0
                    try:
                        if response.status_code == 200:
                            data = response.json()
                            main = data['main']
                            main['temp'] = main['temp']-273.15
                            temperature = round(float(main['temp']))
                            humidity = main['humidity']
                            pressure = main['pressure']
                            report = data['weather']
                            weather = report[0]['description']
                            weather = str(weather).capitalize()
                            printSpeak(f"\nHere is a weather report of {city} for today:\n")
                            print(f"{city:-^30}")
                            printSpeak(f"Temperature: {temperature} Celcius")
                            printSpeak(f"Humidity: {humidity} %")
                            printSpeak(f"Wind Pressure: {pressure} metre per second")
                            printSpeak(f"Weather: {weather}")
                    except Exception as e:
                        print(e)
                        printSpeak("\nSorry I could not find weather details for your area.")

# My Location
                elif 'where we are' in query or 'where am i' in query or 'my location' in query:
                    printSpeak("\nGetting your location... Please wait...")
                    try:
                        ipAddress = requests.get('https://api.ipify.org').text
                        url = 'https://get.geojs.io/v1/ip/geo/' + ipAddress + '.json'
                        geo_requests = requests.get(url)
                        geo_data = geo_requests.json()

                        city = geo_data['city']
                        state = geo_data['region']
                        country = geo_data['country']

                        printSpeak(f"\nWe are located in city: {city}, State: {state} and country: {country}")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not find your location.")

# Take Screenshot
                elif 'screenshot' in query or 'take a picture of this' in query:
                    try:
                        pyautogui.keyDown('winleft')
                        pyautogui.keyDown('printscreen')
                        time.sleep(0.5)
                        pyautogui.keyUp('winleft')
                        pyautogui.keyUp('printscreen')
                        printSpeak("\nScreenshot Captured and saved to 'Screenshots' Folder.")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not capture a screenshot for you.")

# Shutdown System
                elif 'shut down my pc' in query or 'shut down the system' in query:
                    try:
                        printSpeak("\nAre You Sure Want To Turn Off Your PC?")
                        confirmation = takeCommand()
                        if confirmation == 'yes':
                            printSpeak("\nOK, Shutting down your PC in 5 seconds.")
                            os.system("shutdown /s /t 5")
                            try:
                                sys.exit()
                            except Exception:
                                os._exit(0)
                        elif confirmation == 'no':
                            printSpeak("\nOk. I will not shut down your PC. Don't Worry.")
                        else:
                            printSpeak("\nNevermind")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not Shut Down your PC.")

# Restart System
                elif 'restart my pc' in query or 'restart the system' in query:
                    try:
                        printSpeak("\nAre You Sure Want To Restart Your PC?")
                        confirmation = takeCommand()
                        if confirmation == 'yes':
                            printSpeak("\nOK, Restarting your PC in 5 seconds.")
                            os.system("shutdown /r /t 5")
                            try:
                                sys.exit()
                            except Exception:
                                os._exit(0)
                        elif confirmation == 'no':
                            printSpeak("\nOk. I will not restart your PC. Don't Worry.")
                        else:
                            printSpeak("\nNevermind")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not Restart your PC.")

# Sleep System
                elif 'sleep my pc' in query or 'sleep the system' in query:
                    try:
                        printSpeak("\nAre You Sure Want To Sleep Your PC?")
                        confirmation = takeCommand()
                        if confirmation == 'yes':
                            printSpeak("\nOK, Making your PC to go to Sleep.")
                            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                            try:
                                sys.exit()
                            except Exception:
                                os._exit(0)
                        elif confirmation == 'no':
                            printSpeak("\nOk. I will not make your PC Sleep. Don't Worry.")
                        else:
                            printSpeak("\nNevermind")
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I could not make your PC go to Sleep.")

# Check battery Percentage
                elif 'check my battery' in query or 'check battery' in query or 'battery percentage'in query:
                    try:
                        battery = psutil.sensors_battery()
                        percent =  str(battery.percent)
                        percentStr = f"\nThe battery percentage of your system is: {percent}%"
                        printSpeak(percentStr)
                        plugged = battery.power_plugged
                        plugged = "Plugged in" if plugged else "Not Plugged in"
                        pluggedStr = f"Current State: {plugged}"
                        printSpeak(pluggedStr)    
                        count = 0
                    except Exception as e:
                        print(e)
                        printSpeak("\nSorry I could not check for your battery.")          

# No Thanks
                elif 'no thanks' in query or 'no candy' in query or 'no thank you' in query or 'no' in query:
                    try:
                        printSpeak("\nOk I am going for a short nap. Call me when you need me. Have a good time.")
                        cycle = False
                        askForMore = False
                        count = 0
                    except Exception:
                        printSpeak("\nBut I just woke up. I cannot go back to nap. Kindly tell me some task.")

# Switch Windows
                elif 'switch windows' in query or 'press alt tab' in query:
                    try:
                        pyautogui.keyDown('alt')
                        pyautogui.keyDown('tab')
                        time.sleep(0.5)
                        pyautogui.keyUp('tab')
                        pyautogui.keyUp('alt')
                        count = 0
                    except Exception:
                        printSpeak("\nSorry, I cold not switch windows for you.")

# Tell me the news
                elif 'tell me the news' in query or "what is happeneing outside" in query:
                    printSpeak("\nPlease wait while I fetch some news for you.")
                    try:
                        news()
                        count = 0
                    except Exception as f:
                        print(f)
                        printSpeak("\nSorry, I could not fetch news for you.")

# Add Alarm
                elif 'add an alarm' in query or 'set an alarm' in query or 'set alarm' in query or 'add alarm' in query:
                    try:
                        printSpeak("\nTell me the hour to set for alarm: ")
                        alarm_hour =    int(takeCommand())
                        printSpeak("\nTell me the minute to set for alarm: ")
                        alarm_min = int(takeCommand())
                        addAlarm(alarm_hour, alarm_min)
                        count = 0
                    except Exception:
                        printSpeak("\nInvalid Time Entered")
                
            if askForMore == True and cycle == True:
                printSpeak("\nSir, is there anything else I can do for you?")
                count += 1
                
            
            if count == 5:
                printSpeak("\nGoing to sleep mode. Wake me up when you need me.")
                cycle = False



    if __name__ == "__main__":
        def WakeUp():
            permission = ''
            system('cls')
            print("Candy Virtual Assistant: Activated")
            print("Current State: Idle")
            print("\nWaiting for Wakeup Command...")
            while True:
                permission = takePermission()
                if 'wakeup candy' in permission or 'wake up candy' in permission or 'hello candy' in permission or 'hi candy' in permission or 'wake up' in permission or 'wakeup' in permission:
                    tasks()
                    WakeUp()
                elif 'good bye candy' in permission or 'goodbye candy' in permission  or 'bye candy' in permission or 'exit candy' in permission or 'exit' in permission or 'terminate' in permission:
                    printSpeak("\nGoodbye sir. Have a good time.")
                    sys.exit()
        WakeUp()


else:
    print("\nNo Internet Connection Found. Please Connect To The internet then wake me up.\n")