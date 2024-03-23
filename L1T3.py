#Level 1 Task 3
import re
def is_valid_email(email):

    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(email_regex, email):
        return True
    else:
        return False
    
user_email = input("Enter your email id: ")
print(is_valid_email(user_email))
