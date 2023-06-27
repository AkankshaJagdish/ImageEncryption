# Use below command to add PyCryptodome library for AES encryption:
# pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

try:
    # take path of image as a input
    path = input(r'Enter path of Image : ')

    # taking encryption key as input for XOR encryption
    key_xor = int(input('Enter Key for XOR encryption of Image : '))
    
    # taking encryption key as input for AES encryption
    key_aes = input('Enter Key for AES encryption of Image : ')
    # it should be 16, 24 or 32 bytes long
    key_aes = key_aes.encode()

    # print path of image file and encryption key that we are using
    print('The path of file : ', path)
    print('Key for XOR encryption : ', key_xor)
    print('Key for AES encryption : ', key_aes)

    # open file for reading purpose
    fin = open(path, 'rb')

    # storing image data in variable "image"
    image = fin.read()
    fin.close()

    # converting image into byte array to perform encryption easily on numeric data
    image = bytearray(image)

    # performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        image[index] = values ^ key_xor

    # create a new AES cipher object
    cipher = AES.new(key_aes, AES.MODE_CBC)
    
    # perform AES encryption, need to pad the data because AES data size needs to be multiple of 16
    aes_encrypted_image = cipher.encrypt(pad(image, AES.block_size))

    # we need to save the iv to decrypt this image later, so we append it at the beginning of the file
    encrypted_image = cipher.iv + aes_encrypted_image

    # opening file for writing purpose
    fin = open(path, 'wb')

    # writing encrypted data in image
    fin.write(encrypted_image)
    fin.close()
    print('Encryption Done...')

except Exception as e:
    print('Error caught : ', str(e))

# Path of image: assets\resources_top-cybersecurity-threats_730x425.jpg
# Key for XOR encryption :  123
# Key for AES encryption :  myverysecretkey!