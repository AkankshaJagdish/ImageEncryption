from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

try:
    # take path of image as a input
    path = input(r'Enter path of Image : ')

    # taking decryption key as input for XOR encryption
    key_xor = int(input('Enter Key for XOR decryption of Image : '))
    
    # taking decryption key as input for AES encryption
    key_aes = input('Enter Key for AES decryption of Image : ')
    # it should be 16, 24 or 32 bytes long
    key_aes = key_aes.encode()

    # print path of image file and decryption key that we are using
    print('The path of file : ', path)
    print('Note : Encryption key and Decryption key must be same.')
    print('Key for XOR decryption : ', key_xor)
    print('Key for AES decryption : ', key_aes)

    # open file for reading purpose
    fin = open(path, 'rb')

    # storing image data in variable "image"
    encrypted_image = fin.read()
    fin.close()

    # AES iv was appended to the file, so we must extract it first
    iv = encrypted_image[:16]
    encrypted_image = encrypted_image[16:]

    # create a new AES cipher object for decryption
    cipher = AES.new(key_aes, AES.MODE_CBC, iv=iv)
    
    # perform AES decryption
    decrypted_image = unpad(cipher.decrypt(encrypted_image), AES.block_size)

    # converting image into byte array to perform decryption easily on numeric data
    image = bytearray(decrypted_image)

    # performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        image[index] = values ^ key_xor

    # opening file for writing purpose
    fin = open(path, 'wb')

    # writing decryption data in image
    fin.write(image)
    fin.close()
    print('Decryption Done...')

except Exception as e:
    print('Error caught : ', str(e))

# Key for XOR decryption :  123
# Key for AES decryption :  myverysecretkey!