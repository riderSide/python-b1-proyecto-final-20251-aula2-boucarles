import os
import time
import colorama


class Drawer:
    """
    Classe per gestionar la visualització a la consola
    """
    def __init__(self, width) -> None:
        if width is None:
            self.width = 60
        else:
            self.width = width


    def clear_screen(self):
        """
        Neteja la pantalla de la consola.
        """
        os.system('cls' if os.name == 'nt' else 'clear')


    def header(self, title: str):
        """
        Dibuixa un header amb un títol centrat.
        Args:
            title (str): títol a mostrar
        fem servir el mètode center de la str per generar un 
        text de la mateixa amplada que la pantalla
        """
        self.clear_screen()

        print("-" * self.width)
        print(title.center(self.width)) 
        print("-" * self.width)
    

    def modal(self, text: str, timeout: int = 2):
        """
        Mostra un missatge "modal" a l'usuari durant un temps determinat.
        Args:
            text (str): missatge a mostrar
            timeout (int): temps en segons que es mostra el missatge
        """
        self.clear_screen()
        text= text.center(self.width)

        print(colorama.Fore.GREEN + text + colorama.Style.RESET_ALL)
        time.sleep(timeout)

        self.clear_screen()


    def main_menu(self, options= None) -> str:
        """
        Mostra el menú principal i retorna l'opció seleccionada per l'usuari.
        Returns:
            str: opció seleccionada
        """

        if options is None:
            raise ValueError("Error: No s'han proporcionat opcions per al menú.")
        
        self.clear_screen()
        self.header(title="Benvingut al sistema de preparació de comandes")
        
        for key, value in options.items():
            print(f"{key}. {value}")

        print("-" * self.width)

        #esperem l'entrada de l'usuari
        message= "Selecciona una opció: "
        choice = input(colorama.Fore.CYAN + message + colorama.Style.RESET_ALL)

        if choice not in options:
            message= "Opció no vàlida. Torna-ho a intentar."
            print(colorama.Fore.RED + message + colorama.Style.RESET_ALL)
            time.sleep(1)
            return self.main_menu(options)
        
        return choice
    

    def list(self, title: str, items_list: list, return_after: bool = True):
        """
        Mostra una llista d'ojectes.
        Args:
            items_list (list): llista
            title (str): títol de la llista
            return_after (str): missatge per tornar després de mostrar la llista
        """
        self.clear_screen()
        self.header(title= title)

        for item in items_list:
            # fem servir el mètode describe() de cada objecte
            print(item.describe())
        if return_after:
            input("\nPrem Enter per continuar...")


    def ask(self, prompt: str) -> str:
        """
        Sol·licita una entrada a l'usuari.
        Args:
            prompt (str): missatge de sol·licitud
        Returns:
            str: entrada de l'usuari
        """
        return input(colorama.Fore.CYAN + prompt + colorama.Style.RESET_ALL)
    

    def show_message(self, message: str, timeout: int = 0):
        """
        Mostra un missatge a l'usuari.
        Args:
            message (str): missatge a mostrar
        """
        print(colorama.Fore.WHITE + message + colorama.Style.RESET_ALL)
        time.sleep(timeout)
    

    def show_order_summary(self, order):
        """
        Mostra el resum de la comanda.
        Args:
            order (Order): instància de la classe Order per mostrar la comanda
        """

        self.clear_screen()
        self.header(title="Resum de la Comanda")
        print("\n")
        order.show()
        input("\nPrem Enter per continuar...")