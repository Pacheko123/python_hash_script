import sys
import hashlib
path = raw_input("Enter the path of the file to encrypt\n")
confirm = raw_input("The file  is going to be encrypted, are you sure?(NO/YES)")
if(confirm=="YES") or (confirm=="yes"):
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


