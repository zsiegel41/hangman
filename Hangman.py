# http://tinyurl.com/jhrvs94
import random

def hangman():
    word_list = ["cat",
             "dog",
             "fish",
             "armadillo",
             "leopard",
             "elephant",
             "monkey",
             "dolphin",
             "cow",
             "horse",
             "buffalo",
             "bird",
             "ostrich",
             "zebra",
             "lion",
             "lizard",
             "emu",
             "llama",
             "pig",
             "chicken",
             "turkey",
             "alligator",
             "gorilla",
             "bear",
             "beaver",
             "camel",
             "crab",
             "deer",
             "giraffe",
             "hamster",
             "hedgehog",
             "frog"
             ]
    random_number = random.randint(0, 31)
    word = word_list[random_number]
    wrong = 0
    stages = ["",
              "________         ",
              "|       |        ",
              "|       |        ",
              "|       0        ",
              "|      /|\       ",
              "|      / \       ",
              "|                "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman. The answer is the name of an animal.")
    print(board)
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win! It was {}!".format(word))
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))

hangman()

