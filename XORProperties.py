KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
xor12 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
xor23 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
res =  bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

xored23 = bytes([x ^ y for x, y in zip(KEY1, xor23)])
flag = bytes([x ^ y for x, y in zip(xored23, res)]) 

print("\n KEY1 = ", KEY1)
print("\n KEY2 ^ KEY1 = ", xor12)
print("\n KEY2 ^ KEY3 = ", xor23)
print("\n flag: ", flag.decode())