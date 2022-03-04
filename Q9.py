#for i in range(5):
# for j in range(4):
#     print(' '*(4-j)+'*'*5+'\t')
#     if j==4:
#       break


for j in range(5):
    if j==0 or j==4:
     print(' '*(4-j)+'*'*5+'\t')
    else:
     print(' '*(4-j)+'*'+' '*3+'*''\t')
