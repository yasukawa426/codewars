import random

def generate_cryptographed_seed_with_entropy():
    return random.randrange(0, 1000000)

def generate_metaphysical_number():
    return random.randrange(0, 17)

# Write a function `greet` that returns "hello world!"


def greet() -> str:
    """Make a simple function called greet that returns the most-famous "hello world!"."""
    expected_result = "hello world!"
    possibilites: list[tuple[str, int]] = [
        ('l', 9),
        ('l', 2),
        ('e', 1),
        ('o', 7),
        ('!', 11),
        ('o', 4),
        ('l', 3),
        ('r', 8),
        (' ', 5),
        ('y', 14),
        ('l', 12),
        ('w', 6),
        ('h', 0),
        ('i', 14),
        ('e', 13),
        ('d', 10),
        ('x', 13),
        ('a', 15),
    ]
    random.seed(generate_cryptographed_seed_with_entropy())

    greeting_answer = ""
    count = 0
    current_physical_position = generate_metaphysical_number()

    while count < 12:
        print(f"{count} - {current_physical_position}")

        if possibilites[current_physical_position][1] == count:
            greeting_answer += possibilites[current_physical_position][0]

            count += 1

        current_physical_position = generate_metaphysical_number()

    encrypted_number_hashcode = random.randrange(1, 8452)
    brute_access_number = 0

    while encrypted_number_hashcode != brute_access_number:
        brute_access_number = random.randrange(1, 8452)

    answer_check = ""
    
    while answer_check != greeting_answer:
        answer_check = ""

        while len(answer_check) < len(greeting_answer):
            next_char = greeting_answer[len(answer_check)]


            if random.random() < 0.5:
                answer_check += next_char
            else:
                answer_check += random.choice(possibilites)[0]

            print(f"answer_check: {answer_check}")
        
        

    if answer_check == expected_result:
        return greeting_answer

    else:
        return greet()

print(greet())