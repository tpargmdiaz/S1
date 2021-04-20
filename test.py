import requests
import json

def precioDolarEUR():
    
    request = requests.get("https://api.cambio.today/v1/quotes/EUR/USD/json?quantity=1&key=8800|Q16x8DeBowksxgJH^7HZg3W4dDAOiG_x")
    preciosDolar = json.loads(request.content)
    return(preciosDolar['result']['value'])
    

print(precioDolarEUR())