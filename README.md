# RecetApp

Aplicación en Python que te dice qué puedes cocinar con los ingredientes que compraste en el mercado. El usuario escribe sus compras y la app muestra las recetas que puede preparar, con sus pasos, y también las que le faltan por un solo ingrediente.

El proyecto nació para dar más variedad e ideas a la hora de cocinar, con recetas de Colombia y de otros países.

## Qué hace

- En la web, al elegir una región se ven todos sus platos, y cada ingrediente que agregas reduce la lista a los platos que lo usan. Un interruptor permite ver solo lo que ya puedes preparar con tus ingredientes.
- En la web, la región (Colombia, México, Italia, España, Perú, Francia, Japón, Corea, Argentina o Estados Unidos) es opcional: sin elegir ninguna busca en todas, y al elegir una botón filtra solo esa región. En la terminal la región se elige al inicio.
- Incluye 500 recetas (50 por región) de 10 países.
- En la web hay un buscador por nombre de plato (sin importar tildes, mayúsculas ni plurales), que funciona solo o combinado con la región y los ingredientes.
- En cada receta, los ingredientes que tienes salen en verde (✓) y los que te faltan en rojo (✗).
- En la web eliges los ingredientes desde una lista, agregando y quitando los que quieras. En la terminal los escribes separados por coma.
- Muestra las recetas de esa región que se pueden preparar completas, con su paso a paso.
- Muestra las recetas a las que les falta solo un ingrediente, indicando cuál.
- Reconoce mayúsculas, tildes y plurales (por ejemplo, "Papas", "PAPA" y "papa" cuentan igual).
- Considera aceite y sal como ingredientes básicos que ya se tienen en casa.
- Cada receta muestra tiempo, porciones, dificultad, utensilios, ingredientes con cantidades, pasos detallados y consejos.
- En la web, los ingredientes que tienes aparecen en verde y los que faltan en rojo.

## Ejemplo de uso

```
¿De qué región quieres cocinar?
1. Colombia
2. México
3. Italia
4. España
5. Perú
6. Francia
7. Japón
8. Corea
9. Argentina
10. Estados Unidos
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

Abre `recetas.json`, busca la región y agrega una entrada con este formato, cuidando las comas entre recetas:

```json
"Nombre de la receta": {
    "ingredientes": ["arroz", "pollo", "sal"],
    "cantidades": {"arroz": "2 tazas", "pollo": "500 g", "sal": "1 cucharadita"},
    "tiempo": 45,
    "porciones": 4,
    "dificultad": "Fácil",
    "utensilios": ["olla", "tabla de cortar"],
    "pasos": ["Primer paso con tiempos y señales de cocción.", "Segundo paso."],
    "consejos": ["Un consejo útil.", "Otro consejo."]
}
```

- `ingredientes` se escribe en minúscula y en singular; es la lista que usa el buscador.
- `cantidades` debe tener exactamente los mismos ingredientes.
- `tiempo` va en minutos; `dificultad` es "Fácil", "Intermedio" o "Desafiante".
- `pasos` es una lista; el formato antiguo (texto con "1. ... 2. ...") también sigue funcionando.

## Próximos pasos

- Más recetas para cada región.
- Lista de sinónimos para ingredientes (por ejemplo, ahuyama y zapallo).
- Lectura de la factura del supermercado para cargar los ingredientes automáticamente.

## Autor

Oscar Iván Sánchez Arciniegas, estudiante de Ingeniería de Sistemas en la Universidad Autónoma del Caribe.
Proyecto en desarrollo, construido como práctica de Python.

## Pruebas automáticas

El proyecto incluye 30 pruebas con `pytest`:

- `tests/test_logica.py`: limpieza de texto (tildes, mayúsculas, plurales), filtro por ingredientes, ingredientes faltantes, búsqueda por nombre y formato de pasos y tiempo.
- `tests/test_recetas.py`: valida que las 500 recetas tengan el formato correcto (cantidades, tiempo, porciones, dificultad, pasos y consejos).

Para ejecutarlas:

```
pip install -r requirements-dev.txt
pytest
```
