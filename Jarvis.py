# JARVIS

import datetime
import os
import sys
import time
import webbrowser
import pyautogui
import pyttsx3
import pywhatkit
import pywhatkit as kit
import speech_recognition as sr
import wikipedia
from time import sleep
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from jarvisGUI import Ui_Form
from wish import wish
from pizza import pizza
from amazon import amazon

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 185)

# text to speech

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def takeCommand(self):
        # It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=4, phrase_time_limit=7)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # speak("Say that again please...")
            return "None"
        query = query.lower()
        return query

    def run(self):
        speak("please say getup to continue")
        while True:
            query = self.takeCommand()
            if "get up" in query:
                self.TaskExecution()

    # to wish

    wish()

    def TaskExecution(self):
        self.wish()
        while True:
            # if 1:
            query = self.takeCommand().lower()

            if 'how are you' in query:
                speak("I am fine sir!")
                speak("How are you Sir")

            elif 'what is your name' in query:
                speak("My name is jarvis sir")

            elif 'fine' in query or "good" in query:
                speak("It's good to know that your fine")

            # search in wikipedia

            elif 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            # To google scrap search

            elif "google search" in query:
                import wikipedia as googleScrap
                query = query.replace("jarvis", "")
                query = query.replace("google search", "")
                query = query.replace("google", "")
                speak("This is what i found on the web")

                try:

                    pywhatkit.search(query)
                    result = googleScrap.summary(query, 2)
                    speak(result)

                except:

                    speak("No speakable data available")

            # To open application

            elif 'open youtube' in query:
                speak("opening youtube")
                webbrowser.open("youtube.com")

            elif 'open command prompt' in query:
                speak("opening command prompt")
                os.system("start cmd")

            elif 'open eclipse' in query:
                speak("opening eclipse ")
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("alt")
                pyautogui.keyDown("q")
                pyautogui.keyUp("alt")
                pyautogui.keyUp("ctrl")

            elif 'tell me the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"Sir, the time is {strTime}")
                speak(f"Sir, the time is {strTime}")

            elif 'change the window' in query:
                speak("changing the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

            # write notes in MS Word and save using voice commands

            elif 'open word' in query:
                speak("opening Microsoft office word 2007")
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("alt")
                pyautogui.press("w")
                pyautogui.keyUp("ctrl")
                pyautogui.keyUp("alt")
                time.sleep(5)

            elif 'dictate' in query:
                speak("turning on dictation")
                pyautogui.keyDown("win")
                pyautogui.press("h")
                pyautogui.keyUp("win")
                time.sleep(5)

            elif 'stop dictating' in query:
                speak("tuning off dictation")
                pyautogui.keyDown("win")
                pyautogui.press('h')
                pyautogui.keyUp('win')

            elif 'save' in query:
                speak("saving file")
                pyautogui.keyDown("ctrl")
                pyautogui.press("s")
                time.sleep(1)
                pyautogui.keyUp('ctrl')
                pyautogui.press("enter")

            # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

            # copy paste commands

            elif 'open new folder' in query:
                speak("opening new folder")
                codePath = "C:\\Users\\Vishwaa Arumugam\\Desktop\\New folder"
                os.startfile(codePath)

            elif 'select all' in query:
                speak("selecting all files")
                pyautogui.keyDown("ctrl")
                pyautogui.press("a")
                pyautogui.keyUp("ctrl")

            elif 'copy' in query:
                speak("copying all files")
                pyautogui.keyDown("ctrl")
                pyautogui.press("c")
                pyautogui.keyUp("ctrl")

            elif 'open example' in query:
                speak("opening example folder")
                codePath = "C:\\Users\\Vishwaa Arumugam\\Desktop\\example"
                os.startfile(codePath)

            elif 'paste' in query:
                pyautogui.keyDown("ctrl")
                pyautogui.press("v")
                speak("file pasted")
                pyautogui.keyUp("ctrl")

            # --------------------------------------------------------------------------------------------------------------------------------------------------------------#

            # chrome automations

            elif 'open google' in query:
                speak("opening google")
                codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(codePath)

            elif 'new tab' in query:
                speak("opening new tab")
                pyautogui.keyDown("ctrl")
                pyautogui.press("t")
                pyautogui.keyUp("ctrl")

            elif 'new window' in query:
                speak("opening new window")
                pyautogui.keyDown("ctrl")
                pyautogui.press("N")
                time.sleep(1)
                pyautogui.keyUp("ctrl")

            elif 'open downloads' in query:
                speak("opening downloads")
                pyautogui.keyDown("ctrl")
                pyautogui.press("j")
                pyautogui.keyUp("ctrl")

            elif 'open history' in query:
                speak("opening history")
                pyautogui.keyDown("ctrl")
                pyautogui.press("h")
                pyautogui.keyUp("ctrl")

            elif 'open bookmarks' in query:
                speak("opening bookmarks")
                pyautogui.keyDown("ctrl")
                pyautogui.press("b")
                pyautogui.keyUp("ctrl")

            elif 'go to first' in query:
                speak("going to first tab")
                pyautogui.keyDown("ctrl")
                pyautogui.press("1")
                pyautogui.keyUp("ctrl")

            elif 'go to second' in query:
                speak("going to second tab")
                pyautogui.keyDown("ctrl")
                pyautogui.press("2")
                pyautogui.keyUp("ctrl")

            elif 'go to third' in query:
                speak("going to third tab")
                pyautogui.keyDown("ctrl")
                pyautogui.press("3")
                pyautogui.keyUp("ctrl")

            elif 'go to fourth' in query:
                speak("going to fourth tab")
                pyautogui.keyDown("ctrl")
                pyautogui.press("4")
                pyautogui.keyUp("ctrl")

            elif 'go to fifth' in query:
                speak("going to fifth tab")
                pyautogui.keyDown("ctrl")
                pyautogui.press("5")
                pyautogui.keyUp("ctrl")

            elif 'go to sixth' in query:
                speak("going to sixth tab")
                pyautogui.keyDown("ctrl")
                pyautogui.press("6")
                pyautogui.keyUp("ctrl")

            elif 'go to seventh' in query:
                speak("going to seventh tab")
                pyautogui.keyDown("ctrl")
                pyautogui.press("7")
                pyautogui.keyUp("ctrl")

            elif 'close tab' in query:
                speak("closing tab")
                pyautogui.keyDown("ctrl")
                pyautogui.press("W")
                pyautogui.keyUp("ctrl")

            # Notepad automation

            elif 'open notepad' in query:
                speak("opening notepad")
                npath = "C:\\Windows\\System32\\notepad.exe"
                os.startfile(npath)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#

            # YT automations

            elif 'play song on youtube' in query:
                speak("Playing The soul of doctor")
                kit.playonyt("soul of doctor")
                sleep(10)

            elif 'stop' in query:
                speak("pausing video")
                pyautogui.press("k")

            elif 'resume' in query:
                speak("resuming video")
                pyautogui.press("k")

            elif 'full mscreen' in query:
                speak("maximizing video")
                pyautogui.press("f")

            elif 'small screen' in query:
                speak("minimizing video")
                pyautogui.press("f")

            elif 'skip forward' in query:
                speak("skipping forward")
                pyautogui.press("l")

            elif 'skip backward' in query:
                speak("skipping backward")
                pyautogui.press("j")

            elif 'increase speed' in query:
                speak("increasing video speed")
                pyautogui.keyDown("shift")
                pyautogui.press(">")
                pyautogui.keyUp("shift")

            elif 'decrease speed' in query:
                speak("decreasing video speed")
                pyautogui.keyDown("shift")
                pyautogui.press("<")
                pyautogui.keyUp("shift")

            elif 'play next video' in query:
                speak("playing next video")
                pyautogui.keyDown("shift")
                pyautogui.press("n")
                pyautogui.keyUp("shift")

            elif 'mute' in query:
                speak("muting sound")
                pyautogui.press("m")

            elif 'unmute' in query:
                speak("unmuting sound")
                pyautogui.press("m")

            # To check the battery percentage

            elif "how much power left" in query:
                import psutil
                battery = psutil.sensors_battery()
                percentage = battery.percent
                print(battery.percent)
                speak(f"sir our system have {percentage} percent battery")

            # control volume

            elif "volume up" in query:
                speak("increasing volume")
                pyautogui.press("volumeup")

            elif "volume down" in query:
                speak("decreasing volume")
                pyautogui.press("volumedown")

            elif "no volume" in query:
                speak("muting sound")
                pyautogui.press("volumemute")

            # To send message

            elif "send a message" in query:
                speak("sir, what should i say")
                msz = self.takeCommand()

                from twilio.rest import Client

                account_sid = ''
                auth_token = ''

                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                    body=msz,
                    from_='',
                    to=''
                )

                print(message.sid)
                speak("sir, message has been sent")

            # To order pizza

            elif "order a pizza" in query:
                speak("ok sir")
                print("ok sir opening dominos")
                self.pizza()

            # To order a mobile phone in amazon

            elif "order a mobile phone" in query:
                speak("ok sir")
                self.amazon()

            # to close

            elif "close notepad" in query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "close chrome" in query:
                speak("closing chrome")
                os.system("taskkill /f /im chrome.exe")

            elif "sleep" in query:
                speak("Ok sir, say get up, if you need me")
                break

    # To order a pizza

    pizza()

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # To order a mobile in amazon

    amazon()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.startPushButton.clicked.connect(self.startTask)
        self.ui.quitPushButton.clicked.connect(self.close)

    def startTask(self):
        # Jarvis GUI
        self.ui.movie = QtGui.QMovie("C:\\Users\\Vishwaa Arumugam\\PycharmProjects\\voice\\GUI\\Jarvis_Gui (1).gif")
        self.ui.jarvisGUI.setMovie(self.ui.movie)
        self.ui.movie.start()
        # dateLabel
        self.ui.movie = QtGui.QMovie("C:\\Users\\Vishwaa Arumugam\\PycharmProjects\\voice\\GUI\\gggf.jpg")
        self.ui.dateLabel.setMovie(self.ui.movie)
        self.ui.movie.start()
        # timeLabel
        self.ui.movie = QtGui.QMovie("C:\\Users\\Vishwaa Arumugam\\PycharmProjects\\voice\\GUI\\gggf.jpg")
        self.ui.timeLabel.setMovie(self.ui.movie)
        self.ui.movie.start()
        # startLabelNotButton
        self.ui.movie = QtGui.QMovie("C:\\Users\\Vishwaa Arumugam\\PycharmProjects\\voice\\GUI\\Start.png")
        self.ui.startLabelNotButton.setMovie(self.ui.movie)
        self.ui.movie.start()
        # quitLabelNotButton
        self.ui.movie = QtGui.QMovie("C:\\Users\\Vishwaa Arumugam\\PycharmProjects\\voice\\GUI\\Quit.png")
        self.ui.quitLabelNotButton.setMovie(self.ui.movie)
        self.ui.movie.start()
        # earthGIF
        self.ui.movie = QtGui.QMovie("C:\\Users\\Vishwaa Arumugam\\PycharmProjects\\voice\\GUI\\Earth.gif")
        self.ui.earthGIF.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        currentTime = QTime.currentTime()
        currentDate = QDate.currentDate()
        labelTime = currentTime.toString('hh:mm:ss')
        labelDate = currentDate.toString(Qt.ISODate)
        self.ui.dateTextBrowser.setText(f"Date: {labelDate}")
        self.ui.timeTextBrowser.setText(f"Time: {labelTime}")


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
