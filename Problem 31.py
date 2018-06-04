from numpy.polynomial import Polynomial as P
import time
start = time.time()
p1 = P([1]*201)
p2 = P([int(i % 2 == 0) for i in range(201)])
p5 = P([int(i % 5 == 0) for i in range(201)])
p10 = P([int(i % 10 == 0) for i in range(201)])
p20 = P([int(i % 20 == 0) for i in range(201)])
p50 = P([int(i % 50 == 0) for i in range(201)])
p100 = P([int(i % 100 == 0) for i in range(201)])
p200 = P([int(i % 200 == 0) for i in range(201)])

print((p1*p2*p5*p10*p20*p50*p100*p200).coef[200])
print('solution took %s seconds' %(time.time()-start))