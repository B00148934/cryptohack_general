hex_given = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher_str = bytes.fromhex(hex_given)
first_part = "crypto{"
for i in range(len(first_part)):
    print("Key: ", chr(ord(first_part[i])^cipher_str[i]))

#key is myXORkey from the first output
key = "myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkey"
print("Flag: ", ''.join(chr(ord(key[i])^cipher_str[i]) for i in range(len(cipher_str))))