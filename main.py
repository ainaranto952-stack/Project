class boutique:
    def __init__(self, marque, prix, stock):
        self.marque = marque
        self.prix = prix
        self.stock = stock
        
    def vendre(self):
        if self.stock > 0:
            print("{self.marque} de {self.prix}Ar est dispo en stock")
        else:
            print("{self.marque} en rupture de stock")
            
    def afficher_telephone(self):    
        print("{self.marque}, {self.prix}Ar, {self.stock}")
        
        
telephone1 = boutique("Samsung s26, 1000000, 20")
telephone2 = boutique("iPhone 11, 700000, 7")
telephone3 = boutique("Xiaomi 17 pro, 1500000, 0")
telephone4 = boutique("Motorola, 450000, 1")

telephone1.afficher_telephone()
telephone2.afficher_telephone()
telephone3.afficher_telephone()
telephone4.afficher_telephone()
telephone1.vendre()
telephone2.vendre()
telephone3.vendre()
telephone4.vendre()                
             
    