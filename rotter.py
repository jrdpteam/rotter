import os
import sys
import time
import colorama
from colorama import Fore, Back, Style, init

def rot(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_text += shift_char(char, shift)
        else:
            encrypted_text += char
    return encrypted_text

def shift_char(char, shift):
    if char.isalpha():
        if char.islower():
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif char.isupper():
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    elif char.isdigit():
        return chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
    return char


asc1 = r"""            _   _            """
asc2 = r""" JRDP Team | | | |   v3.0    """
asc3 = r"""  _ __ ___ | |_| |_ ___ _ __ """
asc4 = r""" | '__/ _ \| __| __/ _ \ '__|"""
asc5 = r""" | | | (_) | |_| |_|  __/ |  """
asc6 = r""" |_|  \___/ \__|\__\___|__|  """

def help():
    help_message = f"""
{Fore.BLUE}||====================================================||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL} {Fore.RED}\x1b[5m    {asc1}{Style.RESET_ALL}       {Fore.BLUE}           ||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL} {Fore.RED}\x1b[5m    {asc2}{Style.RESET_ALL}       {Fore.BLUE}           ||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL} {Fore.RED}\x1b[5m    {asc3}{Style.RESET_ALL}       {Fore.BLUE}           ||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL} {Fore.RED}\x1b[5m    {asc4}{Style.RESET_ALL}       {Fore.BLUE}           ||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL} {Fore.RED}\x1b[5m    {asc5}{Style.RESET_ALL}       {Fore.BLUE}           ||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL} {Fore.RED}\x1b[5m    {asc6}{Style.RESET_ALL}       {Fore.BLUE}           ||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL}                                                    {Fore.BLUE}||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL}                                                    {Fore.BLUE}||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL} Flags:                                             {Fore.BLUE}||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL}  {Fore.YELLOW}-e{Style.RESET_ALL} = encrypt                                      {Fore.BLUE}||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL}  {Fore.YELLOW}-d{Style.RESET_ALL} = decrypt                                      {Fore.BLUE}||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL}  {Fore.YELLOW}-c{Style.RESET_ALL} = encryption type                              {Fore.BLUE}||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL}                                                    {Fore.BLUE}||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL} Usage:                                             {Fore.BLUE}||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL} {Fore.CYAN}python3 rotter.py -c ENCODING -e "YOUR_TEXT"{Style.RESET_ALL}       {Fore.BLUE}||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL} Example:                                           {Fore.BLUE}||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL} {Fore.CYAN}python3 rotter.py -c ROT13 -e "love you"{Style.RESET_ALL}           {Fore.BLUE}||{Style.RESET_ALL}
{Fore.BLUE}||{Style.RESET_ALL} You can use any encoding between 1 & 100.          {Fore.BLUE}||{Style.RESET_ALL}
{Fore.BLUE}||====================================================||{Style.RESET_ALL}

"""

    if "{Fore.RED}" in help_message:
        help_message = help_message.replace("{Fore.RED}", "")

    print(help_message)

def main():
    args = sys.argv[1:]

    if '-h' in args or '--help' in args:
        help()
        return

    cipher_index = args.index('-c') if '-c' in args else args.index('--cipher') if '--cipher' in args else None
    encrypt_index = args.index('-e') if '-e' in args else args.index('--encrypt') if '--encrypt' in args else None
    decrypt_index = args.index('-d') if '-d' in args else args.index('--decrypt') if '--decrypt' in args else None

    if cipher_index is not None and encrypt_index is not None:
        cipher = args[cipher_index + 1]
        shift = int(cipher[3:]) if cipher.startswith('ROT') and cipher[3:].isdigit() else None
        if shift and 1 <= shift <= 100:
            text = args[encrypt_index + 1]
            result = rot(text, shift)
            print("======================================rotter toolkit======================================")
            print(f'Encrypted text: {result}')
            return

    if cipher_index is not None and decrypt_index is not None:
        cipher = args[cipher_index + 1]
        shift = int(cipher[3:]) if cipher.startswith('ROT') and cipher[3:].isdigit() else None
        if shift and 1 <= shift <= 100:
            text = args[decrypt_index + 1]
            result = rot(text, -shift)
            print("======================================rotter toolkit======================================")
            print(f'Decrypted text: {result}')
            return

    help()

if __name__ == "__main__":
    main()
