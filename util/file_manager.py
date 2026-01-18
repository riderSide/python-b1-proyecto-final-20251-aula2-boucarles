import pandas as pd

class CSVFileManager:
  """
  Clase per a gestionar la lectura i escriptura de fitxers CSV i
  la seva conversió a DataFrame de pandas.
  Atributs:
    path (str): La ruta del fitxer CSV.
  Mètodes:
    read() -> pd.DataFrame: Llegeix el fitxer CSV i retorna un DataFrame.
    write(dataFrame: pd.DataFrame) -> bool: Escriu un DataFrame al fitxer CSV.
  """

  def __init__(self,path: str):
    self.path = path


  def read(self) -> pd.DataFrame:
    """
    Llegeix el fitxer CSV i retorna un DataFrame.
    Retorna:
      pd.DataFrame: El DataFrame llegit des del fitxer CSV.
    Raises:
      FileNotFoundError: Si el fitxer no es troba a la ruta especificada
    """

    try:
      pd.read_csv(self.path)
      return pd.read_csv(self.path)
    except FileNotFoundError:
      raise FileNotFoundError(f"Error: No s'ha trobat el fitxer a la ruta: {self.path}")
    except Exception as e:
      raise Exception(f"Error: No s'ha pogut llegir fitxer CSV: {e}")
    
   
  def write(self,dataFrame) -> bool:
    """
    Escriu un DataFrame al fitxer CSV.
    Args:
      dataFrame (pd.DataFrame): El DataFrame que es vol escriure.
    Returns:
      bool: True si l'escriptura és exitosa, False en cas contrari.
    Raises:
      Exception: Si hi ha un error en escriure el fitxer CSV.
    """
    try:
      dataFrame.to_csv(self.path, index=False)
      return True
    except Exception as e:
      print(f"Error en escriure el fitxer CSV: {e}")
      return False