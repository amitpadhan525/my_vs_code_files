import hashlib
password=input("Enter password: ")
hash_of_password=hashlib.sha256(password.encode()).hexdigest()              #it create hash of the password
print("Hash : ",hash_of_password)