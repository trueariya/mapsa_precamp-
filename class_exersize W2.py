def power(num:int):
 # k=0
  #num=input('number=')
  k=num%2
  quotient= (num - k) // 2
  counter=0
  while quotient>=1:
      quotient= quotient // 2
      counter+=1
  baghimande=num-2**counter
  print('baghimande=',baghimande,"tedade 2=",counter)

power(21)



