import random

word_list = ["chicken", "phone", "apple"]
word = random.choice(word_list)


hidden_word = ['_'] * len(word)
guess_list = []
attempt = 6

while ''.join(hidden_word) != word and attempt > 0:
    print(f"\n {''.join(hidden_word)}")
    print(attempt)
    user_guess = input("Enter a guess: ").lower()

    if user_guess in guess_list:
        print("already exits")
        continue
    guess_list.append(user_guess)

    if user_guess in word:
        for i, letter in enumerate(word):
            if letter == user_guess:
                hidden_word[i] = letter
        print(''.join(hidden_word))
    else:
        print("not in list")
        attempt -= 1

if ''.join(hidden_word) == word:
    print(f"you win. word was {word}")
else:
    print(f"wrong guess. word was {word}")


