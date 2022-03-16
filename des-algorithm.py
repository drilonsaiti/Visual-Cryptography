

#DES
from Crypto.Cipher import DES3
from hashlib import md5
from google.colab.patches import cv2_imshow
print('Choose operation to be done:\n\t1- Encryption\n\t2- Decryption')
select = input('Your Choice: ')

#се зема патека на слика
imagePath = input(r'Enter path of image : ')
#се зема клучот за шифрирање/дешифрирање
key = input('Enter key for encryption : ')

#MD5 - A widely used successor to MD4, commonly used for data integrity and password hashing despite being considered broken and not suitable for crypto purposes.
new_key = md5(key.encode('ascii')).digest()
des_key = DES3.adjust_key_parity(new_key)
cipher = DES3.new(des_key, DES3.MODE_EAX, nonce=b'0')

# се читува слика и се чува на променлива
img = cv2.imread(imagePath)
img_bytes = img.tobytes()

#конвертирање на слика во бајт низа
if select == '1':
  encrypted_image = cipher.encrypt(img_bytes)
  print("Encrypted is done")
  enc_img = np.frombuffer(encrypted_image, np.uint8).reshape(img.shape)

  print('Choose operation to be done:\n\t1- Visible image but encrypted \n\t2- No visible image but encrypted')
  selectOpt = input('Your Choice: ')
  if selectOpt == '1':
    cv2.imwrite("DES-Encrypted.png",enc_img)
    print("Encrypted image")
    cv2_imshow(enc_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

  elif selectOpt == '2':
    writeImage = open("Des-No-visibilty-image.jpg",'wb')
    writeImage.write(enc_img)
    writeImage.close()
else:
  decrypted_image = cipher.decrypt(img_bytes)
  dec_img = np.frombuffer(decrypted_image, np.uint8).reshape(img.shape)
  print("Decrypted is done")
  cv2.imwrite("DES-DecryptedImage.png", dec_img)
  print("Decrypted image")
  cv2_imshow(enc_img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()