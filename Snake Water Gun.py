result = 0
for i in range(1,11):
    print("Enter Your Choice----Snake,Water or Gun")
    your_choice = input()
    import random
    lis = ["Snake", "Water", "Gun"]
    ran_choice = random.choice(lis)

    if __name__ == "__main__":
        print(f"Chances left are {10-i}")
        if ran_choice == your_choice:
            print(f"Opposite Choice is {ran_choice} \n Match Draw....")
        elif ran_choice == "Snake" and your_choice == "Water":
            print(f"Opposite Choice is {ran_choice} \n You lost..")
            result -= 1
        elif ran_choice == "Snake" and your_choice == "Gun":
            print(f"Opposite Choice is {ran_choice} \n You are Winner..")
            result += 1
        elif ran_choice == "Water" and your_choice == "Gun":
            print(f"Opposite Choice is {ran_choice} \n You lost..")
            result -= 1
        elif ran_choice == "Water" and your_choice == "Snake":
            print(f"Opposite Choice is {ran_choice} \n You are Winner..")
            result += 1
        elif ran_choice == "Gun" and your_choice == "Snake":
            print(f"Opposite Choice is {ran_choice} \n You lost..")
            result -= 1
        elif ran_choice == "Gun" and your_choice == "Water":
            print(f"Opposite Choice is {ran_choice} \n You are Winner..")
            result += 1
        if i== 10:
            print(result)