# BUILD A TOOL TO MONITOR CHANGES
# IN FILES BY CALCULATING AND
# COMPARING HASH VALUES.


# DELIVERABLE: A PYTHON SCRIPT
# USING LIBRARIES LIKE HASHLIB TO
# ENSURE FILE INTEGRITY.
import os
import hashlib
def get_file_hash(file_path):
    with open(file_path,"rb") as file:
        data=file.read()  # Read entire file as bytes
        hash_value=hashlib.sha256(data).hexdigest()
    return hash_value


file_path=input('enter file path: ')  # file path like /home/user/file.txt
try:
    old_hash=get_file_hash(file_path)
    input("Make changes to the file, then press Enter to check again...")
    new_hash=get_file_hash(file_path)
    if old_hash==new_hash:
        print("File integrity is intact. Hash values match.")
    else:
        print("File integrity has been compromised. Hash values do not match.")
except FileNotFoundError:
    print('file not found. Please check the file path.')