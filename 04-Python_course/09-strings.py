from cmath import pi


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
  print("Yes, 'free' is present.")
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

print(a.upper())
print(a.lower())

a = " Hello Hola, World! "
print(a.strip()) # returns "Hello, World!"
print(a.replace("H", "J").strip())
print(a.strip().split(",")) # returns ['Hello', ' World!']

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

print(a.center(120))
print(a.count('l'))
print(a.find('l'))
print(a.find('javi'))
print(a.index('l'))
print(a.strip().join("123456"))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"

print(bool("Hello"))
print(bool(15 < 6))

def myFunction() :
  return True

print(myFunction())

print(15 // 2)
print(pi)

thislist = ["apple", "banana", "cherry"]
print(len(thislist[0][0]))

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = ["apple", "banana", "cherry"]
i = -1
while i += 1 < len(thislist):
  print(thislist[i])
  i += 1