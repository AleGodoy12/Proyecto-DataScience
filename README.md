# Proyecto de Búsqueda de Productos en MercadoLibre

Este proyecto implementa un script en Python que permite buscar productos en diferentes versiones de MercadoLibre dependiendo del país. Los productos ingresados por el usuario se buscan en los sitios web específicos de MercadoLibre para Argentina, Brasil, México y Chile. Los resultados se muestran en la consola y se guardan en un archivo Excel para su posterior análisis.

## Librerías Utilizadas

El script utiliza las siguientes librerías:

- **requests**: Esta librería se utiliza para realizar solicitudes HTTP a las páginas web de MercadoLibre. Permite enviar solicitudes y recibir respuestas, lo cual es fundamental para obtener los datos de las páginas buscadas.

- **BeautifulSoup** (de `bs4`): Esta librería se utiliza para el análisis y la extracción de datos de documentos HTML y XML. Permite navegar por la estructura del DOM (Document Object Model) de la página web y extraer información específica, como títulos y enlaces de productos.

- **pandas**: Esta librería se utiliza para manipular datos en forma de tablas (DataFrames). Se emplea para almacenar los resultados de búsqueda y exportarlos a un archivo Excel, facilitando así el manejo de los datos.

## Funcionamiento del Código

### 1. Definición de la Función `search_mercadolibre`

La función `search_mercadolibre` toma dos parámetros: el país y el nombre del producto. A continuación, se detalla el funcionamiento de la función:

- **URLs Base**: Define un diccionario que asocia cada país con su respectiva URL de búsqueda en MercadoLibre.
- **Verificación de País**: Comprueba si el país ingresado está en el diccionario. Si no lo está, imprime un mensaje y retorna una lista vacía.
- **Construcción de la URL**: Crea la URL de búsqueda sustituyendo los espacios en el nombre del producto por guiones.
- **Solicitud GET**: Realiza una solicitud GET a la URL construida, utilizando `requests` con un encabezado de "User-Agent" para simular un navegador web.
- **Análisis de la Respuesta**: Si la respuesta es exitosa (código 200), utiliza BeautifulSoup para analizar el contenido HTML y buscar los elementos que contienen los productos.
- **Extracción de Títulos y Enlaces**: Itera sobre los elementos encontrados, extrayendo el título y el enlace de cada producto. Los datos se almacenan en una lista de diccionarios.
- **Mensajes en Consola**: Imprime en la consola información sobre los productos encontrados o mensajes de error según sea el caso.

### 2. Entrada de Datos

- **Lista de Productos**: Solicita al usuario que ingrese una lista de productos separados por comas. Utiliza `input()` para capturar los datos de entrada.

### 3. Búsqueda de Productos

- **Ciclos Anidados**: Utiliza ciclos `for` para iterar sobre cada producto ingresado y cada país soportado, llamando a la función `search_mercadolibre` para realizar la búsqueda.

### 4. Exportación a Excel

- **Resultados Finales**: Si se encontraron resultados, se crea un DataFrame utilizando `pandas` y se guarda en un archivo Excel llamado `resultados_mercadolibre.xlsx`. Se imprime un mensaje de confirmación en consola.

## Ejemplo de Uso

1. Ejecute el script en un entorno de Python.
2. Ingrese una lista de productos separados por comas (ejemplo: `laptop, teléfono`).
3. El script buscará en las versiones correspondientes de MercadoLibre para Argentina, Brasil, México y Chile.
4. Los resultados se imprimirán en la consola y se guardarán en un archivo Excel en la misma carpeta donde se ejecuta el script.

## Conclusión

Este proyecto proporciona una herramienta útil para buscar productos en múltiples sitios de MercadoLibre y gestionar los datos de manera sencilla. Gracias a las librerías utilizadas, el proceso de web scraping y la manipulación de datos son eficientes y efectivos. Se puede ampliar y mejorar según las necesidades del usuario.
