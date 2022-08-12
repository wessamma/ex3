# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


######### Task 1 #########
'''
c = 3

while c!=0:
    a = input ('Enter number :')
    a = int(a)
    if a%2 == 0: 
      print('even number')
    else:
      print('odd number')

    c-=1

'''
######### Task 2  #############
       
'''
print('Task 2')

a = input('Enter number of argument in range() function :')
a = int(a)
if a == 1:
  r1 = input('Enter stopping number')
  r1 = int(r1)
  for x in range(r1) :
    print(x)

elif a == 2 :
  r1 = input('Enter starting number :')
  r2 = input ('Enter stopping number :')
  r1 = int(r1)
  r2 = int(r2)
  for x in range(r1,r2) :
    print(x)


elif a == 3 :
  r1 = input('Enter starting number :')
  r2 = input ('Enter stopping number :')
  step = input('Enter step :')
  r1 = int(r1)
  r2 = int(r2)
  step = int(step)

  for x in range(r1,r2,step) :
    print(x)
  
else :
  print ('Error')  

'''


##########  Task 3  ###########


'''
print( 'Task 3')

a = input ('Enter number :')
a = int(a)

for x in range(2,a+1) :
    if a % x == 0 :
      print (x)
  

'''

##############  Task 4 ###########
'''
print ( 'Task 3')

a = input('Enter number ')
a =  int(a)
c = 1
for x in range (2,a) :
  if a % x == 0 :
    c = 0
    break 
if c == 0 :
  print (a,'  is not a prime number')
else :
  print (a,'  is  a prime number')

'''


########### Task 5 ############



'''

print ('Task 5')

for x in range (101) :

  if x % 3 == 0 and x % 5 == 0 :
    print ('FizzBuzz')
    continue
  elif x % 3 == 0 :
    print ('Fizz')
    continue
  elif x % 5 == 0 :
    print ('Buzz')
    continue
  else :
    print (x)

'''


##############   Task 6 #############

'''

print ('Task 6')


for x in range (1000,2001) :

  if x % 7 == 0 and x % 5 != 0 :

    print (x)

'''    












