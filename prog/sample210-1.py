def mysqrt(c):
  x1, x2 = 100, 0
  for i in range(30):
    x2 = x1 - (x1 * x1 - c) / (2 * x1);
    print(f'{i}: {x2}')
    x1 = x2
  return x2

print('----- mysqrt(2) -----')
print(f'result: {mysqrt(2)}')
print('----- mysqrt(3) -----')
print(f'result: {mysqrt(3)}')
print('----- mysqrt(4) -----')
print(f'result: {mysqrt(4)}')
