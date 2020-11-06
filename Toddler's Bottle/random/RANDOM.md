# Pwnable.kr : Random

The rand() function can be exploited if not used with a proper seed value. The exploit.c program outputs value of rand() with the default seed value of 1 **(1804289383)**. This when XORed with 0xdeadbeef **(3735928559)** gives us the value of the key **(3039230856)**.
