import hashlib
import math


def merkletree(m,s):

    if(len(m) <= 32): 
        if(isinstance(m,str)):
            return m
        else:
            return m.hex()

    if(isinstance(m,bytearray) == False): m = bytearray(m,"utf-8")

    if(isinstance(s,bytearray) == False): s = bytearray(s,"utf-8")
        
    
    
    l = math.ceil(math.log(len(m)/32,2))
    

    for i in range(0,pow(2,1)*32 - len(m)):
        m.append(0)

    
    out = bytearray()

    for i in range (0,pow(2,l-1)):

        message_to_hash = m[2*i*32 : 2*i*32 + 2*32]
        #print(message_to_hash)

        in_hash = s + message_to_hash
        #print(in_hash)

        out_hash = hashlib.shake_256(in_hash).digest(32)
        #print(out_hash)

        out = out + out_hash


    return merkletree(out,s)
    


def main():
    
    m="abcdefghijklmnopqrstuvwxyz1234567"
    s="abcdefghijklmnopqrstuvwxyz123456"

    hash1 = merkletree(m,s)
    
    print(hash1)

    

# Using the special variable 
# __name__
if __name__=="__main__":
    main()