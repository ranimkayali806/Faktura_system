from datetime import datetime
class ReceiptRow:
    def __init__(self,productnamn:str,count:int,perprice:float):
        self.__ProductNamn = productnamn
        self.__Count = count
        self.__PerPrice = perprice
    def GetProductNamn(self):
        return self.__ProductNamn
    def GetPerPrice(self):
        return self.__PerPrice
    def GetCount(self):
        return self.__Count
    def AddCount(self, antal):
        self.__Count = self.__Count + antal
   

    def GetTotal(self):  # för varje product
        return self.__Count * self.__PerPrice
class Receipt:
    def __init__(self):
        self.__Datum = datetime.now()
        self.__ReceiptRows = []
    def Add(self, prod, antal):
        #recrow = None
        found = False
        for x in self.__ReceiptRows:
            if x.GetProductNamn() == prod.GetName():
                x.AddCount(int(antal))
                found = True
                break
        if found == False:
            r = ReceiptRow(prod.GetName(), antal, prod.GetPrice())
            self.__ReceiptRows.append(r)

    def GetTotal(self):  #sista belopp för varje kvitto
         sum = 0
         for row in self.__ReceiptRows:
            sum = sum + row.GetTotal()
         return sum
    def GetReceiptRows(self):
        return self.__ReceiptRows
