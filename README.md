# App de Recetas

Aplicación en Python que te dice qué puedes cocinar con los ingredientes que compraste en el mercado. El usuario escribe sus compras y la app muestra las recetas que puede preparar, con sus pasos, y también las que le faltan por un solo ingrediente.

El proyecto nació para dar más variedad e ideas a la hora de cocinar, con recetas de Colombia y de otros países.

## Qué hace

- Te deja elegir primero la región (Colombia, México, Italia, España o Perú).
- Recibe una lista de ingredientes separados por coma.
- Muestra las recetas de esa región que se pueden preparar completas, con su paso a paso.
- Muestra las recetas a las que les falta solo un ingrediente, indicando cuál.
- Reconoce mayúsculas, tildes y plurales (por ejemplo, "Papas", "PAPA" y "papa" cuentan igual).
- Considera aceite y sal como ingredientes básicos que ya se tienen en casa.

## Ejemplo de uso

```
¿De qué región quieres cocinar?
1. Colombia
2. México
3. Italia
4. España
5. Perú
Elige el número de la región: 1

Región elegida: Colombia
Escribe los ingredientes que compraste, separados por coma.
Ingredientes: Arroz, pollo, cebolla, tomate, papa

Puedes preparar:

- Pollo guisado
1. Sofríe cebolla y tomate en aceite. 2. Agrega el pollo en presas y dóralo. ...

- Arroz con pollo
1. Sofríe cebolla y tomate. 2. Agrega el pollo en trozos y cocínalo. ...

Te falta solo 1 ingrediente para:
- Arroz con huevo (te falta: huevo)
- Yuca frita (te falta: yuca)
...
```

## Requisitos

- Python 3.10 o superior.
- La versión de terminal no necesita librerías adicionales.
- La versión web necesita Streamlit (ver más abajo).

## Cómo ejecutarla

1. Clona el repositorio:

   ```
   git clone https://github.com/Oscarsz06/app-recetas.git
   ```

2. Entra a la carpeta del proyecto:

   ```
   cd app-recetas
   ```

3. Ejecuta la versión de terminal:

   ```
   python app.py
   ```

### Versión web

1. Instala Streamlit:

   ```
   python -m pip install -r requirements.txt
   ```

2. Ejecuta la página:

   ```
   python -m streamlit run app_web.py
   ```

   Se abre en el navegador (normalmente en http://localhost:8501).

## Estructura del proyecto

| Archivo | Descripción |
| --- | --- |
| `logica.py` | Lógica compartida: limpieza de texto, plurales y búsqueda de recetas. |
| `app.py` | Versión de terminal. |
| `app_web.py` | Versión web hecha con Streamlit. |
| `requirements.txt` | Librerías necesarias para la versión web. |
| `recetas.json` | Base de recetas organizada por región, con sus ingredientes y pasos. |

## Cómo agregar una receta

Abre `recetas.json`, busca la región a la que pertenece la receta (o crea una nueva con el nombre del país) y agrega una entrada con este formato dentro de ella, cuidando las comas entre recetas:

```json
"Nombre de la receta": {
    "ingredientes": ["ingrediente1", "ingrediente2"],
    "pasos": "1. Primer paso. 2. Segundo paso."
}
```

Escribe los ingredientes en minúscula y en singular.

## Próximos pasos

- Más recetas para cada región.
- Lista de sinónimos para ingredientes (por ejemplo, ahuyama y zapallo).
- Lectura de la factura del supermercado para cargar los ingredientes automáticamente.

## Autor

Oscar Iván Sánchez Arciniegas, estudiante de Ingeniería de Sistemas en la Universidad Autónoma del Caribe.
Proyecto en desarrollo, construido como práctica de Python.
