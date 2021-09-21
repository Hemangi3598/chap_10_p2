# wapp to accept as input integers
# print if the number is even or odd

print("welcome")
try:
	num = int(input(" enter an integer "))
	if num % 2 == 0:
		msg = "even"
	else:
		msg = "odd"
	print(msg)
except ValueError:
	print("integers only ")
print("bye")

# try with single except