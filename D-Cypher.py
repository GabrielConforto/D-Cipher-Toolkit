import os
import base64

file = input("Which .txt do you wish to decrypt? ")

cipher = int(input("Which cipher is the string in?\n"
                   "1. Octal\n"
                   "2. Hexadecimal\n"
                   "3. Base32\n"
                   "4. Base64\n"))

with open(file, 'r') as f:
    string = f.read().strip()

def write_to_file(decoded_string):
    with open('decoded.txt', 'a') as output_file:
        output_file.write(decoded_string + '\n')

def octal():
    try:
        octal_numbers = string.split()
        decoded_chars = [chr(int(num, 8)) for num in octal_numbers]
        decoded_string = ''.join(decoded_chars)
        write_to_file(decoded_string)
        print('Successfully decoded the string')
    except ValueError as e:
        print(f"Conversion error: {e}")

def hex():
    try:
        hex_numbers = string.split()
        decoded_chars = [chr(int(num, 16)) for num in hex_numbers]
        decoded_string = ''.join(decoded_chars)
        write_to_file(decoded_string)
        print('Successfully decoded the string')
    except ValueError as e:
        print(f"Conversion error: {e}")

def b32():
    try:
        dcode = base64.b32decode(string).decode('utf-8')
        write_to_file(dcode)
        print('Successfully decoded the string')
    except ValueError as e:
        print(f"Conversion error: {e}")

def b64():
    try:
        dcode = base64.b64decode(string).decode('utf-8')
        write_to_file(dcode)
        print('Successfully decoded the string')
    except ValueError as e:
        print(f"Conversion error: {e}")

if cipher == 1:
    octal()
elif cipher == 2:
    hex()
elif cipher == 3:
    b32()
elif cipher == 4:
    b64()
else:
    print("Invalid cipher ID, try again.")
