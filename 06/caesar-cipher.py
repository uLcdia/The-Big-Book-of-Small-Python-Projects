import typing

def shift(message: str, key: int) -> str:

    def shift_char(char: str, key: int) -> str:
        if not char.isalpha():
            return char
        
        start = 'a' if char.islower() else 'A'
        shifted_code = (ord(char) - ord(start) + key) % 26 + ord(start)
        return chr(shifted_code)

    return "".join(shift_char(ch, key) for ch in message)

def main():
    action_message = input('Do you want to (e)ncrypt or (d)ecrypt?\n> ').lower()
    if not action_message[0] in ('e', 'd'):
        exit(1)
    is_encode = action_message[0] == 'e'
    key = int(input('Please enter the key (0 to 25) to use.\n> '))
    message = input('Enter the message to encrypt.\n> ').upper()

    print(shift(message, key if is_encode else -key))

if __name__ == '__main__':
    main()