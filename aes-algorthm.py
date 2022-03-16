


#AES
import os
import cv2
import numpy as np
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from google.colab.patches import cv2_imshow


# се зема патека на слика
imagePath = input(r"Enter path of image : ")

#генерираме рандом клуч
key = os.urandom(16)

#Вектор за иницијализација (IV) е произволен број што може да се користи заедно со клуч за шифрирање на податоците
iv = os.urandom(16)

img = cv2.imread(imagePath)

select = -1

while select != "3":
    print("Choose operation to be done:\n\t1- Encryption\n\t2- Decryption\n\t3- Exit")
    select = input("Your Choice: ")

    if select == "1":
        #се креира објект од АЕС
        cipher = AES.new(key, AES.MODE_CBC, iv)
        # се читува слика и се чува на променлива
        img_bytes = img.tobytes()
        #шифирање на бајти
        encrypted_image = cipher.encrypt(img_bytes)

        #преку numpy библиотека генерираме слика
        enc_img = np.frombuffer(encrypted_image, np.uint8).reshape(img.shape)
        print(
            "Choose operation to be done:\n\t1- Visible image but encrypted \n\t2- No visible image but encrypted"
        )
        selectOpt = input("Your Choice: ")

        if selectOpt == "1":
            #се чува шифрирана слика
            cv2.imwrite("AES-Encrypted.png", enc_img)
            cv2_imshow(enc_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif selectOpt == "2":
            #се чува шифрирана слика
            writeImage = open("AES-No-visibilty-image.jpg", "wb")
            writeImage.write(enc_img)
            writeImage.close()

    elif select == "2":
        #дешифрирање на слика
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_image = cipher.decrypt(enc_img.tobytes())
        dec_img = np.frombuffer(decrypted_image, np.uint8).reshape(enc_img.shape)

        #се чува дешифрирана слика
        cv2.imwrite("AES-DecryptedImage.png", dec_img)
        print("Decrypted image")
        cv2_imshow(enc_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        break