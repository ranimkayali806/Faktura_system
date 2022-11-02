class product:
#använda encapculation
    def __init__(self,namn:str,price:int,productid:str,producttype:str):  
        self.__Namn = namn
        self.__Price = price
        self.__ProductId = productid
        self.__ProductType = producttype
    def GetName(self):
        return self.__Namn
    def GetPrice(self):
        return self.__Price
    def GetProductId(self):
        return self.__ProductId
    
    



