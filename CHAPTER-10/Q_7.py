# 21 no q form the bank
class Calculator:
    def square(self,number):
        return number**2
    def cube(self,number):
        return number**3
n=int(input("Enter your number:"))
suss=Calculator()
print("Square:", suss.square(n))
print("Cube:", suss.cube(n))