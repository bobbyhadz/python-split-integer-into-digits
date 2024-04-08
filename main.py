# Split an integer into digits in Python

an_int = 13579

list_of_digits = [int(x) for x in str(an_int)]

print(list_of_digits)  # 👉️ [1, 3, 5, 7, 9]