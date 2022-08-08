from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if stopper == input_of_user:
            mixer.music.stop()
            break
def log_now(msg):
    with open("log.txt","a") as f:
        f.write(f"{msg} at {datetime.now()} \n")

if __name__ == "__main__":
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40 * 60
    exercisesecs = 30 * 60
    eyessecs = 45 * 60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking Time. Type \"drank\" to stop... ")
            musiconloop("water.mp3","drank")
            log_now("drank")
        if time() - init_eyes > eyessecs:
            print("Eyes exercie time.Type done to stop....")
            musiconloop("Eyes.mp3","done")
            log_now("Eyes Exercise")
        if time() - init_exercise > exercisesecs:
            print("Physical Exercise Time. Type done to stop...")
            musiconloop("exercise.mp3","done")
            log_now("Physical Exercise done")
