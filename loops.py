# while loops examples
i = 1
while i <= 10:
  print(i) 
  i = i + 1

# nested while loops
i = 1
while i <= 3:
  j = 1
  while j <= 5:
    print(i, j)
    j = j + 1
  i = i + 1

#for loop
for i in range(1, 11):
  print(i)

for x in [1,2,3,4,5,6,7,8,9]:
    print(x)

# for loop with step
for i in range(1, 11, 2):
  print(i)


# nested for loop
for i in range(1, 4):
  for j in range(1, 6):
    print(i, j)


# for loop with break statement
for i in range(1, 11):
  if i == 5:
    break
  print(i)

# for loop with continue statement
for i in range(1, 11):
  if i % 2 == 0:
    continue
  print(i)

# for loop with else statement
for i in range(1, 11):
  print(i)
else:
  print("Loop completed")

# for loop with else statement in nested loop
for i in range(1, 4):
  for j in range(1, 6):
    if j == 3:
      break
    print(i, j)
  else:
    print("Inner loop completed")


# for loop with else statement in nested loop with break statement
for i in range(1, 4):
  for j in range(1, 6):
    if j == 3:
      break
    print(i, j)
  else:
    print("Inner loop completed")
    

# for loop with else statement in nested loop with continue statement
for i in range(1, 4):
  for j in range(1, 6):
    if j == 3:
      continue
    print(i, j)
  else:
    print("Inner loop completed")


# for loop with else statement in nested loop with break and continue statement
for i in range(1, 4):
  for j in range(1, 6):
    if j == 3:
      continue
    print(i, j)
  else:
    print("Inner loop completed")


