t,ke=raw_input().split()
t=int(t)
ke=int(ke)
for num in range(t,ke+ 1):
   
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print num,
