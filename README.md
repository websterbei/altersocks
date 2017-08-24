# altersocks
Alternative to shadowsocks


## Handshake:
Server:
+---------+---------+
| NMETHOD | METHODS |
+---------+---------+
|         |         |
+---------+---------+

Client:
+------+  
|METHOD|  
+------+  
|      |  
+------+

+------+------+
| UNAME| PWD  |
+------+------+
|      |      |
+------+------+


## Connection Request:
### IPV4 support only
+--------+----------+----------+  
| CMD    | DST.ADDR | DST.PORT |  
+--------+----------+----------+  
|        |          |          |  
+--------+----------+----------+  