#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo para calcular el número de días transcurridos entre dos fechas.

Este módulo utiliza el módulo estándar datetime para asegurar un cálculo robusto,
incluyendo el manejo correcto de años bisiestos, validando que la fecha inicial sea
anterior o igual a la fecha final.
"""

from datetime import date

def dias_entre_fechas(day1, month1, year1, day2, month2, year2):
    """
    Calcula el número de días transcurridos entre dos fechas.

    Args:
        day1 (int): Día de la fecha inicial.
        month1 (int): Mes de la fecha inicial.
        year1 (int): Año de la fecha inicial.
        day2 (int): Día de la fecha final.
        month2 (int): Mes de la fecha final.
        year2 (int): Año de la fecha final.

    Returns:
        int: Número de días entre la fecha inicial y la fecha final.

    Raises:
        ValueError: Si la fecha inicial es posterior a la fecha final.
    """
    try:
        fecha_inicial = date(year1, month1, day1)
        fecha_final = date(year2, month2, day2)
    except ValueError as ve:
        raise ValueError("Una o más de las fechas introducidas no son válidas: " + str(ve))

    if fecha_inicial > fecha_final:
        raise ValueError("La fecha inicial debe ser anterior o igual a la fecha final.")

    diferencia = fecha_final - fecha_inicial
    return diferencia.days

if __name__ == '__main__':
    # Ejemplo de uso
    try:
        dias = dias_entre_fechas(1, 1, 2020, 10, 1, 2020)
        print("Número de días entre 1/1/2020 y 10/1/2020:", dias)
    except ValueError as error:
        print("Error:", error)
