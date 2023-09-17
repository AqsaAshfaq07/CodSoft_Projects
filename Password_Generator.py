# Step - 1
import random

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
              'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              '!', '#', '$', '%', '&', '(', ')', '*', '+']

# Step - 2
print("Welcome to the Password Generator!")

num_letters = int(input("How long do you want your password? \n"))

# Step-3
# Easy Level

password = ""

for char in range(1, num_letters + 1):
    password += random.choice(characters)

# Step - 4
# Hard Level

password_list = []

for char in range(1, num_letters + 1):
    password_list.append(random.choice(characters))

random.shuffle(password_list)

# Step - 5
# Gather the whole thing

password_ = ""

for char in password_list:
    password_ += char

if len(password_) > num_letters: password_ = password_[0:num_letters]
print('Strong Password: ', password_)
