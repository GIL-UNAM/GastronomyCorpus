# GastronomyCorpus

## Corpus 
* Se tienen los siguientes corpus

| Corpus | Paráfrasis | No paráfrasis 
| --- | --- | --- |
| Carrito | 150 | 350 |
| Cocina molecular | 648 | 1512 |
| Kebab | 175 | 408 |
| Ofrenda | 200 | 467 |
| Sushi | 166 | 387 |
| Tequila | 175 | 408 |
| Vegana | 150 | 350 |


* Se obtuvieron particiones de entrenamiento (70%) y prueba (30%)

| Corpus | Entrenamiento | Prueba | Total |
| --- | --- | --- | --- |
| Carrito | <ul><li>Paráfrasis: 105</li> <li>No paráfrasis: 244</li></ul> |  <ul><li>Paráfrasis: 45</li> <li>No paráfrasis: 106</li></ul> | 500 |
| Cocina molecular | <ul><li>Paráfrasis: 453</li> <li>No paráfrasis: 1058</li></ul> |  <ul><li>Paráfrasis: 195</li> <li>No paráfrasis: 454</li></ul> | 2160 |
| Kebab | <ul><li>Paráfrasis: 122</li> <li>No paráfrasis: 285</li></ul> |  <ul><li>Paráfrasis: 53</li> <li>No paráfrasis: 123</li></ul> | 583 |
| Ofrenda | <ul><li>Paráfrasis: 140</li> <li>No paráfrasis: 326</li></ul> |  <ul><li>Paráfrasis: 60</li> <li>No paráfrasis: 141</li></ul> | 667 |
| Sushi | <ul><li>Paráfrasis: 116</li> <li>No paráfrasis: 270</li></ul> |  <ul><li>Paráfrasis: 50</li> <li>No paráfrasis: 117</li></ul> | 553 |
| Tequila | <ul><li>Paráfrasis: 122</li> <li>No paráfrasis: 285</li></ul> |  <ul><li>Paráfrasis: 53</li> <li>No paráfrasis: 123</li></ul> | 583 |
| Vegana | <ul><li>Paráfrasis: 105</li> <li>No paráfrasis: 244</li></ul> |  <ul><li>Paráfrasis: 45</li> <li>No paráfrasis: 106</li></ul> | 500 |  


### Distribución final de los corpus de entrenamiento y evaluación

| Corpus | Núm. pares de oraciones en total | Núm. pares de oraciones paráfrasis | Núm. pares de oraciones no paráfrasis 
| --- | --- | --- | --- |
| Entrenamiento | 7601 (100%) | 1501 (20%) | 6100 (80%) | 
| Evaluación | 2942 (100%) | 588 (20%)  | 2354 (80%) |


### Directorios del corpus

Los corpus están divididos en carpetas distintas y se pueden ubicar de la siguiente manera.

Los textos originales tienen el nombre del corpus:
* sushi.txt
* cocina.txt
* tequila.txt
* kebab.txt
* ofrenda.txt
* vegana.txt
* carrito.txt

Los demás textos tienen un prefijo más un identificador numérico para poder diferenciarlos.

Estos prefijos son los siguientes

| Tipo de texto | prefijo | Ejemplo |
|---|---|---|
| Creación literaria | Creación | CreacionCocina_01.txt |
| Paráfrasis baja | Baja | BajaKebab_01.txt |
| Paráfrasis alta | Alta | AltaOfrenda_01.txt |
| No paráfrasis | NoParafrasis | NoParafrasisVegana_01.txt |

Dentro de cada carpeta, hay otra llamada *references_parafrasisAlta*, en donde se encuentran las referencias de las paráfrasis altas.

