num_1= float(input('Please Enter First Number= '))
num_2= float(input('Please Enter Second Number= '))
num_3= float(input('Please Enter Third Number= '))
if num_1> num_2:
    max= num_1
    min= num_2
else:
    max= num_2
    min= num_1
if max> num_3:
    if min> num_3:
        min=num_3
else:
    max=num_3
print('max is', max)
print('min is', min)