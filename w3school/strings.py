""" a = """ """
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it
"""
""" 
a = "Hello, World!" """

""" print(a[0])
print(a[1])
print(a[2])
"""
""" 
for idx in a:
    print(idx) """

""" print(len(a)) """

""" if "hello" in a.lower():
    print("Found!")
else:
    print("Not Found!") """

""" if "hello" in a.lower():
    print("Found!")
elif "hello" not in a.lower():
    print("Not Found!") """

""" b = "   Hello, World   " """
# print(b[2:5]) # llo
# print(b[:5]) #Hello
# print(b[2:]) #llo, World
# print(b[-5:-2]) #Wor
# print(b[1::2]) #Hello,Wprld => el

# print(b.upper())
# print(b.lower())
# print(b.strip()) #trim
# print(b.lstrip()) #trim left
# print(b.rstrip()) #trim right

b = "Hello, World"
# print(b.replace("H","J"))
# print("-".join(b.split(",")))
print("<=>".join(b.split(",")))