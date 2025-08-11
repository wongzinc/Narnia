![alt text](image.png)

![alt text](image-3.png)
```gdb
set disassembly-flavor intel
b *0x080491df
```

![alt text](image-5.png)
可以看出第一個是blah 的地址，第三個是return address

![alt text](image-7.png)
我們發現 0xffffd650 -> 0xffffd640
blah 的 address 每增加一個byte , 就會減少一個byte


**calculate blah_address**
![alt text](image-8.png)
0xffffd65e - blah_address(4bytes) - junk(4bytes) - ret_addr(4bytes) - shellcode(33bytes) 

blah_address = 0xffffd631
ret_address = blah_address+ fill_bytes(20bytes) + blah_addr(4bytes) + junk(4bytes) + ret_addr(4bytes) = 0xffffd651


![alt text](image-2.png)
whoami: 1FFD4HnU4K