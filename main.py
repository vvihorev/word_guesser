import random


def guess_word(answer):
    attempt = 0
    while attempt < 5:
        result = ""
        guess = input(f'Attempt {attempt + 1}: Your guess: ')
        if len(guess) != 5:
            print('Guesses must be 5 letters only')
            continue
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                result += 'X'
            elif guess[i] in answer:
                result += '^'
            else:
                result += '.'
        print(result)
        if result == "XXXXX":
            print("You won!")
            return
        attempt += 1
    print("You lost!")

if __name__ == "__main__":
    with open('words.txt', 'r') as f:
        words = f.read().split()
    word = words[random.randint(0, len(words))]
    guess_word(word)

