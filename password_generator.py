import json
import os
import random

"""
throws IndexError if all options are False
"""
def generate_password(length: int, use_chars: bool,
                      use_numbers: bool, use_special_chars: bool) -> str:
    
    if length < 1 or length > 128:
        raise ValueError

    LOWERCHARS = 'abcdefghijklmnopqrstuvwxyz'
    UPPERCHARS = LOWERCHARS.upper()
    NUMBERS = '0123456789'
    SPECIALCHARS = r'!@#$%^&*_.?'
    password = ''

    config = []

    if use_chars:
        config.append(LOWERCHARS)
        config.append(UPPERCHARS)
    if use_numbers:
        config.append(NUMBERS)
    if use_special_chars:
        config.append(SPECIALCHARS)

    for _ in range(length):
        password += random.choice(random.choice(config))

    return password

try:
    # Initialize file with default values
    with open('config.json', 'x') as config_file:
        json.dump(
            {
                'passwordLength': 12,
                'useChars': True,
                'useNumbers': True,
                'useSpecialChars': True
            }, config_file
        )
        os.system(f"msg {os.getlogin()} Configuration file not found! Creating a new one." if os.name == 'nt' else "echo Configuration file not found! Creating a new one.")
except FileExistsError:
    pass

# Generate password and write to file
with open('generated_password.txt', 'w') as file:
    config = json.load(open('config.json'))
    try:
        file.write(generate_password(config['passwordLength'], config['useChars'], config['useNumbers'], config['useSpecialChars']))
        os.system(f"msg {os.getlogin()} Password generated successfully in '{file.name}'!" if os.name == 'nt' else f"echo Password generated successfully in '{file.name}'")
    except IndexError:
        os.system(f"msg {os.getlogin()} Error: At least one generate option must be activated in 'config.json'!" if os.name == 'nt' else "echo Error: At least one option must be activated in 'config.json'!")
    except ValueError:
        os.system(f"msg {os.getlogin()} Error: Password length must be between 1 and 128!" if os.name == 'nt' else "echo Error: Password length must be between 1 and 128!")