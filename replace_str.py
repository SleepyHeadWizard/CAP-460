s = "Hello, World!"
old_char = "o"
new_char = "a"

result = ""

for char in s:
	if char == old_char:
		result += new_char
	else:
		result += char

print(result)