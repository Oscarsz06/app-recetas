# App de Recetas

Aplicación en Python que te dice qué puedes cocinar con los ingredientes que compraste en el mercado. El usuario escribe sus compras y la app muestra las recetas que puede preparar, con sus pasos, y también las que le faltan por un solo ingrediente.

El proyecto nació para dar más variedad e ideas a la hora de cocinar, con recetas colombianas y de la costa.

## Qué hace

- Recibe una lista de ingredientes separados por coma.
- Muestra las recetas que se pueden preparar completas, con su paso a paso.
- Muestra las recetas a las que les falta solo un ingrediente, indicando cuál.
- Reconoce mayúsculas, tildes y plurales (por ejemplo, "Papas", "PAPA" y "papa" cuentan igual).
- Considera aceite y sal como ingredientes básicos que ya se tienen en casa.

## Ejemplo de uso

```
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
- No necesita instalar librerías adicionales.

## Cómo ejecutarla

1. Clona el repositorio:

   ```
   git clone https://github.com/Oscarsz06/app-recetas.git
   ```

2. Entra a la carpeta del proyecto:

   ```
   cd app-recetas
   ```

3. Ejecuta la aplicación:

   ```
   python app.py
   ```

## Estructura del proyecto

| Archivo | Descripción |
| --- | --- |
| `app.py` | Lógica de la aplicación: lectura de ingredientes, limpieza de texto y búsqueda de recetas. |
| `recetas.json` | Base de recetas con sus ingredientes y pasos. |

## Cómo agregar una receta

Abre `recetas.json` y agrega una entrada con este formato, cuidando las comas entre recetas:

```json
"Nombre de la receta": {
    "ingredientes": ["ingrediente1", "ingrediente2"],
    "pasos": "1. Primer paso. 2. Segundo paso."
}
```

Escribe los ingredientes en minúscula y en singular.

## Próximos pasos

- Interfaz web con Streamlit.
- Más recetas colombianas.
- Lista de sinónimos para ingredientes (por ejemplo, ahuyama y zapallo).
- Lectura de la factura del supermercado para cargar los ingredientes automáticamente.

## Autor

Oscar Iván Sánchez Arciniegas, estudiante de Ingeniería de Sistemas en la Universidad Autónoma del Caribe.
Proyecto en desarrollo, construido como práctica de Python.
