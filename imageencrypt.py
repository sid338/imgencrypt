from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()

    # Encrypt each pixel
    for i in range(img.size[0]):  # width
        for j in range(img.size[1]):  # height
            r, g, b = pixels[i, j]

            # Apply a simple encryption operation (XOR with key)
            r = r ^ key
            g = g ^ key
            b = b ^ key

            # Set the modified pixel back
            pixels[i, j] = (r, g, b)

    # Save the encrypted image
    encrypted_image_path = "encrypted_image.png"
    img.save(encrypted_image_path)
    print(f"Image encrypted and saved as {encrypted_image_path}")

def decrypt_image(image_path, key):
    # Decryption is simply the inverse operation of encryption
    encrypt_image(image_path, key)  # XOR again with the same key

# Get input from the user
image_path = input("Enter the path to the image: ")
key = int(input("Enter the encryption key (an integer): "))
operation = input("Would you like to 'encrypt' or 'decrypt' the image? ")

if operation.lower() == 'encrypt':
    encrypt_image(image_path, key)
elif operation.lower() == 'decrypt':
    decrypt_image(image_path, key)
else:
    print("Invalid operation! Please choose 'encrypt' or 'decrypt'.")
