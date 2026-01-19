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
    Clase que representa un usuari tipus caixer
    Attributes:
        dni (str): DNI
        name (str): nom
        age (int): edat
        timetable (str): horari
        salary (float): salari
  """

  def __init__(self, dni:str, name:str, age:int, timetable:str, salary:float):
    super().__init__(dni,name,age)
    self.timetable = timetable
    self.salary = salary
 

  def describe(self)-> str:
    """
    Returns: str: descripció d'un usuari tipus caixer
    """
    return f"Cashier - Nom: {self.name}, DNI: {self.dni}, Horari: {self.timetable}, Salari: {self.salary}"



class Customer(User):
  """
    Clase que representa un usuari tipus client
    Attributes:
        dni (str): DNI
        name (str): nom
        age (int): edat
        email (str): email
        postalcode (str): codi postal
  """

  def __init__(self, dni:str, name:str, age:int, email:str, postalcode:str):
    super().__init__(dni,name,age)
    self.email = email
    self.postalcode = postalcode

  def describe(self) -> str:
    """
    Returns: str: descripció d'un usuari tipus client
    """
    return f"Customer - Nom: {self.name}, DNI: {self.dni}, Edat: {self.age}, Email: {self.email}, Codi Postal: {self.postalcode}"