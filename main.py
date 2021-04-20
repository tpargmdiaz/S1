import requests
import json

def ARS_USD():
    
  
    request = requests.get("http://ws.geeklab.com.ar/dolar/get-dolar-json.php")
    USD = json.loads(request.content)
    return int(USD['libre'])


def EUR_USD():
    
    request = requests.get("https://api.cambio.today/v1/quotes/EUR/USD/json?quantity=1&key=8800|Q16x8DeBowksxgJH^7HZg3W4dDAOiG_x")
    USD = json.loads(request.content)
    return int((USD['result']['value']))



moneda = input("Ingrese 1 para ARS o 2 para EUR:")


# Pasar como argumento la cantidad de ARS a convertir en dólares.
if moneda =="1":
    Cotiz_USD = print(f"La cotización actual del USD es de ${ARS_USD()} ARS.")
    USD = ARS_USD()
    monto_en_ARS = int(input("Ingrese el monto de ARS que desea convertir a USD:"))
    monto_en_USD = monto_en_ARS * USD
    print(f'${monto_en_ARS} ARS equivalen a ${monto_en_USD} EUR')

# Pasar como argumento la cantidad de EUR a convertir en dólares.
elif moneda == "2":
    Cotiz_USD = print(f"La cotización actual del USD es de ${EUR_USD()} EUR.")
    USD = EUR_USD()
    monto_en_EUR = int(input("Ingrese el monto de EUR que desea convertir a USD:"))
    monto_en_USD = monto_en_EUR * USD
    print(f'${monto_en_EUR} EUR equivalen a ${monto_en_USD} USD.')

else:
    print("Solo puede ingresar los valores 1 o 2")



