import requests
from bs4 import BeautifulSoup
import pandas as pd

#diccionario que tiene las url de MeLi para hacer las busquedas
def search_mercadolibre(country, product_name):
    base_urls = {
        'argentina': 'https://listado.mercadolibre.com.ar/',
        'brasil': 'https://lista.mercadolivre.com.br/',
        'mexico': 'https://listado.mercadolibre.com.mx/',
        'chile': 'https://listado.mercadolibre.cl/'
    }
#verifica si el pais esta soportado
    if country not in base_urls:
        print(f"País '{country}' no soportado.")
        return []

    #  URL de búsqueda
    url = base_urls[country] + product_name.replace(' ', '-')
    #configuración para hacer solicitudes http
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    resultados = [] #realiza solicitud get

    if response.status_code == 200: #respuesta exitosa 
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('li', class_='ui-search-layout__item')

        if items:
            print(f"\nResultados en MercadoLibre {country.capitalize()} para '{product_name}':") #chequear que se encontraron los productos
            for item in items:
                title = item.find('h2', class_='ui-search-item__title')
                link_tag = item.find('a', class_='ui-search-link')
                if title and link_tag:
                    link = link_tag['href']
                    print(f"Producto encontrado: {title.text.strip()}")
                    print(f"URL: {link}\n")
                    resultados.append({'País': country.capitalize(), 'Producto': product_name, 'Título': title.text.strip(), 'URL': link})
                else:
                    print("No se encontró enlace o título para un producto.")
        else:
            print(f"No se encontraron productos en MercadoLibre {country.capitalize()} para '{product_name}'.")
    else:
        print(f"Error al conectar con MercadoLibre {country.capitalize()}.")

    return resultados
#Solicitar productos por consola
productos = input("Ingresa una lista de productos separados por comas: ").split(',')

paises = ['argentina', 'brasil', 'mexico', 'chile']
todos_resultados = []

#búsqueda para cada producto en cada país
for producto in productos:
    producto = producto.strip()
    for pais in paises:
        resultados = search_mercadolibre(pais, producto)
        todos_resultados.extend(resultados)

# genera archivo Excel con el resultado
if todos_resultados:
    df = pd.DataFrame(todos_resultados)
    df.to_excel('resultados_mercadolibre.xlsx', index=False)
    print("\nLos resultados se han guardado en 'resultados_mercadolibre.xlsx'.")
else:
    print("\nNo se encontraron resultados para los productos ingresados.")
