import itertools
# there are two options:
# 1) the right angle is at the origin. Easy in this case, we have bound^2 many triangles.
# 2) the right angle is not the origin. Then we must have (P-Q)*P = 0 or (Q-P)*Q = 0

bound = 50

def dot(A, B):
    return sum([A[i]*B[i] for i in range(len(A))])


def dif(A,B):
    return [A[i] - B[i] for i in range(len(A))]

points = [i for i in range(bound+1)]

count = 0
for P in itertools.product(points, repeat=2):
    for Q in itertools.product(points, repeat=2):
        if P != Q and P != (0,0) and Q != (0,0):
            # the idea is that they form a right angle if the dot product of the vectors is zero.
            if dot(dif(P,Q), P) == 0 or dot(dif(Q,P),Q) == 0:
                print(P,Q)
                count += 1

# we double counted, and we add the diagonal
print(count/ 2 + bound**2)