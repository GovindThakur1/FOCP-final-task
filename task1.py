# Importing random module to generate random choices.
import random

# Declaring constant list of words.
WORD_LIST1 = ['brave', 'bitter', 'cross', 'angry', 'happy', 'testy', 'caustic',
              'impressive', 'lie', 'lively']
WORD_LIST2 = ['pink', 'orange', 'gold', 'gray', 'white', 'cyan', 'maroon',
              'beige', 'blue', 'lime']
WORD_LIST3 = ['koala', 'mule', 'rat', 'otter', 'boar', 'mammoth', 'bat',
              'ibex', 'emu', 'dove']


# Function to generate password as per required.
def generate_password(required_number):
    counter = 1
    while counter <= required_number:
        word1 = random.choice(WORD_LIST1)
        word2 = random.choice(WORD_LIST2)
        word3 = random.choice(WORD_LIST3)
        password = word1 + word2 + word3
        print('\t', '|' + str(counter) + '|', '--->', password)
        counter += 1


# Displaying the home screen.
print('\n\t\t\t\t*******WELCOME TO PASSWORD GENERATOR PROGRAM*********\n')


# Prompting the user to enter the number of password required.
while True:
    number_of_password = input('Enter the number of passwords needed: ')
    # Checking if the entered value is a digit.
    if number_of_password.strip().isdigit():
        # Typecasting number_of_password into integer value.
        number_of_password = int(number_of_password)

        # Checking if number_of_password is between 1 and 24 inclusive.
        if number_of_password in range(1, 25):
            break
        else:
            print('Please enter a number between 1 and 24')
    else:
        print('Please enter a number')

    # Printing the passwords
if number_of_password == 1:
    print('\nThe password is :\n')
    generate_password(number_of_password)
else:
    print('\nThe passwords are :\n')
    generate_password(number_of_password)

print('\n\t\t\t\t#######################################################')
print('\t\t\t\t\tThank you for using Password Generator Program!')
print('\t\t\t\t#######################################################')