from Crypto.PublicKey import RSA

# import RSA key from the file
with open('privacy_enhanced_mail.pem', 'r') as f:
    privatekeyData = f.read()

privatekey = RSA.importKey(privatekeyData)

print(privatekey.d)