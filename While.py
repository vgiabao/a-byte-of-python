number = 23
running = True

while running:
    guess = int(input('Enter an int: '))
    # congratulation and stop the loop whien the number is guessed
    if guess == number:
        print('congratulation!')
        # it causes stop
        running = False
    # print a hint when the guessed is smaller than the number
    elif guess < number:
        print('No, it is higher.')
    # print the hint when the guessed is larger than the number
    else:
        print('No, it is smaller.')
# print statement to inform the loop is stopped
else:
    print('The while loop is over.')
print('done')
