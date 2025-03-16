'''
Abstract Factory Pattern - 
Components:
- Client code
- Abstract Product (for each product variant) and Abstract Factory (for each product family)
- Concrete Product and Concrete Factory

Pros
- SRP - product creation
- OCP - can add new products
- avoid tight coupling between products and client code
Cons
- complexity increases with more relations and interfaces

Example:
Imagine your client code wants a particular variant of a product family. 
You could specifically define an instance of it. Or better, you can retrieve it through a factory.

Here the product variant is the type of a product line. Eg: chair product has ivory and wooden tyes.

Retrieving through a factory increases abstraction. 
Also, if company decides to make changes in that product variant, your client code doesn't error on compile time due to changed behaviors.
This is because what product variant to return can be controlled by the specific product family factory.

Output:
I am an Ivory Chair
I am a wooden chair
I am an Ivory Table
I am a wooden table
'''

from abc import ABC, abstractmethod

# abstract factory
# furniture store
class AbstractFactory(ABC):
    @abstractmethod
    def create_variant_1():
        pass
    @abstractmethod
    def create_variant_2():
        pass

# chair factory
class ChairFactory(AbstractFactory):
    # Specify numeric variant from abstract factory
    @staticmethod
    def create_variant_1():
        return IvoryChair()
    def create_variant_2():
        return WoodenChair()

# table factory
class TableFactory(AbstractFactory):
    @staticmethod
    def create_variant_1():
        return IvoryTable()
    def create_variant_2():
        return WoodenTable()


# abstract chair product
class AbstractChair(ABC):
    @abstractmethod
    def announce():
        pass
    @abstractmethod
    def has_cushioning():
        pass
    
# ivory chair product
class IvoryChair(AbstractChair):
    def announce(self):
        print("I am an Ivory Chair")
    def has_cushioning():
        print("Ivory chair has cushioning")
        
# wooden chair product
class WoodenChair(AbstractChair):
    def announce(self):
        print("I am a wooden chair")
    def has_cushioning():
        print("Wooden chair doesn't have cushioning")
        
# abstract table product
class AbstractTable(ABC):
    @abstractmethod
    def announce():
        pass
    @abstractmethod
    def weight_limit():
        pass

# ivory table product
class IvoryTable(AbstractTable):
    def announce(self):
        print("I am an Ivory Table")
    def weight_limit(self):
        print("Ivory table weight limit is 50 lbs")
        
# wooden table product
class WoodenTable(AbstractTable):
    def announce(self):
        print("I am a wooden table")
    def weight_limit():
        print("Wooden table weight limit is 100 lbs")

# client code testing
class client_code():
    def __init__(self,factory):
        self.factory=factory
    def test(self):
        # buy variant 1 of product family (based on factory passed)
        variant_1 = self.factory.create_variant_1()
        variant_1.announce()
        # buy variant 2 of product family (based on factory passed)
        variant_2 = self.factory.create_variant_2()
        variant_2.announce()
        
if __name__ == '__main__':
    # chair factory
    client_code(ChairFactory).test()
    # table factory
    client_code(TableFactory).test()
  

