num = int(input("Enter +ve integer: "))
a = num
reverse = 0
while num > 0:
  digit = num % 10
  reverse = reverse * 10 + digit
  num = num // 10
if a is reverse:
  print(f"{a} is a palindrome")
else:
  print(f"{a} is not a palindrome")