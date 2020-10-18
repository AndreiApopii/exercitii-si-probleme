xa=int(input("dati numarul de bile albe mici"))
xr=int(input("dati numarul de bile rosii mici"))
xv=int(input("dati numarul de bile verzi mici"))
ya=int(input("dati numarul de bile albe mari"))
yr=int(input("dati numarul de bile rosii mari"))
yv=int(input("dati numarul de bile verzi mari"))
xt=xa+xr+xv
yt=ya+yr+yv
print("total=",xt+yt,"bile")
if(xt>yt):
    print("bile mici sunt mai multe")
    if(xt<yt):
        print("bile mari sunt mai multe")
        if(xt==yt):
            print("bilele mari si bilele mici sunt egale")
            if((xa+ya>xr+yr)and(xa+ya>yv+yv)):
            print("albe")
            if((xr+yr>xa+ya)and(xr+yr>xv+yv)):
                print("rosii")
                else:
                    print("verzi")