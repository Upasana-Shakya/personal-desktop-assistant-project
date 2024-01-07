import pyttsx3     # Converts text to speech
import speech_recognition as sr    # for voice recognition
import datetime        # For date & time
import wikipedia       # For asking ques to wikipedia
import webbrowser      # To open websites
import os
import socket       # To check connection
import re           # regular expression module


engine = pyttsx3.init('sapi5')  #sapi5 is used to take voice
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak("Good Morning Ma'am!")
        print("Good Morning Ma'am!")

    elif hour >= 12 and hour < 18 :
        speak("Good Afternoon Ma'am!")
        print("Good Afternoon Ma'am!")

    else:
        speak("Good Evening Ma'am!")
        print("Good Evening Ma'am!")
    
    speak("I am your virtual assistant, JARVIS. Please tell me how may I help you")
    print("I am your virtual assistant, JARVIS. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said : {query}\n")

    except Exception as e :
        # print(e)   # write when you want to see errors in console
        print("Say that again please...")
        return "None"
    return query

def check_internet_connection():
    try:
        # Try to connect to a well-known server (in this case, Google's public DNS server)
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True  # If connection is successful, return True
    except OSError:
        pass

    return False  # If connection is not successful, return False

def ans_ques(query):

    if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        
    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open lead code' in query:
        webbrowser.open("leetcode.com")

    elif 'open gfg' in query:
        webbrowser.open("geekforgeeks.org")

    elif 'open gl bajaj' in query:
        webbrowser.open("glbitm.org")

    elif 'how are you' in query:
        speak("I'am fine. Thank you for asking, and what about you.")
        
    elif 'I am also fine' in query:
        speak("That's great to hear! Have a great day! ")

    elif 'play music' in query:
        music_dir = 'C:\\Users\\UPASANA\\Music\\My Music'
        songs = os.listdir(music_dir)
        # print (songs)
        os.startfile(os.path.join(music_dir , songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Ma'am, the time is {strTime}")

    elif 'the date' in query :
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        print(current_date)
        speak(f"Today's date is {current_date}")
                
    elif 'open code' in query:
        codePath = '"C:\\Users\\UPASANA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
        os.startfile(codePath)

    # Check for Addition
    elif 'calculate' in query:
        # Use regular expression to extract addition
        match = re.search(r'calculate (.+)', query)
        if match:
            expression = match.group(1)
            try:
                result = eval(expression)  # Use eval to evaluate the expression
                speak(f"The result of {expression} is {result}")
                print('The result is : ' , result)
            except Exception as e:
                speak("Sorry, I couldn't calculate that.")
                print(e)

    elif 'quit' in query:
        speak("Thank you for giving your precious time !! ")
        exit()

    else:
        speak("I'm sorry, I don't have information on that topic.")
        exit()
        

if __name__ == "__main__":

    wishMe()
    
    if check_internet_connection():
        print("Connected to the internet.")
    else:
        print("Not connected to the internet. Please check your internet connection.")

    while True:
        query = takeCommand().lower()
        ans_ques(query)