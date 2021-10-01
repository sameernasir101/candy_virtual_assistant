-----------------------------------------------------------------------------------------------------------------
                                                          CANDY VIRTUAL ASSISTANT
                                                     AUTHOR: SYED MUHAMMAD SAMEER NASIR
-----------------------------------------------------------------------------------------------------------------

This is Candy, a basic virtual assistant for your PC made by Syed Muhammad Sameer Nasir. This program is made in Python.
This program is best compatible with Windows as of now. Other platforms complete support will be added soon.

-----------------------------------------------------------------------------------------------------------------
A complete list of Commands/Functionalities:

0. Check Internet Connectivity
1. Text To Speech
2. Greet
3. Send email to myself
4. Add an Alarm
5. Open Notepad
6. Close Notepad
7. Open CMD
8. Close CMD
9. Open Google Chrome
10. Close Google Chrome
11. Open Visual Studio Code
12. Close Visual Studio Code
13. Open SHAREit
14. Close SHAREit
15. Open WinRAR
16. Close WinRAR
17. Fetch info from Wikipedia
18. Open YouTube
19. Close YouTube
20. Open Facebook
21. Close Facebook
22. Open Instagram
23. Close Instagram
24. Open Twitter
25. Close Twitter
26. Open Stack Overflow
27. Close Stack Overflow
28. Open Whatsapp
29. Close Whatsapp
30. Google Search for Something
31. Play Some Music
32. Stop Music
33. Tell Time
34. Send Whatsapp Message to someone
35. Play a YouTube Video
36. Respond to "I Love You"
37. Respond to "What is your Name?"
38. Respond to "My Name is ______"
39. Tell me my IP Address
40. Respond to No Thanks
41. Respond to an Invalid Task
42. Shutdown System
43. Restart System
44. Sleep System
45. Tell a Joke
46. Switch Windows
47. Tell me some News 
48. Send an email with attachment
49. Check instagram Profile or download it's profile picture.
50. Check My Location.
51. Check Weather.
52. Take a Screenshot.
53. Read PDF.
54. Peform Calculations.
55. Respond to thanks.
56. Respond to hello.
57. Respond to how are you
58: WakeUp Command
59. Check battery percentage and state
60. Check Internet Speed
61. Voume Up, Volume Down, Mute
62. Go To Sleep

    More will be added soon.

-----------------------------------------------------------------------------------------------------------------
Important Notes:

Python Modules installed in my PC are given in "requirements.txt" file. 
1. You can install all those by using pip in your terminal by using following command: (without arrow)
      -> pip install -r requirements.txt
  
Note: Open terminal in the root folder

2. Go to "Voice Module" folder and add the "CortanaVoice.reg" to your registry by double clicking it and hot ok.

3. Download and install Chrome Browser in your PC as this program requires it to perform many it's functions.

4. User must be connected to internet to run this program.

-----------------------------------------------------------------------------------------------------------------
For sending emails using Candy:

    Add your GMAIL_ID and GMAIL_PASSWORD in line 658 and line 659 of "Candy.py" respectively in order to send email from your account automatically.
    
For attaching files with email:
    
    Make a zip file containing all the attachments you want to send and rename it as "attachment.zip". Then place this zip file in "attachments" folder before sending email.

For making Tweets using Twitter Bot from Candy:
    
    Add your Twitter account (username and password) in "account.txt" file under account directory in order to auto tweet using your Twitter Account

For sending WhatsApp messages:
    
    Add details of the persons who you want to send a whatsapp message through voice in following way in line 606 in "Candy.py":
          -> Change "FIRST_PERSON" : "PHONE_NO" to something like:   "sameer" : "+001234567890" (use country code without dashes)
          -> Add as much contacts as you like.
          
-----------------------------------------------------------------------------------------------------------------

Following Modules were imported and used in this project:

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
    from os import system
    import pywhatkit as kit
    from requests import get
    from email import encoders
    from selenium import webdriver
    import speech_recognition as sr
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from instadownloader import instaloader
    from email.mime.multipart import MIMEMultipart 
    from selenium.webdriver.chrome.options import Options 
