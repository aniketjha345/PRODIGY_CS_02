from PIL import Image

def encrypt_image(image_path, key):
    """
    Encrypt an image using a bitwise XOR operation with the given key.
    
    :param image_path: Path to the image file.
    :param key: Integer key for encryption (0-255).
    """
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    # Encrypt each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    # Save the encrypted image
    image.save("encrypted_image.png")
    print("Encryption complete. Encrypted image saved as 'encrypted_image.png'.")

def decrypt_image(image_path, key):
    """
    Decrypt an image using a bitwise XOR operation with the given key.
    
    :param image_path: Path to the image file.
    :param key: Integer key for decryption (0-255).
    """
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    # Decrypt each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    # Save the decrypted image
    image.save("decrypted_image.png")
    print("Decryption complete. Decrypted image saved as 'decrypted_image.png'.")

def main():
    """
    Main function to handle user input for encrypting or decrypting images.
    """
    while True:
        print("\nImage Encryption Tool")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            image_path = input("Enter the path of the image to encrypt: ").strip()
            key = int(input("Enter the encryption key (0-255): ").strip())
            if 0 <= key <= 255:
                encrypt_image(image_path, key)
            else:
                print("Error: Key must be between 0 and 255.")
        elif choice == "2":
            image_path = input("Enter the path of the encrypted image: ").strip()
            key = int(input("Enter the decryption key (0-255): ").strip())
            if 0 <= key <= 255:
                decrypt_image(image_path, key)
            else:
                print("Error: Key must be between 0 and 255.")
        elif choice == "3":
            print("Exiting the tool.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
