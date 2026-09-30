# XOR与CBC攻击

> 合并自 `算法性质.md` 的 XOR/CBC 翻转攻击部分与 `CTF/Web/Python.md` 的 XOR 脚本部分（`from pwn import xor`）。

## XOR 运算性质

> 在编程语言中通常使用 `^` 代表异或操作

```python
Commutative: A ⊕ B = B ⊕ A  # 交换率
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C # 结合律
Identity: A ⊕ 0 = A # 0异或任何数，得其本身。相反全1异或任何数，任何数取反
Self-Inverse: A ⊕ A = 0 # 自反性，任何一个数字异或自己都等于0
```

那么可以得出最常用性质：

```text
KEY1 ^ KEY2 ^ FLAG = c
FLAG = c ^ KEY1 ^ KEY2
```

`k1^k2^k3^k1^k2` 相同异或最终可以抵消，其实就是`k3`...?

所以说如果题目给了
`k1^k2^k3^flag`，又能创建`other`来构造出`k1^k2^k3^other`，那就能够通过构造的参数异或出flag。

## 已知明文攻击

当题目给出密文，并提示是XOR加密后，且提示明文包含`crypto{`，那么我们可以先异或该明文（异或的自反性）恢复出部分密钥，看密钥是否有提示。

### 脚本：已知部分明文恢复部分密钥

> 来源：原 `CTF/Web/Python.md`「自制脚本收集」。因为异或性质是异或相同后抵消，那可以直接恢复出已知明文的密钥。

```python
data = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
decoded_data = bytes.fromhex(data)
plain_text = 'crypto{'
key = ''.join((chr(decoded_data[i] ^ ord(plain_text[i]))) for i in range(7))
print(key) # 结果是myXORke，所以可以直接猜测最后XOR的密文是myXORkey
```

## CBC 翻转攻击（Bit Flip）

> 来源：原 `算法性质.md`。对前16位有效，后面的更麻烦，暂未接触。

对于AES的CBC模式而言，我们有：
`old_p = old_iv^Dk(c)`
`new_p = new_iv^Dk(c)`

求`new_p`，我们现在有个情况是`old_iv`可以变成`new_iv`，而且最终程序会执行`old_iv^Dk(c)`
其中`p`指`plain text`, `iv`是随机向量，`Dk(c)`是使用Key解密后的密文(根据AES算法性质，直接用key解密后的是被`IV`异或过的密文)`Decrypt(key, cipherText)`
构造
`old_p^old_p^new_p = old_iv^Dk(c)^old_p^new_p`
即
`new_p = old_iv^Dk(c)^old_p^new_p`

我们现在不知道`Dk(c)`，但已知`old_iv`，而算法最后会使用这个`old_iv`去进行`Dk(c)^old_iv`的操作，所以只需要构造出`new_iv = old_iv^old_p^new_p`。

```text
old_iv = cd56fa3c834a9e15a622dd24e461fd34
old_p = 61646d696e3d46616c73653b65787069
new_p = 61646d696e3d547275653b6578706969

即构造出：
new_iv = cd56fa3c834a8c06bf34837af969e434
```

例题：[flipping_cookie (aes.cryptohack.org)](https://aes.cryptohack.org/flipping_cookie/)

## 工具

### `from pwn import xor`

`pwntools` 提供的 `xor()` 函数，可直接对 `bytes`（或 `str`/`int`，短的一方自动循环复用）做异或，常用于上述已知明文恢复密钥的场景。

> 来源：原 `CTF/Web/Python.md` 中的占位小节，此处补一句说明。
