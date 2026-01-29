# #todo:Assignment5: Creating Custom Module(Backend Structure)
#Problem Statement: VALIDATION MODULE
#create a module validators.py with following fxn.
#1. is_valid_email(email)
#2. is_valid_mobile(phone)
#3. is_strong_password(password)

#Use the module inside app.py


from validators import is_valid_email, is_valid_mobile, is_strong_password

print(is_valid_email("sa@lpu.com"))
print(is_valid_mobile("987654321"))
print(is_strong_password("StrongP@ss1"))