from abc import ABC, abstractmethod


class User(ABC):
  """
    Clase abstracta que representa un usuari genèric
    Attributes:
        dni (str): DNI de l'usuari
        name (str): nom de l'usuari
        age (int): edat de l'usuari
  """

  def __init__(self,dni:str,name:str,age:int):
    self.dni = dni
    self.name = name
    self.age = age    


  @abstractmethod
  def describe(self)-> str:
      pass



class Cashier(User): 
  """
    Clase que representa un usuari tipu scaixer
    Attributes:
        dni (str): DNI
        name (str): nom
        age (int): edat
        timeTable (str): horari
        salary (float): salari
  """

  def __init__(self, dni:str, name:str, age:int, timeTable:str, salary:float):
    super().__init__(dni,name,age)
    self.timeTable = timeTable
    self.salary = salary
 

  def describe(self)-> str:
    """
    Returns: str: descripció del caixer
    """
    return f"Cashier - Name: {self.name}, DNI: {self.dni}, Timetable: {self.timeTable}, Salary: {self.salary}."



class Customer(User):
  """
    Clase que representa un usuari tipu client
    Attributes:
        dni (str): DNI
        name (str): nom
        age (int): edat
        email (str): email
        postalCode (str): codi postal
  """

  def __init__(self, dni:str, name:str, age:int, email:str, postalCode:str):
    super().__init__(dni,name,age)
    self.email = email
    self.postalCode = postalCode


  def describe(self) -> str:
    """
    Returns: str: descripció d'un client
    """
    return f"Customer - Name: {self.name}, DNI: {self.dni}, Age: {self.age}, Email: {self.email}, Postal Code: {self.postalCode}"