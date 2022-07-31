
def calc(a,b,c):
   if c=="sum":
     return a+b
   if c=="subtract":
        return a-b
   if c=="multiply":
      return a*b
   if c=="divide":
        return a/b

d=calc(232,11,"divide")
print(d)
e=calc(32,78,"multiply")
print(e)
k=calc(67,90,"sum")
print(k)
h=calc(456,897,"subtract")
print(h)