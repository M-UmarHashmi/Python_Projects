#Health Management System
def getdate():
    import datetime
    return datetime.datetime.now()

def nameselection(name,thing,purpose):
    if name == 1 :
        if thing == 1 :
            f = open("harry_diet_save.txt","a")
            print("Enter Your diet...\n")
            s = input()
            save = f"[{getdate()}] {s}\n"
            f.write(save)
            f.close()
        elif thing == 2:
            j = open("harry_exercise_save.txt", "a")
            print("Enter Your exercise...\n")
            s = input()
            exercise_save = f"[{getdate()} {s}\n"
            j.write(exercise_save)
            j.close()

    elif name == 2 :
        if thing == 1:
            k = open("rohan_diet_save.txt", "a")
            print("Enter Your diet...\n")
            s = input()
            save = f"[{getdate()}] {s}\n"
            k.write(save)
            k.close()

        elif thing == 2:
            l = open("rohan_exercise_save.txt", "a")
            print("Enter Your exercise...\n")
            s = input()
            save = f"[{getdate()}] {s}\n"
            l.write(save)
            l.close()

    elif name == 3 :
        if thing == 1:
            m = open("Hammad_diet_save.txt", "a")
            print("Enter Your diet...\n")
            s = input()
            save = f"[{getdate()}] {s}\n"
            m.write(save)
            m.close()

        elif thing == 2:
            n = open("rohan_exercise_save.txt", "a")
            print("Enter Your exercise...\n")
            s = input()
            save = f"[{getdate()}] {s}\n"
            n.write(save)
            n.close()
    print("File saved Successfully....")


def purposeselection(name, thing, purpose):
    if name == 1 and thing == 1:
        f = open("harry_diet_save.txt", "r")
        print(f.read())
        f.close()

    elif name == 1 and thing == 2:
        j = open("harry_exercise_save.txt", "r")
        print(j.read())
        j.close()

    elif name == 2 and thing == 1:
        k = open("rohan_diet_save.txt", "r")
        print(k.read())
        k.close()

    elif name == 2 and thing == 2:
        l = open("rohan_exercise_save.txt", "r")
        print(l.read())
        l.close()

    elif name == 3 and thing == 1:
        m = open("Hammad_diet_save.txt", "r")
        print(m.read())
        m.close()

    elif name == 3 and thing == 2:
        n = open("rohan_exercise_save.txt", "r")
        print(n.read())
        n.close()
    print("File retrieved Successfully....")

print("What's Your name?")
print("Enter 1 for Harry\nEnter 2 for Rohan \nEnter 3 for Hammad")
name = int(input("Enter value here\n"))
print("What you want to excess?")
print("Enter 1 for Diet\n Enter 2 for Excercise")
thing= int(input("Enter value here\n"))
print("what do you want to do?\n Enter 1 for save\n Enter 2 for retrieve")
purpose = int(input("Enter value here...\n"))
if purpose == 1:
        nameselection(name,thing,purpose)
elif purpose == 2:
        purposeselection(name,thing, purpose)



