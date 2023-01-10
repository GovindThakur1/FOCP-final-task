# Importing the necessary module
import sys
import time

# Declaring a constant dictionary containing the standard frequencies of
# english letters
LETTER_FREQUENCIES = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.00095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074
}

# Defining class CaesarCipherDecrypter
class CaesarCipherDecrypter:
    def __init__(self, encrypted_message):
        self.encrypted_message = encrypted_message

    # Defining decrypt method which decrypts the message and returns the
    # decrypted message
    def get_decrypted(self, shift):
        encrypted_message = self.encrypted_message
        decrypted_message = ''
        for character in encrypted_message:
            if character.isdigit():
                print("\nError: Decryption Failed. Probably not a Caesar Cypher at play here.\n")
                quit()
            elif character.isalpha():
                if character.islower():
                    decrypted_message += chr((ord(character) - ord('a') - shift) % 26 + ord('a'))

                elif character.isupper():
                    decrypted_message += chr((ord(character) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_message += character

        return decrypted_message

    # Defining method which takes the decrypted message as argument and
    # returns the difference between the frequencies of letters in the
    # message and the standard frequency of english letters in s Text
    def get_letter_frequency_difference(self, string_value):
        letter_with_counts = {}
        for letter in string_value:
            if letter.isalpha():
                if letter in letter_with_counts:
                    letter_with_counts[letter] += 1
                else:
                    letter_with_counts[letter] = 1

        # Calculating frequency difference of the letters in decrypted
        # message and standard english language letters
        difference = 0
        for letter, count in letter_with_counts.items():
            frequency_of_letters = count / len(string_value)
            eng_letter_frequency = LETTER_FREQUENCIES[letter.lower()]
            difference += abs(frequency_of_letters - eng_letter_frequency)
        if self:
            return difference

    # Defining decrypt method
    def decrypt(self):
        """
        Decrypt method calls get_decrypted method to obtain decrypted message
        and then calculates the frequency difference for every decrypted
        message and then prints the correct decrypted message with very low
        letter frequency difference (i.e.highest similarity in letter
        frequencies) and also prints corresponding shift key value
        """
        correct_shift = 0
        correct_decryption = ''
        minimum_frequency_diff = float('inf')
        # Trying possible shifts in range 0 and 26
        for shift in range(0, 26):
            decrypted_msg = self.get_decrypted(shift)

            # Checking the frequency difference for each decrypted message and
            # then storing the decryption with the least frequency difference
            # and corresponding shift key
            letter_frequency_difference = self.get_letter_frequency_difference(decrypted_msg)
            if letter_frequency_difference < minimum_frequency_diff:
                minimum_frequency_diff = letter_frequency_difference
                correct_shift = shift
                correct_decryption = decrypted_msg

        print(f'\n\nShift value: {correct_shift}\nDecrypted Message:\n\n{correct_decryption}')

# Getting encrypted file name from command line argument
encrypted_file = sys.argv[1]

# Exception handling to handle errors if the file is not found or not able to
# be opened
try:
    with open(encrypted_file, 'r') as file:
        message = file.read()
# If the provided file name is not found or cannot be opened then the below
# error occurs and the error is prompted on the screen.
except FileNotFoundError:
    print(f'Error: The file "{encrypted_file}" cannot be opened. Sorry about that.\n')
    quit()

# Screen Display Simulation
print('\n\t\t\t     >> INITIATING DECRYPTION <<')
for i in range(4):
    print('\t\t...', end='', flush=True)
    time.sleep(1)

# Creating Object and calling the method
decrypt_obj = CaesarCipherDecrypter(message)
decrypt_obj.decrypt()