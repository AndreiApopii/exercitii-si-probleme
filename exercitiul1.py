n1=int(input("dati numarul elevului"))
n2=int(input("dati numarul elevului"))
n3=int(input("dati numarul elevului"))
p1=int(input("dati punctajul primului elev"))
p2=int(input("dati punctajul elevului doi"))
p3=int(input("dati puctajul elevului trei"))
if(p1>p2)and(p1>p3):
    print(n1)
if(p2>p1)and(p2>p3):
    print(n2)
if(p3>p1)and(p3>p2):
    print(n3)
if(p1==p2)and(p1>p3)and(p2>p3):
    print(n1 and n2)
if(p1==p3)and(p1>p2)and(p3>p2):
    print(n1 and n2)
if(p2==p3)and(p2>p1)and(p3>p1):
    print(n2 and n3)