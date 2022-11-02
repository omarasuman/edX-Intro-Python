# Ask user for their name and removes whitespace
# from str and capitalize user's name
name = input("what's your name? ").strip().title()

# split user's name into first name and last name
first, last = name.split(" ")

# say hello to user
print(f"hello, {first}")
