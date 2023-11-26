terms = int(input("Put the number of terms: "))
a = 7
b = 3
print(a)
for i in range(1, terms):
  c = a + b
  print(c)
  a = b
  b = c