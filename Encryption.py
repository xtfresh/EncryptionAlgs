
def RSAencrypt(message, pubKey, modulus):
    c = 1
    for i in range (0,pubKey):
       c = (c*message)%modulus
       
    print c

def RSAdecrypt(cipherText, privKey, modulus):
    c = 1
    for i in range (0,privKey):
       c = (c*cipherText)%modulus
    print c
RSAencrypt(5,2131,2081819)
RSAdecrypt(1158741,1056451,2081819)

def keySchedAlg(key):
    j = 0
    s = range(256)
    keyLen = len(key)

    for i in range (256): 
        j = (j + s[i] + ord( key[i % len(key)] )) % 256
        s[i], s[j] = s[j], s[i]
   
    return s


        

def RC4encrypt(message, key):
    i = 0
    j = 0
    s = keySchedAlg(key)
    ret = []
    for char in message:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        ret.append(hex(ord(char) ^ s[(s[i] + s[j]) % 256]))
    
    print ''.join(ret).replace("0x","")

def RC4decrypt(cipherText,key):
    i = 0
    j = 0
    s = keySchedAlg(key)
    ret = []
    for char in cipherText:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        ret.append(hex(ord(char) ^ s[(s[i] + s[j]) % 256]))
    print ''.join(ret).replace("0x","")


RC4encrypt("Attack at dawn", "This is a test")
RC4decrypt("10989df4d6c9d019d45d584c3f2539955c","51921")

