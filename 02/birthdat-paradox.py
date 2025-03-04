import datetime, random, typing

def get_birthdays(n: int) -> list[int]:
    if n < 1 or n > 365 :
        return None;

    birthdays = [random.randint(0, 364) for _ in range(n)]

    return birthdays

def has_duplicate(l: list) -> bool:
    return len(l) != len(set(l))

size = int(input("How many birthdays shall I generate? (Max 100)\n> "))
iterations = int(input("How many iterations shall I run?\n> "))

duplication_count = 0

for i in range(iterations):
    if (has_duplicate(get_birthdays(size))):
        duplication_count += 1

print(f"Out of {iterations} simulations of {size} people,there was a matching birthday in that group {duplication_count} times.")
print(f"This means that {size} people have a {(duplication_count / iterations) * 100:.2f} % chance of having a matching birthday in their group.")
print("That's probably more than you would think!")