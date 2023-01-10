# Importing necessary module.
import sys
import re
import random

# Exception handling for errors like IndexError and FileNotFoundError.
try:
    input_file = sys.argv[1]
    open(input_file)
# If command-line argument i.e. file name is not there then IndexError occurs
# and the error below is prompted.
except IndexError:
    print('Error: Cannot proceed due to missing command-line argument.')
    quit()
# If the provided file name is not found then the below error occurs and the
# error is prompted on the screen.
except FileNotFoundError:
    print(f'Error: The file "{sys.argv[1]}" cannot be opened. Sorry about that.')
    quit()

# Creating university domain which is same for all the students.
# university_domain = '@poppleton.ac.uk'

# User-defined function to generate required emails.
def generate_emails(id_number, name_details):
    # Getting family names from name details using by indexing.
    family_names = name_details[1].strip().split(' ')

    # Getting the initials from family names.
    initials = ''
    for words in family_names:
        initials += words[0] + '.'
    initials = initials.lower()

    # Getting surname from name details and removing non-alphabetic characters.
    surname = name_details[0]
    surname = re.sub(r'[^a-zA-Z]+', '', surname)
    surname = surname.lower()

    # Generating four digit random number.
    four_digit = random.randint(1111, 9999)

    # Concatenating the above details and generating the email.
    email = initials + surname + str(four_digit) + '@poppleton.ac.uk' + '\n'

    # Concatenating email with student id number and returning it.
    id_with_email = id_number + ' ' + email
    return id_with_email

# Reading the file given as command line argument and writing the emails into a
# new file called emails.txt.
with open(input_file, 'r') as read_file:
    for line in read_file:
        # Parsing every line of file to get student id and name details.
        student_id = line[:8]
        name = line[9:].strip().split(',')
        created_emails = generate_emails(student_id, name)

        # Writing the emails into emails.txt file.
        with open('emails.txt', 'a') as write_file:
            write_file.write(created_emails)