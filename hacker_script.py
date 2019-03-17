from string import ascii_letters

def password_generator():
    for char in ascii_letters:
        for char2 in ascii_letters:
            yield char + char2
            
# if __name__ == '__main__':
#     passwords = []
#     for password in hacker():
#         passwords.append(password)

        
