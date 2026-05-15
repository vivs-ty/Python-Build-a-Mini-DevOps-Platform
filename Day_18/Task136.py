# Task 136: Encrypt and decrypt files with a basic encryption method.

def encrypt_decrypt_file(filepath, key=123):
    # Read original bytes
    with open(filepath, 'rb') as f:
        data = bytearray(f.read())
        
    # Shift each byte using the key
    for i in range(len(data)):
        data[i] ^= key
        
    # Write modified bytes back to the file
    with open(filepath, 'wb') as f:
        f.write(data)
        
    print(f"Processed {filepath}")
    print(f" \n Python 30 days Series - Day 18 Task 136 \n")
    print(f" \n Day 18 : Advanced File Automation \n")
    print(f" \n Have a good one! \n " + "-"*40)
    