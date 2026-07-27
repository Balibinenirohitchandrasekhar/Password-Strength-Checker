import string
print("========== Password Strength Checker ==========")
#Taking Input
password = input()
password_length=8
# Check Password length
score=0

if len(password) >= password_length:
    print("Password length is valid")
    score += 1
else :
    print ("Password should have minimum 8 characters")


# Check Password Capital or not 

has_upper = any(char.isupper() for char in password)
if has_upper:
    print("✅Contains Upper character")
    score += 1
else :
    print("Password should have atleast 1 Capital Letter")

#Check Password Lowercase or not

has_lower = any(char.islower() for char in password)
if has_lower:
    print("✅Contains Lower character")
    score += 1
else :
    print("Password should have atleast 1 Lower Letter")

# Check Number in a Password

number = any(char.isdigit() for char in password)
if number:
    print("✅Contains Number")
    score += 1
else  :
    print("Password should have atleast 1 number") 

# Assign Special Characters

special_characters = any(char in string.punctuation for char in password)
if special_characters:
    print("✅Contains Special character")
    score += 1
else :
    print("Password should have atleast 1 special character")

if score == 5 :
    print("Strong")
elif score >= 3:
    print("Medium")
else:
    print("Weak")