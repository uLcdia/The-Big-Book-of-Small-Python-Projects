import typing

def collatz_sequence(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n % 2 == 0:
        return [n] + collatz_sequence(n // 2)
    else:
        return [n] + collatz_sequence(n * 3 + 1)

if __name__ == '__main__':
    while True:
        user_input = input('Enter a starting number (greater than 0) or QUIT:\n> ')
        if user_input.lower() == 'quit':
            break

        try:
            n = int(user_input)
            if n <= 0:
                print("Please enter a positive integer.")
                continue

            sequence = collatz_sequence(n)
            print(sequence)

        except ValueError:
            print("Invalid input. Please enter an integer or 'QUIT'.")