secret = 7
attempts = 0

while attempts < 5:
    guess= int(input("Guess The Number: "))
    attempts += 1
    
    if guess == secret:
        print(f"Correct! you got it in {attempts} attempts!")
        break
    elif guess > secret:
        print("Too high!")
        
    else:
        print("Too low!")
        
else:
        print("Game over! Secret  Number was 7!")
