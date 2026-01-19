import colorama
import pandas as pd

from users import Cashier, Customer
from products import Product

from util import CSVFileManager

class Order:

  def __init__(self, cashier:Cashier, customer:Customer):
    self.cashier = cashier
    self.customer = customer
    self.products = []


  def add(self, product : Product) -> bool:
    """
    Afegeix un producte a la comanda
    Args:
        product (Product): Producte a afegir
    Returns:
        bool: True si s'ha afegit correctament, False en cas contrari
    """
    self.products.append(product)
    return True


  def save(self) -> bool:
    """
    Guarda la comanda en un fitxer CSV
    """
    try:
      # preparem les dades per a guardar  
      
      data = {
          "cashier_dni": [self.cashier.dni],
          "customer_dni": [self.customer.dni],
          "datetime": [pd.Timestamp.now()],
          "total": [f"{self.calculateTotal():.2f}"]
      }

      # creem el DataFrame
      df = pd.DataFrame(data)

      # guardem el DataFrame en un fitxer CSV
      file_manager = CSVFileManager("data/orders.csv")
      if not file_manager.write(df):
          return False

      return True
    except Exception as e:
      print(f"Error en guardar la comanda: {e}")
      return False



  def calculateTotal(self) -> float:
    """
    Calcula el preu total de la comanda
    Returns:
        float: Preu total
    """
    total= 0
    for product in self.products:
      total += product.price
    return total
  

  def show(self):
    """
    Mostra la informació de la comanda
    """
    # definim colors que aplicarem de forma alterna a les línies de productes
    zebbra_colors ={
          1: colorama.Fore.YELLOW,
          2: colorama.Fore.RED
    }
    
    print("Hola : "+self.customer.describe())
    print("Atès per : "+self.cashier.describe() + "\n")
    
    for index, product in enumerate(self.products, start=1):
            color = zebbra_colors[(index % 2) + 1] # calculem el color segons l'índex
            print(color + f"{index}: " + product.describe() + colorama.Style.RESET_ALL)
    
    total= self.calculateTotal()
    # com total es un float el formatem a 2 decimals
    print(f"\nImport Total: {colorama.Fore.GREEN}{total:.2f}{colorama.Style.RESET_ALL}€")
