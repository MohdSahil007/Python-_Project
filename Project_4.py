#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 4. password_generator.py
import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    character_pool = string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    
    if length < 1:
        return None

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to Secure Password Generator")
    
    length = int(input("Enter desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    generated_password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    
    if generated_password:
        print(f"Generated Password: {generated_password}")
    else:
        print("Invalid password length.")

if __name__ == "__main__":
    main()

