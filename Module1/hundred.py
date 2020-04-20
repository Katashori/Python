from datetime import date
user_name = input("Hello! What is your name? ")
age = int(input("Thank you! How old are you? "))
print(f'{user_name}, you will be a hundred in {date.today().year + 100 - age}')
