from abc import ABC, abstractmethod
from users import Cashier, Customer
from products.product import Hamburger, Soda, Drink, HappyMeal

class Converter(ABC):
  """
  Classe abstracta que defineix el mètode convert 
  per convertir un DataFrame en una llista d'objectes
  """


  @abstractmethod
  def convert(self, dataFrame, *args) -> list:
    pass
  

  def print(self, objects_list) -> None:
    """
    Imprimeix la descripció dels objectes passats com a paràmetre
    Args:
        objects_list (list): llista d'objectes a imprimir
    Returns: 
      None
    """

    for obj in objects_list:
      print(obj.describe())



class CashierConverter(Converter):

  def convert(self, dataFrame, *args) -> list:
    """ 
    Converteix un DataFrame en una llista d'objectes Caixers 
    Args:
        dataFrame (DataFrame): DataFrame amb les dades dels caixers
    Returns:
        list: llista d'objectes Caixers
    """

    data_list = []
    for row in dataFrame.itertuples(): # itertuples té millor rendiment que iterrows
      cashier = Cashier(
        dni= row.dni,
        name= row.name,
        age= row.age,
        timeTable= row.timeTable,
        salary= row.salary
      )
      data_list.append(cashier)
    return data_list



class CustomerConverter(Converter):
  
  def convert(self, dataFrame, *args) -> list:
    """ 
    Converteix un DataFrame en una llista d'objectes Clients 
    Args:
        dataFrame (DataFrame): DataFrame amb les dades dels clients
    Returns:
        list: llista d'objectes Clients
    """

    data_list = []
    for row in dataFrame.itertuples():
      customer = Customer(
        dni= row.dni,
        name= row.name,
        age= row.age,
        email= row.email,
        postalCode= row.postalCode
      )
      data_list.append(customer)
    return data_list
  
  

class ProductConverter(Converter):
  
  def convert(self, dataFrame, product_type:str) -> list:
    """ 
    Converteix un DataFrame en una llista d'objectes Productes
    Args:
        dataFrame (DataFrame): DataFrame amb les dades dels productes
        tipus de producte (str): tipus de producte a convertir
    Returns:
        list: llista d'objectes Productes
    """
    
    # validem que el tipus sigui correcte
    if product_type not in ["Hamburger", "Soda", "Drink", "HappyMeal"]:
      raise ValueError(f"Tipus de producte desconegut: {product_type}")
    
    """
      Definim un diccionari per mapejar els tipus i la classe.
      D'aquesta manera evitem if-else i el codi es molt més net i escalable
      ja que podem afegir nous tipus de productes fàcilment.
      
    """
    product_class = {
      "Hamburger": Hamburger,
      "Soda": Soda,
      "Drink": Drink,
      "HappyMeal": HappyMeal
    }

    products_list = []
    for row in dataFrame.itertuples():
      product = product_class[product_type](
        id= row.id,
        name= row.name,
        price= row.price
      )
      products_list.append(product)
    
    return products_list