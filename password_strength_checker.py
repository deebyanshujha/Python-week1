import string
import random
import getpass

def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("*To short minimumm 8 characters*")
    if not any(c.islower() for c in password):
        issues.append("*password doesnt contain lowercase letters*")
    if not any(c.isupper() for c in password):
        issues.append("*password doesnt contain uppercase letter*")
    if not any(c.isdigit() for c in password):
        issues.append("*password doesnt contain numbers*")
    if not any(c in string.punctuation for c in password):
        issues.append("*password doesnt contain any special character*")
    return issues

def generate_strong_password(length = 12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

password = getpass.getpass("enter a password: ");
issues = check_password_strength(password)

if not issues:
    print("Strong password! you are good to go.")
else:
    for issue in issues:
        print(f"- {issue}")

suggestion = generate_strong_password()    
print("\n suggesting you a strong password")
print(suggestion)