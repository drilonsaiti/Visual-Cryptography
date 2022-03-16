

#XOR
from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot
from google.colab.patches import cv2_imshow
#Ова е наједноствна шифрирање/дешифрирањ на слика.
#Со користење на XOR.


#се зема патека на слика
imagePath = input(r'Enter path of image : ')

print('Choose operation to be done:\n\t1- Encryption\n\t2- Decryption')
select = input('Your Choice: ')
#се зема клучот за шифрирање/дешифрирање
key = int(input('Enter key for encryption : '))


# се читува слика и се чува на променлива
img = cv2.imread(imagePath)

#конвертирање на слика во низа од бајти
image_bytes = bytearray(img)

for k,v in enumerate(image_bytes):
  #со користење на XOR правиме шифрирање/дешифрирање на бајт
  image_bytes[k] = v ^ key

enc_img = np.frombuffer(image_bytes, np.uint8).reshape(img.shape)

if select == '1':
  print('Choose operation to be done:\n\t1- Visible image but encrypted \n\t2- No visible image but encrypted')
  selectOpt = input('Your Choice: ')
  if selectOpt == '1':
    cv2.imwrite("XOR-Encrypted.png",enc_img)
    print("Encrypted image")
    cv2_imshow(enc_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
  elif selectOpt == '2':
    #се чува шифрирана/дешифрирана слика

    writeImage = open("XOR-No-visibilty-image.jpg",'wb')
    writeImage.write(enc_img)
    writeImage.close()
elif select == '2':
  cv2.imwrite("XOR-Dencrypted.png",enc_img)
  print("Decrypted image")
  cv2_imshow(enc_img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()



print('The path of file : ', imagePath)
print('Key for encryption : ', key)