number = 23
guess = int(input('input integer: '))
if guess == number:
    # new block start here
    print('Congratulation, got it.')
    print('But you do not win any prize')
    # new block end here
elif guess < number:
    print('No, it is little higher')
    # you must have guessed number < number to reach here
else:
    print('No, it is smaller a little bit')
    # you must have guessed number > number to reach here
print('done')
