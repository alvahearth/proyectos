class Employee:
    
    pay_increased = 1.05
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    def apply_raise(self):
        self.pay = int(self.pay * self.pay_increased)
        
        
emp1 = Employee("raul","conumil",4000)

print(emp1.pay)

emp1.apply_raise()

print(emp1.pay)

