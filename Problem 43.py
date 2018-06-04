import itertools

pandigital = []

digits = [i for i in range(10)]


def compatible(a,b):
    if a[len(a)-2:] == b[:2] and len(set(a+b)) +2 == len(set(a)) + len(set(b)):
        return True
    else:
        return False




mult17 = [str(i*17).zfill(3) for i in range(59) if len(str(i*17)) == len(list(set(str(i*17))))]

mult13 = [str(i*13).zfill(3) for i in range(1000//13) if len(str(i*13)) == len(list(set(str(i*13))))]

mult11 = [str(i*11).zfill(3) for i in range(1000//11) if len(str(i*11)) == len(list(set(str(i*11))))]

mult7 = [str(i*7).zfill(3) for i in range(1000//7) if len(str(i*7)) == len(list(set(str(i*7))))]

mult5 = [str(i*5).zfill(3) for i in range(1000//5) if len(str(i*5)) == len(list(set(str(i*5))))]


for y in mult5:
    for z in mult7:
        for a in mult11:
            for b in mult13:
                for c in mult17:
                    if compatible(y,z) and compatible(y+z,a) and compatible(y+z+a,b) and compatible(y+z+a+b,c):
                        print(y+z[2]+a[2]+b[2]+c[2])

# seems like the number has to end in either 357289 or 952867...

# xx60357289, xx30952867, xx06357289