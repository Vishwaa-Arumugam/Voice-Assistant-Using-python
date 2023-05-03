import datetime
from Jarvis import speak


def wish(self):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    print("Hello sir, Please tell me how may I help you")
    speak("Hello sir, Please tell me how may I help you")