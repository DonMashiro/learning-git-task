numbers = list(range(0, 101))
cube = []
for number in numbers:
  if number % 5 == 0:
    cube.append(number**3)
print(cube)