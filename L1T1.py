#Level 1 Task 1
def reverse(string):
	string = string[::-1]
	return string

s = "COGNIFYZ"
print("The original string is : ", end="")
print(s)
print("The reversed string is : ", end="")
print(reverse(s))

