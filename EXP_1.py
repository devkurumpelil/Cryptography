message = input("Enter a 4-letter message: ").upper()
# Position order for encryption
order = [3, 1, 4, 2]
if(len(message) == 4):
    encrypted = ' '.join(message[i - 1] for i in order)
    print("Encrypted message:", encrypted)

    # Reverse the shuffling
    decrypted = ''.join(
        encrypted[order.index(i + 1)] for i in range(4)
    )
    print("Decrypted message:", decrypted)
else:
    print("Please enter exactly 4 characters.")
