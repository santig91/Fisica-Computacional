import sys
import operator
from pprint import pprint

if(len(sys.argv)>1):
    print "Abriendo " + sys.argv[1]
else:
    print "Debes indicar el nombre del archivo"

f=open(sys.argv[1],"r")
parte=f.read()

a=parte.count('a')
b=parte.count('b')
c=parte.count('c')
d=parte.count('d')
e=parte.count('e')
f=parte.count('f')
g=parte.count('g')
h=parte.count('h')
i=parte.count('i')
j=parte.count('j')
k=parte.count('k')
l=parte.count('l')
m=parte.count('m')
n=parte.count('n')
o=parte.count('o')
p=parte.count('p')
q=parte.count('q')
r=parte.count('r')
s=parte.count('s')
t=parte.count('t')
u=parte.count('u')
v=parte.count('v')
w=parte.count('w')
x=parte.count('x')
y=parte.count('y')
z=parte.count('z')
cero=parte.count('0')
uno=parte.count('1')
dos=parte.count('2')
tres=parte.count('3')
cuatro=parte.count('4')
cinco=parte.count('5')
seis=parte.count('6')
siete=parte.count('7')
ocho=parte.count('8')
nueve=parte.count('9')
todo=a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z+cero+uno+dos+tres+cuatro+cinco+seis+siete+ocho+nueve
ap=(float(a)/float(todo))*100
bp=(float(b)/float(todo))*100
cp=(float(c)/float(todo))*100
dp=(float(d)/float(todo))*100
ep=(float(e)/float(todo))*100
fp=(float(f)/float(todo))*100
gp=(float(g)/float(todo))*100
hp=(float(h)/float(todo))*100
ip=(float(i)/float(todo))*100
jp=(float(j)/float(todo))*100
kp=(float(k)/float(todo))*100
lp=(float(l)/float(todo))*100
mp=(float(m)/float(todo))*100
np=(float(n)/float(todo))*100
op=(float(o)/float(todo))*100
pp=(float(p)/float(todo))*100
qp=(float(q)/float(todo))*100
rp=(float(r)/float(todo))*100
sp=(float(s)/float(todo))*100
tp=(float(t)/float(todo))*100
up=(float(u)/float(todo))*100
vp=(float(v)/float(todo))*100
wp=(float(w)/float(todo))*100
xp=(float(x)/float(todo))*100
yp=(float(y)/float(todo))*100
zp=(float(z)/float(todo))*100
cerop=(float(cero)/float(todo))*100
unop=(float(uno)/float(todo))*100
dosp=(float(dos)/float(todo))*100
tresp=(float(tres)/float(todo))*100
cuatrop=(float(cuatro)/float(todo))*100
cincop=(float(cinco)/float(todo))*100
seisp=(float(seis)/float(todo))*100
sietep=(float(siete)/float(todo))*100
ochop=(float(ocho)/float(todo))*100
nuevep=(float(nueve)/float(todo))*100



dict={'a':ap,'b':bp,'c':cp,'d':dp,'e':ep,'f':fp,'g':gp,'h':hp,'i':ip,'j':jp,'k':kp,'l':lp,'m':mp,'n':np,'o':op,'p':pp,'q':qp,'r':rp,'s':sp,'t':tp,'u':up,'v':vp,'w':wp,'x':xp,'y':yp,'z':zp,'cero':cerop,'uno':unop,'dos':dosp,'tres':tresp,'cuatro':cuatrop,'cinco':cincop,'seis':seisp,'siete':sietep,'ocho':ochop,'nueve':nuevep}

sorted_dict=sorted(dict.iteritems(), key=operator.itemgetter(1))

f3=open('frecuencias_'+sys.argv[1],'w')
f3.write(str(sorted_dict[35])+"%"+'\n')
f3.write(str(sorted_dict[34])+"%"+'\n')
f3.write(str(sorted_dict[33])+"%"+'\n')
f3.write(str(sorted_dict[32])+"%"+'\n')
f3.write(str(sorted_dict[31])+"%"+'\n')
f3.write(str(sorted_dict[30])+"%"+'\n')
f3.write(str(sorted_dict[29])+"%"+'\n')
f3.write(str(sorted_dict[28])+"%"+'\n')
f3.write(str(sorted_dict[27])+"%"+'\n')
f3.write(str(sorted_dict[26])+"%"+'\n')
f3.write(str(sorted_dict[25])+"%"+'\n')
f3.write(str(sorted_dict[24])+"%"+'\n')
f3.write(str(sorted_dict[23])+"%"+'\n')
f3.write(str(sorted_dict[22])+"%"+'\n')
f3.write(str(sorted_dict[21])+"%"+'\n')
f3.write(str(sorted_dict[20])+"%"+'\n')
f3.write(str(sorted_dict[19])+"%"+'\n')
f3.write(str(sorted_dict[18])+"%"+'\n')
f3.write(str(sorted_dict[17])+"%"+'\n')
f3.write(str(sorted_dict[16])+"%"+'\n')
f3.write(str(sorted_dict[15])+"%"+'\n')
f3.write(str(sorted_dict[14])+"%"+'\n')
f3.write(str(sorted_dict[13])+"%"+'\n')
f3.write(str(sorted_dict[12])+"%"+'\n')
f3.write(str(sorted_dict[11])+"%"+'\n')
f3.write(str(sorted_dict[10])+"%"+'\n')
f3.write(str(sorted_dict[9])+"%"+'\n')
f3.write(str(sorted_dict[8])+"%"+'\n')
f3.write(str(sorted_dict[7])+"%"+'\n')
f3.write(str(sorted_dict[6])+"%"+'\n')
f3.write(str(sorted_dict[5])+"%"+'\n')
f3.write(str(sorted_dict[4])+"%"+'\n')
f3.write(str(sorted_dict[3])+"%"+'\n')
f3.write(str(sorted_dict[2])+"%"+'\n')
f3.write(str(sorted_dict[1])+"%"+'\n')
f3.write(str(sorted_dict[0])+"%"+'\n')

