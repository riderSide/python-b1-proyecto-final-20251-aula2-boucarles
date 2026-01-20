import pandas as pd
from pathlib import Path

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
    Returns:
      pd.DataFrame: El DataFrame llegit des del fitxer CSV.
    Raises:
      FileNotFoundError: Si el fitxer no es troba a la ruta especificada
    """

    try:
      return pd.read_csv(self.path)
    except FileNotFoundError:
      raise FileNotFoundError(f"Error: No s'ha trobat el fitxer a la ruta: {self.path}")
    except Exception as e:
      raise Exception(f"Error: No s'ha pogut llegir fitxer CSV: {e}")
    
   
  def write(self,dataFrame) -> bool:
    """
    Afegeix un DataFrame al fitxer CSV.
    Args:
      dataFrame (DataFrame): El DataFrame que es vol afegir.
    Returns:
      bool: True si l'escriptura és exitosa, False en cas contrari.
    Raises:
      Exception: Si hi ha un error en escriure el fitxer CSV.
    """
    try:
      # convertim la cadena del path a un objecte tipus Path
      path= Path(self.path)
      
      # fem servir el mode 'a' per afegit
      # header = not path.exists() per escriure l'encapçalament només si el fitxer no existeix
      dataFrame.to_csv(path, index=False, mode='a', header= not path.exists())
      return True
    except Exception as e:
      print(f"Error en escriure el fitxer CSV: {e}")
      return False