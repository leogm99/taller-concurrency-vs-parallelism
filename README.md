# Concurrencia Vs Paralelismo

En este repositorio se muestran ejemplos de uso de hilos para construir una suma particionada en cpp y en python.

Las diferencias principales, mas allá del código, es lo que sucede con el uso de los cpu cores. En la 
implementacion en cpp, veremos que la maquina utilizará multiples cores al mismo tiempo (paralelismo) 
mientras que la version de python utilizará a lo sumo un core a la vez. Esto se debe a que CPython tiene un lock global (GIL), utilizado para sincronizar el manejo de memoria entre los threads. Esto limita
entonces las posibilidades de ejecutar hilos de manera paralela, ya que el interprete podrá ejecutar
unicamente el código de un solo hilo en un instante de tiempo.
De esta manera, los threads en python pelean por un mismo recurso, el time slice, mientras que 
los threads en cpp tienen la posibilidad de aprovechar cada uno su propio slice de tiempo en 
un core distinto.

Concurrencia: N hilos comparten un mismo recurso (léase: file descriptors, heap, stack, cpu cores, etc)

Paralelismo: Cada hilo tiene ownership de sus recursos y los acceden de manera independiente y potencialmente al mismo tiempo que otros.