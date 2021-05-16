# Prompting and Passing

from sys import argv

script, user_name, password = argv
prompt = ">>>> "

print(f"Hy {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}? ")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice!
""")

print(f"And you password is: {password}, don't forget!")
