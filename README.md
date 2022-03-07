# mutantex
Autor: Jose Gomez
Código para detectar secuencias ADN mutantes Xmen - Python+Flask

Para ejecutar la API
1. Ir dirección http://107.180.72.62:5000/ - se verifica que el servicio este disponible
2. Abrir un SOAP UI y pasar REST bajo la dirección http://107.180.72.62:5000/mutant
3. Pasar la estructura json con el formato ; puede variar según la secuencia de cuatro letra iguales , de forma oblicua, horizontal o vertical
  {
   "dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG","AAAAGT"]
  }
 4. para verificar las estadisticas http://107.180.72.62:5000/stats 

