username=input("Enter Username: ")
password=input("Enter Password: ")

correc_username="arnab"
correc_pass="python123"

if username==correc_username and password==correc_pass:
    print("Login successful! Welcome Arnab!")
    
elif  username==correc_username and password!=correc_pass: 
    print("Wrong pass bro") 
else:
        print("User not found!")
