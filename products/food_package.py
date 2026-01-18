from abc import ABC, abstractmethod


class FoodPackage (ABC): 

  @abstractmethod
  def pack(self)  -> str:
    """
    Les implementacions han de retorna el tipus de contenidor.
    """
    pass
  
  
  @abstractmethod
  def material(self) -> str:
    """
    Les implementacions han de retorna el material del contenidor.
    """
    pass
  

  def describe(self):
    """
    Métode que descriu el tipus i material del contenidor.
    """
    return f"Embolcall: {self.pack()} , Material: {self.material()}"    
    



class Wrapping(FoodPackage):  

  def pack(self) -> str:
      return "Food wrap paper"
  
  def material(self) -> str:
      return "Paper"



class Bottle(FoodPackage):  
  
  def pack(self) -> str:
      return "Bottle"
  

  def material(self) -> str:
    return "Plastic"



class Glass(FoodPackage):

  def pack(self) -> str:
    return "Glass"
  

  def material(self) -> str:
    return "Cardboard"



class Box(FoodPackage):

  def pack(self) -> str:
    return "Box"
  

  def material(self) -> str:
    return "Cardboard"