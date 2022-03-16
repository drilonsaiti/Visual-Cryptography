# **The XOR Encryption algorithm**

Алгоритмот за шифрирање XOR е многу ефикасен, но лесен за имплементација со користење на метод на симетрично шифрирање. Поради својата ефикасност и едноставност, шифрирањето XOR се користи во посложените алгоритми за шифрирање што се користат во денешно време.

![symmetric-encryption-image](https://user-images.githubusercontent.com/50522333/158622767-5febdb52-ec6c-4cdf-8b8a-7a7d7ac0906b.jpg)



Алгоритмот за шифрирање XOR се заснова на примена на маска XOR со користење на обичен текст или бајти и клуч

![xor](https://user-images.githubusercontent.com/50522333/158622806-611f9f0b-a8a0-4bf0-92ff-26a825ca6420.jpg)

###  	Code 1 - XOR Algorithm

![xorCODE](https://user-images.githubusercontent.com/50522333/158622897-8e431e98-a808-4f11-bbe3-15515ca6087c.png)

​																										

### Слики

#### Оргинална слика:

![orginal](https://user-images.githubusercontent.com/50522333/158623091-a39ce9e5-2db7-4136-98d7-a993527b5e14.png)

#### Шифриана слика:

![XORencrypted](https://user-images.githubusercontent.com/50522333/158623297-6c171951-e747-4ab3-8831-181f2aeb3029.png)

 

 

 

 

 

# **DES : Data Encryption Standard**

Стандардот за шифрирање на податоци (DES) е блок шифра со симетричен клуч.DES е блок шифра и шифрира податоци во блокови со големина од 64 бита, што значи дека 64 бита обичен текст оди како влез во DES, кој произведува 64 бита шифриран текст. Истиот алгоритам и клуч се користат за шифрирање и дешифрирање, со мали разлики.![encryption_scheme](https://user-images.githubusercontent.com/50522333/158623441-a6f6aab5-cb4a-45a7-9a4c-5d2f75f82f98.jpg)

Троен DES алгоритам TDES(DES3) има фиксна големина на блок податоци од 8 бајти. Се состои од каскада од 3 единечни DES шифри (EDE: Encryption - Decryption - Encryption), каде што секоја фаза користи независен под-клуч DES.

![Untitled-Diagram-130-1](https://user-images.githubusercontent.com/50522333/158623489-e766ec1f-e419-442e-b76c-3fba0f39d78e.jpg)

### Code 2 – Triple DES Alogrithm

![DESCode](https://user-images.githubusercontent.com/50522333/158623541-daaf9636-1ae9-4313-8f87-c3bebc5df40f.png)

​																											

### Слики

#### Оргинална слика:

![orginal](https://user-images.githubusercontent.com/50522333/158623091-a39ce9e5-2db7-4136-98d7-a993527b5e14.png)

#### Шифриана слика:

![DESAlgorithm](https://user-images.githubusercontent.com/50522333/158623742-bfb2a20a-d17b-41e3-adde-70406d55930f.png)

 

 

 

 

 

# **AES = Advanced Encryption Standard**

Алгоритмот за шифрирање AES е симетричен алгоритам за шифрирање блок со големина на блок/дел од 128 бита. Ги конвертира овие поединечни блокови користејќи клучеви од 128, 192 и 256 бита. Откако ќе ги шифрира овие блокови, ги спојува заедно за да го формира шифрениот текст.

![aes](https://user-images.githubusercontent.com/50522333/158624034-5a4c8b99-98a1-4dd1-886f-6014ce49f4d8.png)

### Code 3 - AES Algorithm

![AESCode](https://user-images.githubusercontent.com/50522333/158624046-fb241c6d-db9d-468e-b347-d42bb93b1b54.png)

​																													

### Слики

#### Оргинална слика:

![orginal](https://user-images.githubusercontent.com/50522333/158623091-a39ce9e5-2db7-4136-98d7-a993527b5e14.png)

#### Шифриана слика:

![AESencrypted](https://user-images.githubusercontent.com/50522333/158624060-ed0cfa71-1ff3-488c-b254-2173e2e09c0c.png)

 

 