
def play_game():
    secret_number = 7
    while True:
        guess = int(input("Enter your guess: "))
        if guess == secret_number:
            print("🎉 Congratulations! You guessed it correctly.")
            break   
        elif guess > secret_number:
            print("Too High! Try a smaller number.")
        else:
            print("Too Low! Try a bigger number.")



play_game()