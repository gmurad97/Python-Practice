""" x = int(10)
y = int(10.5)
# z = int("128.64") #error => string->float->int
z = int(float("128.64"))

print(x, y,z) """

""" x = int(10)
y = float(10.5)
z = str("string")

print(type(x))
print(type(y))
print(type(z))
 """