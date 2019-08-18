import random

word_list = ["python", "java", "kotlin", "javascript"]
eng_lowercase = list("abcdefghijklmnopqrstuvwxyz")
random_word = list(random.choice(word_list))
crutch = list()
crutch.append("play")
crutch.append("exit")


print("H A N G M A N")
play_or_exit = ""
while play_or_exit not in crutch:
    play_or_exit = str(input('Type "play" to play the game, "exit" to quit: '))
while play_or_exit == "play":
    print()

    current_word_status = list("-" * len(random_word))
    guessed_word = list("-" * len(random_word))
    typed_letters = list()

    count_of_life = 8

    while count_of_life > 0:
        print("".join(current_word_status))
        answer = str(input("Input a letter: "))
        if len(answer) != 1:
            print("You should print a single letter")
            print()
            continue
        elif answer not in eng_lowercase:
            print("It is not an ASCII lowercase letter")
            print()
            continue
        elif answer in typed_letters:
            print("You already typed this letter")
            print()
            continue
        else:
            typed_letters.append(answer)
        if answer in random_word:
            for j in range(len(random_word)):
                if answer == random_word[j]:
                    current_word_status[j] = random_word[j]
                    random_word[j] = "-"
            if random_word == guessed_word:
                print("You guessed the word " + "".join(current_word_status) + "!")
                print("You survived!")
                break
            else:
                print()
                continue
        else:
            print("No such letter in the word")
            count_of_life -= 1
            if count_of_life != 0:
                print()
    else:
        print("You are hanged!")
    print()
    play_or_exit = str(input('Type "play" to play the game, "exit" to quit: '))