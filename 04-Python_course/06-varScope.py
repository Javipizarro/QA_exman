x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Global varible in a fucntion

def myfunc():
  global x
  x = "fantastic"

print("Python is " + x)

#The global x only will be declared once the function myfunc() is called
myfunc()

print("Python is " + x)


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

print("Python is " + x)

myfunc()

print("Python is " + x)