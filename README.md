# Python - Días entre fechas

Este proyecto contiene una función en Python que calcula el número de días transcurridos entre dos fechas. Se ha mejorado la implementación original utilizando el módulo `datetime` de Python para lograr un código más robusto, claro y eficiente.

## Características

- **Cálculo preciso:** Se utiliza el módulo `datetime` para calcular la diferencia en días, manejando correctamente años bisiestos.
- **Validación de fechas:** Se comprueba que la fecha inicial sea anterior o igual a la fecha final y que las fechas sean válidas.
- **Código limpio y documentado:** El código cuenta con docstrings y comentarios que facilitan su mantenimiento y comprensión.

## Requisitos

- Python 3.6 o superior

## Instalación

No se requieren dependencias externas, ya que se utiliza la biblioteca estándar de Python.

1. Clona el repositorio:

   ```bash
   git clone https://github.com/runciter2078/Python_Dias_Entre_Fechas.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd Python_Dias_Entre_Fechas
   ```

## Uso

La función principal se encuentra en el archivo `dias_entre_fechas.py`. Puedes importarla en tu script o ejecutarla directamente desde la línea de comandos.

### Ejemplo de Uso

```python
from dias_entre_fechas import dias_entre_fechas

# Calcula el número de días entre el 1 de enero de 2020 y el 10 de enero de 2020
dias = dias_entre_fechas(1, 1, 2020, 10, 1, 2020)
print("Número de días:", dias)
```

También puedes ejecutar el script directamente para ver un ejemplo en acción:

```bash
python dias_entre_fechas.py
```

## Manejo de Errores

- **Fechas no válidas:** Si alguna de las fechas introducidas no es válida, se lanzará un `ValueError` con un mensaje descriptivo.
- **Orden de fechas:** Si la fecha inicial es posterior a la fecha final, se lanzará un `ValueError` indicando que la fecha inicial debe ser anterior o igual a la fecha final.

## Notas

- La implementación se basa en el módulo `datetime`, lo que simplifica el manejo de fechas y garantiza la precisión del cálculo.
- Este proyecto es una versión mejorada y modernizada del código original, eliminando duplicaciones y posibles errores lógicos.

## Licencia

Este proyecto se distribuye bajo la [Licencia MIT](LICENSE).
