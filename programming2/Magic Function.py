class Customer:
    
    def __init__(self, name, balance=5):  
        self.name = name
        self.balance = balance
        print("The init method was called")
        
    def __str__(self):
        return 'Customer: ' + str(self.name) + ', balance: ' + str(self.balance)
    
    def __repr__(self):
        return f"Customer(name={self.name}, balance={self.balance})"
    
    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance
    
    def __le__(self, other):
        return self.balance <= other.balance
    
    def __gt__(self, other):
        return self.balance > other.balance
    
    def __ge__(self, other):
        return self.balance >= other.balance
    
    def __add__(self, other):
        return Customer(self.name + ' & ' + other.name, self.balance + other.balance)
    
    def __sub__(self, other):
        return Customer(self.name + ' & ' + other.name, self.balance - other.balance)

customer1 = Customer("Alice", 10)
customer2 = Customer("Bob", 7)
customer3 = Customer("Charlie", 10)


print(str(customer1))


print(repr(customer2)) 

print(customer1 == customer2)  
print(customer1 == customer3)  

print(customer2 < customer1)  
print(customer1 < customer3)   

print(customer2 <= customer1)  
print(customer1 <= customer3)  

print(customer1 > customer2)
print(customer2 > customer3)  

print(customer1 >= customer2)  
print(customer1 >= customer3)  

customer4 = customer1 + customer2  
print(customer4) 

customer5 = customer1 - customer2  
print(customer5)  



class Customer:
    
    def	__init__(self, name, balance=20):  
        self.name = name
        self.balance = balance
        print("The init method was called")
        
    def __add__(self, other): 
        return Customer("Test_Customer",self.balance + other)

    def __sub__(self, other): 
        return Customer("Test_Customer",self.balance - other)

c1 = Customer("Ali") 
print(c1.balance) 
print(str(c1))

c2 = c1 + 30
c3 = c1 - 3
print(c2.balance , c3.balance)