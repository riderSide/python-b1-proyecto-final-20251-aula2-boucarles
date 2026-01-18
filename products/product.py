from abc import ABC, abstractmethod
from products.food_package import FoodPackage, Wrapping, Bottle, Glass, Box


class Product(ABC):

    def __init__(self, id:str, name:str, price:float):
      self.id = id
      self.name = name
      self.price = price


    @abstractmethod
    def type(self) -> str:
        pass


    @abstractmethod
    def foodPackage(self)->FoodPackage:
        pass


    def describe(self):
        return f"Product - Type: {self.type()}, Name: {self.name}, Id: {self.id} , Price: {self.price} , {self.foodPackage().describe()}."   



class Hamburger(Product):
    """
    Implementació de la classe Hamburger que hereta de Product.
    Representa una hamburguesa amb el seu tipus i embolcall.
    """

    def __init__(self, id:str, name:str, price:float):
        super().__init__(id, name, price)


    def type(self) -> str:
        return "Hamburguesa"
    

    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        


class Soda(Product):
    """
    Representa una beguda tipus soda.
    """

    def __init__(self, id:str, name:str, price:float):
        super().__init__(id, name, price)


    def type(self) -> str:
        return "Soda"


    def foodPackage(self) -> FoodPackage:
        return Bottle()



class Drink(Product):
    """
    Representa una beguda genèrica.
    """

    def __init__(self, id:str, name:str, price:float):
        super().__init__(id, name, price)

    def type(self) -> str:
        return "Drink"
    
    def foodPackage(self) -> FoodPackage:
        return Glass()



class HappyMeal(Product):
    """
    Representa un Happy Meal.
    """

    def __init__(self, id:str, name:str, price:float):
        super().__init__(id, name, price)

    def type(self) -> str:
        return "Happy Meal"
    
    def foodPackage(self) -> FoodPackage:
        return Box()