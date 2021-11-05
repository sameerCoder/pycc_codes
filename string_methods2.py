## String function Method 2
## PPT number 23.

str1= "hello world  "
print("original string:",str1)
length=len(str1)
print("lenght of string:",length)
# zfill
print("str1.zfill(27):",str1.zfill(27))

# count
print("str1.count('o',0,len(str1)):",str1.count('o',0,len(str1)))


# Find
print("str1.find('hello',0,12)",str1.find('hello',0,12))
print("str1.find('world',0,12)",str1.find('world',0,12))
print("str1.find('wii',0,12)",str1.find('wii',0,12))
print("str1.find('sameer',0,12)",str1.find('sameer',0,12))


# join operation.

list1=['a','b','c']
s="_"
seq=("PY","Ty","Ky")
path=("c:","user","Downloads")
p="/"
print("s.join(seq)",s.join(seq))

print("s.join(list1)",s.join(list1))
print("Total path:",p.join(path))

strpy="Python is great programming language."

print("strpy.startswith('Python',0,28)",strpy.startswith("Python",0,28))
print("strpy.startswith('Pn',0,28)",strpy.startswith("Pn",0,28))

print("strpy.endswith('on',0,6)",strpy.endswith("on",0,6))
print("strpy.endswith('Py',0,6)",strpy.endswith("Py",0,6))






