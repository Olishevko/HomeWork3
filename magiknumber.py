import random
guesses_taken = 0
print('Привет, давай сыграем, я загадал число от 1 до 20')
number = random.randint(1,20)
while guesses_taken < 6:
    print('Какое число я загадал?')
    guess = input()
    guess = int(guess)
    guesses_taken = guesses_taken+1
    if guess < number:
        print('Мое число больше твоего')
    if guess > number:
        print('Мое число меньше твоего')
    if guess == number:
        break
if guess == number:
    guesses_taken = str(guesses_taken)
    print('Ты угадал число с' , guesses_taken, 'попытки.')
if guess != number:
    number = str(number)
    print('Жаль, но у тебя не осталось попыток. Я загадал число', number, '.')

# answer = input('continue? Y/n')   не разобрался.
# if answer == 'n':
#     break