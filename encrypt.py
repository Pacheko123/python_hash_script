import sys
import hashlib
key= raw_input("Enter your hashing key")
path = raw_input("Enter the path of the file to encrypt\n")
confirm = raw_input("The file  is going to be encrypted, are you sure?(NO/YES)")
confirm = confirm.lower()
if(confirm=="yes"):
   with open(path,'r') as encrypt:
        content = encrypt.read()
        print(content)
        m=hashlib.sha256()
        m.update(content)
        #print( m.digest())
        encrypt.close()
        encrypt.open(path,'w')
        encrypt.write(m.digest())
        encrypt.close()


elif(confirm == "NO") or (confirm=="no"):
    sys.exit()
else:
    print("Invalid input")


