# PBE

PBE（Password Based Encryption，基于密码加密），由hash函数衍生出key和iv。

**openssl密码加密特征：** 密文以`U2FsdGVkX1`开头，base64解码为`Salted__`

> 本页原为 `Crypto/PBE.md` 算法对应表，2026-09 治理并入原 `CTF/README.md` 的 PBE/U2FsdGVkX1 章节（去重）。

## 算法介绍

PBE算法在加密过程中并不是直接使用口令来加密，而是加密的密钥由口令生成，这个功能由PBE算法中的KDF函数完成。KDF函数的实现过程为：将用户输入的口令首先通过"盐"（salt）的扰乱产生准密钥，再将准密钥经过散列函数(MD5等)多次迭代后生成最终加密密钥，密钥生成后，PBE算法再选用对称加密算法对数据进行加密，可以选择AES、DES、3DES、RC5等对称加密算法。

### 口令

是某个用户自己编织的便于记忆的一串单词、汉字、数字字符。

口令的特点容易被记忆，但也容易泄露或者被盗取。也容易被社会工程学、暴力破解、撞库等方式获取！

### 密钥

是经过加密算法计算出来的。

密钥一般不容易记忆，不容易被破解，而且很多时候密钥是作为算法的参数出现的。算法对密钥长度也是有要求的，因为加密算法的作用就是利用密钥来扰乱明文顺序。

### 加盐了的口令

用户密码加盐意思就是将用户的口令，加之可能是随机插入的字符串（加盐算法），然后进行哈希，以防止脱裤后攻击者知晓明文密码，此时盐也需要同用户数据存在一起（随机盐就是一个用户一个盐，固定盐就是整个系统一个盐，但如果这个固定盐泄露，就可以根据这个固定盐建立彩虹表）。即使攻击者成功通过彩虹表反向哈希，拿到的字符串还是加盐过后的口令，无法知晓真正的口令。（除非拿到了加盐算法？）

## U2FsdGVkX1（OpenSSL 特征）

OpenSSL的特征就是开头有`U2FsdGVkX1`

参考：[ToolsFx Wiki - PBE#aes](https://github.com/Leon406/ToolsFx/wiki/PBE#aes)

U2FsdGVkX1 is the base64 encoding of the ASCII string **Salted__**. It is a prefix that indicates that the encrypted data was produced by **OpenSSL** or a compatible library. It is followed by 8 bytes of **salt**, which is used to derive the encryption key and IV from the password. The actual encrypted data starts at the 17th byte.

This prefix is not insecure, as it only reveals that OpenSSL was used, which is not a secret. The salt is random and different for each encryption, so it prevents attacks based on precomputed tables¹.

To decrypt such a thing, you need to know the password and the encryption algorithm (such as AES-256-CBC). You can use OpenSSL or any library that supports the same format. You can also follow these steps:

- Base64-decode the output from OpenSSL, and UTF-8 decode the password, so that you have the underlying bytes for both of these.

- Separate the first 16 bytes of the decoded output, which consist of 8 bytes of Salted_\_ and 8 bytes of salt.

- Use a key derivation function (such as PBKDF2 or EVP_BytesToKey) to generate the encryption key and IV from the password and salt. The key size and IV size depend on the encryption algorithm.

- Use the encryption algorithm (such as AES-256-CBC) to decrypt the remaining bytes of the decoded output, using the key and IV obtained in the previous step.

- The result is the original plaintext.

## 常用算法对应（CryptoJs 实现）

### [AES](https://www.sojson.com/encrypt_aes.html)

常见基于CryptoJs实现， 使用AES-256-CBC算法及PKCS5Padding/PKCS7Padding，生成key,iv长度为32字节,16字节

对应算法为 `MD5and256bitAES-CBC-OPENSSL`，其他默认即可

### [DES](https://www.sojson.com/encrypt_des.html)

常见基于CryptoJs实现，使用DES-CBC算法及PKCS5Padding/PKCS7Padding，生成key,iv长度为8字节

对应算法为 `MD5andDES`，其他默认即可

### [RC4](https://www.sojson.com/encrypt_rc4.html)

常见基于CryptoJs实现，使用RC4算法， 生成key长度32字节（openssl 16字节）

对应算法为 `MD5andRC4`，其他默认即可

### [3DES](https://www.sojson.com/encrypt_triple_des.html)

常见基于CryptoJs实现，使用DESede-CBC算法及PKCS5Padding/PKCS7Padding，生成key,iv长度为24字节,8字节

对应算法为 `MD5andTripleDES`，其他默认即可

### 其他算法

- RC2
- TwoFish
- IDEA
