class calculator:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        if y!=0:
            return x/y
        else:
            print("Cannot divide by zero")
x=int(input("Enter one number:"))
y=int(input("Enter another number:"))
cal=calculator()
summ=cal.add(x,y)
dif=cal.sub(x,y)
pro=cal.mul(x,y)
quo=cal.div(x,y)
print("The sum is:",summ)
print("The difference is:",dif)
print("The product is:",pro)
print("The quotient is:",quo)
