import sys
a='ACGT'
z=open(sys.argv[1],'rU')
b=dict(map(lambda x:(x,0),a))
for x in z:
 if x[0]=='>': continue
 jj = filter(lambda xx:xx in a,x)
 for j in jj: b[j]+=1
print(b)

