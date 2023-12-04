d1 = 100000000000000
d2 = 0.001
print(f'd1: {d1}')
print(f'd2: {d2}')
print(f'd1+d2: {d1+d2}')
print()

result = d1
for i in range(10):
  result += d2
  print(f'{i}, {result}')
print(f'result: {result}')
print()

result = 0
for i in range(10):
  result += d2
  print(f'{i}, {result}')
result += d1
print(f'result: {result}')
