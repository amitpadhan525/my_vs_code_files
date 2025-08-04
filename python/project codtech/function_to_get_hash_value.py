import hashlib

def get_file_hash(filename):
    try:
        with open(filename, "rb") as file:
            data = file.read()  # Read entire file as bytes
            hash_value = hashlib.sha256(data).hexdigest()
        return hash_value
    except FileNotFoundError:
        return None
filename = input("Enter filename: ")                #file name like /home/user/file.txt
hash_result = get_file_hash(filename)

if hash_result:
    print(f"SHA-256 hash of '{filename}': {hash_result}")
else:
    print("File not found. Please check the filename.")
