import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = (b**2)-(4*a*c)
x1 = int((-b+(d**0.5))/2*a)
x2 = int((-b-(d**0.5))/2*a)
print(str(x1))
print(str(x2))
