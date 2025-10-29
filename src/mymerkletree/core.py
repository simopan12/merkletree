import hashlib
import math


def merkletree(m,s):
    
    
    
    if isinstance(m, str):
        m = m.encode()
    if isinstance(s, str):
        s = s.encode()
    
    
    if len(m) <= 32:
        return m
    
   
    l = math.ceil(math.log2(len(m)/32))
    

    target_len=(2**l) * 32
    
    m=m+ bytes(target_len - len(m))

    out = b''
    
    num_blocks=2 **(l -1)

    for i in range (num_blocks):

        message_to_hash = m[2*i*32 : 2*i*32 + 2*32]
        

        in_hash = s + message_to_hash
        

        out_hash = hashlib.shake_256(in_hash).digest(32)
        out+=out_hash

        


    return merkletree(out,s)
    


def main():
    
    m="abcdefghijklmnopqrstuvwxyz123456177"
    s="abcdefghijklmnopqrstuvwxyz123456"
    final_hash=merkletree(m,s)
    if len(m) <= 32:
        try:
            print("Final Merkle Tree hash (string):",final_hash.decode())
        except UnicodeDecodeError:
               print("Final Merkle Tree hash (hex):", final_hash.hex())
    else :
          print("Final Merkle Tree hash (hex):", final_hash.hex())
                
    
    

    

# Using the special variable 
# __name__
if __name__=="__main__":
    main()