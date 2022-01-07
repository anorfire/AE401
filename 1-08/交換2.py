A=10
B=25
C=31
T=0
#-------------------#
while C>A or B>A:
    if A<B:
        T=A
        A=B
        B=T
    if B<C:
        T=B
        B=C
        C=T
print(A,B,C)
