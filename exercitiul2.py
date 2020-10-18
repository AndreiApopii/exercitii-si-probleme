a=int(input("prima latura a triunghiului"))
b=int(input("a doua latura a triunghiului"))
c=int(input("a treia latura a triunghiului"))
if((a<b+c)and(b<a+c)and(c<a+b)):
    print("Da")
else:
    print("Nu")