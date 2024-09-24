PWD = "I love Python"

for i in range(3):
    p = input("Please enter password: ")
    if p == PWD:
        print("Correct password")
        print("Access allowed")
        break
    print(f"Password is wrong, attempt #{i+1}")
    print("Access not allowed")
else:
    print("Maximum attempts exceeded")
