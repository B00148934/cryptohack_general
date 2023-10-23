from binascii import unhexlify
import string

def xor(input, key):

    output = b''
    for b in input:
        output += bytes([b ^ key])

    try:
        return output.decode("utf-8")
    except:
        return "bytes cannot be decode"

data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
decoded = unhexlify(data)

print("[-] HEX_DECODE: {}\n".format(decoded))

result = {}
for i in range(256):
    result[i] = (xor(decoded, i))

print("FLAG: {}".format([s for s in result.values() if "crypto" in s]))