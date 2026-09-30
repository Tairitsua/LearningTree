# RSA与数论

> 合并自 `RSA.md`（原工具/公式空壳）、`RSA理论知识.md`（数论主体）、`算法性质.md` 的数论部分（`GCD`/欧几里得/扩欧，取两文件并集去重）与 `CTF.md` 的 `RSA-crack` 词条。
> `算法性质.md` 的 XOR/CBC 翻转攻击部分独立为 [XOR与CBC攻击](XOR与CBC攻击.md)。
> 原稿中 2 处图片嵌入的附件已丢失，以文字备注保留痕迹。

## 数论基础

### 术语

`number theory` 数论
`elliptic curves` 椭圆曲线
`algebraic geometry` 代数几何
`group theory` 群论

### 逆元

> 如果 ax≡1（mod M)，就称x为在模M下 a的 逆元
> 简单地说，如果一个数x满足 ax%M=1，那么x就称为在模M下 a的逆元！

### 模运算

模运算与基本四则运算有些相似，但是除法除外。其规则如下：

```text
(a + b) % p = (a % p + b % p) % p
(a - b) % p = (a % p - b % p) % p
(a * b) % p = (a % p * b % p) % p
a ^ b % p = ((a % p) ^ b) % p
结合律
((a + b) % p + c) = (a + (b + c) % p) % p
((a * b) % p * c) = (a * (b * c) % p) % p
交换律
(a + b) % p = (b + a) % p
(a * b) % p = (b * a) % p
分配律
(a + b) % p = (a % p + b % p) % p
((a + b) % p * c) % p = ((a * c) % p + (b * c) % p
重要定理
若 a ≡ b (mod p)，则对于任意的 c，都有(a + c) ≡ (b + c) (mod p)
若 a ≡ b (mod p)，则对于任意的 c，都有(a * c) ≡ (b * c) (mod p)
若 a ≡ b (mod p)，c ≡ d (mod p)，则
(a + c) ≡ (b + d) (mod p)
(a - c) ≡ (b - d) (mod p)
(a * c) ≡ (b * d) (mod p)
(a / c) ≡ (b / d) (mod p)
```

在模运算下是没有除法运算的，比如:

$$\begin{aligned}
a * b \equiv c \ mod \ n  \\
c * \frac{1}{a} \equiv b \mod\ n 是错误的 \\
c * a^{-1} \equiv \ b \mod\ n 才是对的
\end{aligned} $$

### 最大公约数（GCD）

> 也称为最大公因子

the largest number which divides two positive integers `(a,b)`
- `gcd(a,b) = 1`则称为两个数互质(coprime integers)
- 两个数都是质数，那他们也肯定互质。如果`a`是质数，而`b<a`，那么它们也互质

#### 欧几里得算法（Euclidean algorithm）

也称为辗转相除法。
1. 如果A=0，则GCD(A,B)=B；
2. 如果B=0，则GCD(A,B)=A；
3. 如果A≠0，B≠0，则A=B∙Q+R，其中Q是B除A的商，R是余数。
4. GCD(A,B)= GCD(B,R)，即A和B的最大公约数等于B和R的最大公约数

```python
def gcd(a,b):
    if b==0:
        return a
    # if a<b:
    #     return gcd(b,a)
    return gcd(b,a%b)
```

### 扩展欧几里得算法（Extended Euclidean algorithm）

> 这也称之为贝祖等式(Bézout's identity)

设
$$ a,b \in Z , d = gcd (a,b )$$
则
$$ \exists x , y \in Z$$
使得
$$ ax + by = gcd(a,b) $$

对于不完全为 0 的非负整数 a，b，`gcd(a,b)` 表示 a，b 的最大公约数，必然存在整数对 x，y ，使得 `gcd(a,b) = ax + by`。
扩展欧几里得算法可以用来计算**模反元素**(也叫模逆元, `modulo multiplicative inverse`)，而模反元素在RSA加密算法中有举足轻重的地位。

> 可以使用`gmpy2.gcdext(a,b)`求解x、y的组合；并使用`x+i*b`的方式进行爆破
> 对于`ax≡1(mod p)`可以化成`ax-kp=1`（k为整数），令k = -k，且a，p互质，那么就可用扩展欧几里得求解。

### 定理速查表

| 定理       | 条件/描述                                                                  | 公式                                                                                                                            |
| -------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 费马小定理    | 对于质数 p，当 a 是一个与 p互质的整数时                                                | a^p-1≡1(mod p)；即可化为a * a^p-2 ≡1(mod p)                                                                                        |
| 欧几里得算法   |                                                                        | gcd(a,b)=gcd(b,a)=gcd(−a,b)=gcd(∣a∣,∣b∣)=gcd(b, a mod b)                                                                      |
| 扩展欧几里得   | 对于不完全为 0 的整数 a，b，gcd（a，b）表示 a，b 的最大公约数，必然存在整数对 x，y ，使得 gcd（a，b）=ax+by。 | gcd（a，b）=ax+by;可以使用gmpy2.gcdext(a,b)求解x、y的组合；并使用`x+i*b`的方式进行爆破；对于ax≡1(mod p)可以化成`ax-kp=1`(k为整数)，令k = -k，且a，p互质，那么就可用上扩展欧几里得了。 |
| 威尔逊定理    | 对于素数p                                                                  | (p-1)!≡-1(mod p)                                                                                                              |
| 欧拉定理     | 若n,a为正整数，且n,a互质                                                        | `a^φ(n)≡1 mod n `                                                                                                             |
| 中国剩余定理   |                                                                        |                                                                                                                               |
| 欧拉准则     | p为素数                                                                   | a^((p-1)/2)  =   {a/p}mod p                                                                                                   |
| 二次剩余定理   | p是素数、a!=kp、存在x，使得x^2 = a mod p ，那么我们称a是模p的二次剩余，记为QR，否则记NR              | QR，{a/p}=1 ；NR {a/p=-1}                                                                                                       |
| 二次剩余定理拓展 | 如果一个数是模p的二次剩余，另外一个不是                                                   | 那么这2个数的积不是模p的二次剩余                                                                                                             |
|          |                                                                        |                                                                                                                               |

### 补充式子

1. a和n互质：`a^(-y) % n = invert(a,n)^y % n`
2. $\phi(p^k*q)=p^(k-1)*(p-1)*(q-1)$
3. $$(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} (b[可正可负])^k$$

### 欧拉函数

> 欧拉函数（Euler's totient function），即phi_n，表示的是小于等于n和n互质的数的个数。特别的，当n是质数时，phi_n = n-1

### 欧拉定理

> 若n,a为正整数，且n,a互质，则：`a^φ(n)≡1 mod n `

### 费马小定理

> 对于质数 p，当 a 是一个与 p互质的整数时有：`a**(p-1)≡1(mod p)`；
> 即可化为`a * a**(p-2) ≡1(mod p)`

### 威尔逊定理

> 对于素数p，`(p-1)!≡-1(mod p)`

### 中国剩余定理

> 「物不知数」问题：有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二。问物几何？

> [图片已丢失：Pasted image 20231106224355]

解题

```python
import gmpy2
from Crypto.Util.number import long_to_bytes

def CRT(k_count, a_result_pre_mod, n_mod):
    n = 1; ans = 0
    for i in range(0, k_count ):
        n = n * n_mod[i]
    for i in range(0, k_count ):
        m = n // n_mod[i]; b = y = 0
        b = gmpy2.invert(m, n_mod[i]) # b * m mod r[i] = 1
        ans = (ans + a_result_pre_mod[i] * m * b % n) % n
    return (ans % n + n) % n
```

### 欧拉准则与二次剩余

> [图片已丢失：Pasted image 20231201154721]

## RSA 原理

$$
m^e \mod n \equiv c
$$

## 工具与攻击

### RSA-crack

RSA解密一把梭

**特征**: RSA题型, 大整数

**测试数据**:

见 [rsa](https://github.com/Leon406/ToolsFx/tree/dev/testdata/ctf/rsa)

### sagemath

数论/RSA 计算常用的数学软件系统。
