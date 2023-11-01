def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

x = set(range(8 , 23))
y = set()

for i in x:
    if is_prime(i):
       y.add(i)

print(f'x: {x}')
print(f'y: {y}')