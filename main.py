from datetime import datetime
from math import prod
from product import product
from receipt import Receipt,ReceiptRow
allProducts = []
allaKvittor = []
with open("products.txt",'r') as file:
    for line in file:
       parts = line.split(";")
       prod = product(parts[1],float(parts[2]), parts[0],parts[3])
       allProducts.append(prod)


def HuvudMeny():
  while True:

    print('1. Ny kund')
    print('2.Avsluta')
    
    try: 
      selection = int(input(':'))
      return selection
    except ValueError:
      print('it is not integer')

def findProducts(allProducts, productId):
    for x in allProducts:
        if x.GetProductId() == productId:
            return x
    return None

def NyttKvitto(allProduct):
 rec = Receipt()
 while True:
  print('kassa')
  datum = datetime.now() #'2002-20-05 13:45:12'  #strftime
  print(f'kvitto: {datum}')
  for row in rec.GetReceiptRows():
    print(f"{row.GetProductNamn()}  {row.GetCount()} {row.GetPerPrice()}  {row.GetCount()*row.GetPerPrice()}")
  
  print( rec.GetTotal() )
  print('kommando:')
  print('pay')
  action = input('kommando:')
  if action == 'pay':

   with open('receipt.txt', 'a') as file:
      
    file.write(f'kvitto: {datum}\n')
    for row in rec.GetReceiptRows():
      file.write(f"{row.GetProductNamn()}  {row.GetCount()} {row.GetPerPrice()}  {row.GetCount()*row.GetPerPrice()}\n")
    file.write( str(rec.GetTotal()) + "\n" )

    
   
      
    print(f'kvitto: {datum}')
    break
  parts = action.split(" ")
  productId = parts[0]
  
  try:
   antal = int(parts[1])
  except:
    print('fel, it is not integer')
    continue

    
  p = findProducts(allProduct,productId)
  if p == None:
    print("felaktigt produktid")
  else:
    rec.Add(p,antal)



while True:
 sel = HuvudMeny()
 if sel == 2:
        break 
 elif sel == 1:
        NyttKvitto(allProducts)
