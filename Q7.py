
multi=[]
for i in range(105,0,-1):
    if i<22:
     continue
    if i%5==0 and i%3!=0:
      multi.append(i)
print(multi)


