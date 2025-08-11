### 解題思路
一開始以爲是format string vulnerabilites, 結果不是。而且只允許寫4個bytes 到 val。 我一直以爲是deadbeef，怎麽可能能覆寫8個byte, 才發現原來是看錯，其實是0xdeadbeef。 這題只是考驗玩家對於 little-endian與big-endian 的理解罷了

cat /etc/narnia_pass/narnia1: WDcYUTG5ul