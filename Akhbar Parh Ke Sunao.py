import requests
import json
from win32com.client import Dispatch
def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)
if __name__ == '__main__':
    new = requests.get(url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=f72f4aaa879a4935b63f9e7c927e5b25")
    news = new.json()
    allArticles = news['articles']
    result = []
    result2 = []
    for arr in allArticles:
        result.append(arr["title"])
        result2.append(arr["description"])
    try:
        n = int(input("You want to listen only headlines or full news.\nPress 1 for Headlines.\nPress 2 for Full News\n"))
    except Exception as e:
        print(f"{e},Try again.....")
    else:
        if n == 1:
            for i in range(1, 11):
                print(f"{i}.", result[i])
                speak(result[i])
                if i == 9:
                    speak("Here goes our last news.")
                elif i == 10:
                    break
                else:
                    speak("Our next news is:")
        elif n==2:
            for i in range(1, 11):
                print(f"{i}.", result[i])
                speak(result[i])
                print(f"{i}.", result2[i])
                speak(result2[i])
                if i == 9:
                    speak("Here goes our last news.")
                elif i == 10:
                    break
                else:
                    speak("Our next news is:")