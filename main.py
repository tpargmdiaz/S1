import requests
import json


#La función ARS_USD consume la api de geeklab.com.ar. De allí toma el valor del dólar desde la key 'libre'.

def ARS_USD():
    
    request = requests.get("http://ws.geeklab.com.ar/dolar/get-dolar-json.php")
    USD = json.loads(request.content)
    return float(USD['libre'])



#La función EUR_USD consume la api de cambio.today. De allí toma el valor del euro desde la key 'value' dentro del valor de la key 'result'

def EUR_USD():
    
    request = requests.get("https://api.cambio.today/v1/quotes/EUR/USD/json?quantity=1&key=8800|Q16x8DeBowksxgJH^7HZg3W4dDAOiG_x")
    USD = json.loads(request.content)
    return float((USD['result']['value']))


# Aquí comienza el flujo. El loop while es para que el programa continúe funcionando hasta que el usuario ingrese el valor indicado para terminar. Agregué un try/except para el control de errores.

while True:
    moneda = input("Ingrese 1 para ARS o 2 para EUR (presione s para salir):")
    try:

        # Si el valor ingresado es '1' el programa realizará la conversión de pesos a dólares. Se redondea el resultado a dos decimales.

        if moneda == "1":
            Cotiz_USD = print(f"La cotización actual del USD es de ${ARS_USD()} ARS.")
            USD = ARS_USD()
            monto_en_ARS = float(input("Ingrese el monto de ARS que desea convertir a USD:"))
            monto_en_USD = monto_en_ARS / USD
            monto_en_USD_round = round(monto_en_USD, 2)
            print(f'${monto_en_ARS} ARS equivalen a ${monto_en_USD_round} USD')
    

        # Si el valor ingresado es '2' el programa realizará la conversión de euros a dólares. Se redondea el resultado a dos decimales.

        elif moneda == "2":
            Cotiz_USD = print(f"La cotización actual del USD es de ${EUR_USD()} EUR.")
            USD = EUR_USD()
            monto_en_EUR = float(input("Ingrese el monto de EUR que desea convertir a USD:"))
            monto_en_USD = monto_en_EUR / USD
            monto_en_USD_round = round(monto_en_USD, 2)
            print(f'${monto_en_EUR} EUR equivalen a ${monto_en_USD_round} USD.')


        # Si el valor ingresado es 's' el programa termina de ejecutarse.

        elif moneda == "s":
            print("Programa Terminado")
            break
            

        # Si el usuario ingresa un valor distindo de 1 o 2 el programa imprime un mensaje indicando que solo puede ingresar esos valores.

        else:
            print("Solo puede ingresar los valores 1 o 2")
            continue
    

    # Control de errores.
    
    except:
        print("Ha habido un error. Revise el valor ingresado e Intente nuevamente.")