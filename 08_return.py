sum=0
for i in range(1,11):
  sum=sum+i

print(sum)

def sum_range():
  sum=0
  for i in range(1,10):
    sum+=i
  print(sum)

sum_range()

def sum_range2(min,max):
  sum=0
  for i in range(min,max):
    sum+=i
  return sum

print(sum_range2(1,10))