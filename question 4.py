imfile =open ("r.txt",'r')
question= [x.rstrip()for x in imfile]

c=0
for i in question:
    print(i [:i.index("=")+1])
    
    z=input('enter answer')
    if z==i[i.index("=")+1]:
     c+=1
     
name=input ('enter your name')
print(name,c)
