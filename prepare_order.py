import os

from users import Customer, Cashier
from util import CSVFileManager, CustomerConverter, CashierConverter, ProductConverter

from util.drawer import Drawer

from orders import Order

# definm la constant de l'amplada de la pantalla
SCREEN_WIDTH = 60

class PrepareOrder:

    def __init__(self):
        self.customers= []
        self.cashiers= []
        self.products= []
        self.order= []
        
        if not self.read_data_soources():
            print("Error en carregar les dades inicials dels fitxers CSV.")
            exit(1)
        self.run()


    def run(self):
        drawer = Drawer(SCREEN_WIDTH)

        options = {
            "0": "Nova comanda",
            "1": "Llistar clients",
            "2": "Llistar caixers",
            "3": "Llistar productes",
            "9": "Sortir"
        }

        while True:
            choice = drawer.main_menu(options)
            match choice:
                case '0':
                    drawer.modal(text= "Iniciant nova comanda...", timeout= 1)
                    self.new_order(drawer)
                    
                case '1':
                    drawer.list("Llistat de Clients", self.customers)

                case '2':
                    drawer.list("Llistat de Caixers", self.cashiers)

                case '3':
                    drawer.list("Llistat de Productes", self.products)

                case '9':
                    drawer.modal("Sortint del sistema. Fins aviat!")
                    exit(0)


    def cashier_login(self, drawer: Drawer) -> Cashier:
        """
        Sol·licita al caixer que introdueixi el seu DNI i verifica si existeix.
        Args:
            drawer (Drawer): instància de la classe Drawer per gestionar la interfície d'usuari
        Returns:
            Cashier: retorna l'objecte Cashier si es troba
        """
        drawer.clear_screen()
        cashier_dni = drawer.ask("Introdueix DNI del caixer: ")

        # cerquem el dni a la llista
        for cashier in self.cashiers:
            if str(cashier.dni) == cashier_dni:
                drawer.show_message(cashier.describe(), timeout=1)
                return cashier

        # No s'ha trobat el caixer, el torem a demanar
        drawer.modal("Caixer no trobat.", timeout=2)
        self.cashier_login(drawer)
    

    def search_customer(self, drawer: Drawer) -> Customer:
        """
        Sol·licita al client que introdueixi el seu DNI i verifica si existeix.
        Args:
            drawer (Drawer): instància de la classe Drawer per gestionar la interfície d'usuari
        Returns:
            Customer: retorna l'objecte Customer si es troba
        """

        drawer.clear_screen()
        customer_dni = drawer.ask("Introdueix DNI del client: ")

        # cerquem el dni a la llista
        for customer in self.customers:
            if str(customer.dni) == customer_dni:
                drawer.show_message(customer.describe(), timeout=1)
                return customer

        # No s'ha trobat el client, el torem a demanar
        drawer.modal("Client no trobat.", timeout=2)
        self.search_customer(drawer)


    def product_selection(self, drawer: Drawer, order: Order):
        """
        Permet seleccionar productes per afegir a la comanda.
        Args:
            drawer (Drawer): instància de la classe Drawer per gestionar la interfície d'usuari
            order (Order): instància de la classe Order per afegir productes
        """

        drawer.clear_screen()
        while True:
            drawer.list("Llistat de Productes", self.products, return_after= False)
            choice = drawer.ask("Selecciona un producte per afegir: ")
            
            found= False
            for product in self.products:
                if str(product.id) == choice:
                    if not order.add(product):
                        drawer.modal("Error en afegir el producte a la comanda.", timeout=2)
                        return
                    
                    drawer.modal(f"Producte '{product.name}' afegit a la comanda.", timeout=1)
                    found = True
                    break

            if not found:
                drawer.modal("Producte no trobat. Torna-ho a intentar.", timeout=2)
            else:
                # preguntem si vol afegir més productes
                while True:
                    add_more = drawer.ask("Vols afegir més productes? (s/n): ")
                    if add_more.lower() == 's':
                        break  # Torna al principi del bucle per afegir més productes
                    elif add_more.lower() == 'n':
                        return  # Surt de la funció
                    drawer.clear_screen()

      
    def new_order(self, drawer: Drawer):
        """
        Inicia el proecdiment per a geenrar una nova comanda.
        """
        # sol·licitar al caixer
        cashier = self.cashier_login(drawer)

        # sol·licitar al client
        customer = self.search_customer(drawer)

        # creem la comanda
        order = Order(cashier, customer)

        # afegim productes
        self.product_selection(drawer, order)

        # gaurdem la comanda
        if not order.save():
            drawer.modal("Error en guardar la comanda.", timeout=2)
            return        
        
        # mostrem el resum de la comanda
        drawer.show_order_summary(order)

        





    def read_data_soources(self) -> bool:
        """
        Carrega les dades inicals dels fitxers CSV i les converteix 
        en llistes d'objectes.
        Returns:
            bool: True si la càrrega és exitosa, False en cas contrari.
        """
        try:
            # Carregar i convertir dades dels clients
            customer_file_manager = CSVFileManager("data/customers.csv")
            customer_df = customer_file_manager.read()
            customer_converter = CustomerConverter()
            self.customers = customer_converter.convert(customer_df)
        except Exception as e:
            print(f"S'ha produït un error al carregar les dades dels clients: {e}")
            return False

        try:
            # Carregar i convertir dades dels caixers
            cashier_file_manager = CSVFileManager("data/cashiers.csv")
            cashier_df = cashier_file_manager.read()
            cashier_converter = CashierConverter()
            self.cashiers = cashier_converter.convert(cashier_df)
        except Exception as e:
            print(f"S'ha produït un error al carregar les dades dels caixers: {e}")
            return False


        """
        Creem un llista (mapping) amb els prodcutes que volem carregar i els 
        seus fitxers corresponents.
        Amb aquest sistema fem un bucle per carregar i convertir.  
        Evitem repetir codi i el codi és més fácil d'ampliar.
        """
        try:
            products_dict = {
                'Hamburger': "hamburgers.csv",
                'Soda': "sodas.csv",
                'HappyMeal': "happyMeal.csv",
                'Drink': "drinks.csv"
            }
            
            # Carregar i convertir dades dels productes
            for product in products_dict:
                # generem la ruta del fitxer
                file_name = os.path.join("data", products_dict[product])

                file_manager = CSVFileManager(file_name)
                df = file_manager.read()
                converter = ProductConverter()
                converted_products = converter.convert(df, product)

                # afegim els productes a la llista general
                self.products.extend(converted_products)

        except Exception as e:
            print(f"S'ha produït un error al carregar les dades inicials: {e}")
            return False
        return True


if __name__ == "__main__":
    app = PrepareOrder()
    app.run()
