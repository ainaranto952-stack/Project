class Telephone:
    def __init__(self, marque, prix, stock):
        self.marque = marque
        self.prix = prix
        self.stock = stock

    def vendre(self):
        if self.stock > 0:
            print(f"{self.marque} à {self.prix} Ar est disponible en stock")
        else:
            print(f"{self.marque} est en rupture de stock")

    def afficher_telephone(self):
        print(f"{self.marque}, {self.prix} Ar, {self.stock}")


telephone1 = Telephone("Samsung S26", 1000000, 20)
telephone2 = Telephone("iPhone 11", 700000, 7)
telephone3 = Telephone("Xiaomi 17 Pro", 1500000, 0)
telephone4 = Telephone("Motorola", 450000, 1)

telephone1.afficher_telephone()
telephone2.afficher_telephone()
telephone3.afficher_telephone()
telephone4.afficher_telephone()

telephone1.vendre()
telephone2.vendre()
telephone3.vendre()
telephone4.vendre()