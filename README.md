# Python_Dias_Entre_Fechas
El siguiente código es un programa en Phyton que calcula el número de días transcurridos entre dos fechas cualesquiera.

En general, la resolución del algoritmo tiene los siguientes matices:

1- Se crea una función, llamada diasHastaFecha que recibe como entradas 6 números: día, mes y año de inicio, y día, mes y año final.
2- El primer código dentro de la función es otra función llamada esBisiesto que nos dice si un año es bisiesto o no. Está sacado directamente de la definición del algoritmo de año bisiesto que indica que un año es bisiesto si dicho año es divisible entre 4, excepto aquellos divisibles entre 100 pero no entre 400.
3- El resto del código está dividido en dos partes: una si el cálculo es entre diferentes años y otra si es dentro de un mismo año.
4- Si el cálculo es entre diferentes años, primero calculamos los días que quedan desde la fecha de inicio hasta el 31 de diciembre de dicho año. Se tiene en cuenta que si el año es bisiesto febrero tiene 29 días. Luego se calculan los días de los años intermedios entre fechas: 365 días los años normales y 366 días los años bisiestos. Por último se calcula los días que hay desde el 1 de enero del año final hasta la fecha indicada.
5- La segunda posibilidad es que la diferencia de días solicitada sean dentro del mismo año. El caso más sencillo es que sea además un cálculo dentro del mismo mes. En ese caso simple es tan sólo la diferencia entre los dos argumentos de entrada “días”. Si son diferentes meses, pues se calculan los días hasta final del primer mes, los días de meses intermedios y se le suma por último el número de día objetivo del mes final, todo ello considerando, igual que en los anteriores casos, que febrero tiene 28 o 29 días dependiendo de si el año es bisiesto.
6- Por último, pero no por ello menos importante, no se consideran posibles los viajes en el tiempo. Es decir, la fecha inicial debe ser siempre menor que la final. Es fácil implementar en el código un aviso de error si este caso sucediera, pero por no liarlo más se ha supuesto que la entrada es introducida correctamente por el usuario siempre.
