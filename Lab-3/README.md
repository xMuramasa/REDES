# Lab 3 Redes de Computadores
github: "https://github.com/xMuramasa/REDES/tree/master/Lab%203"

## Integrantes:
- Zhuo Chang 
- Martin Salinas Scussolin

## Requerimientos:
- Máquina virtual con mininet
- pox
- python 2.7

# Uso
#### Parte 1 (se encuentra en la carpeta topo 1)

- Se deben copiar los archivos de la carpeta forwarding del repositorio del laboratorio en el directorio "pox/pox/forwarding"

- Para ejecutar el controlador, se debe utilizar la siguiente linea para ejecutar:
    
    - python pox.py --verbose openflow.spanning_tree --no-flood --hold-down openflow.discovery forwarding.l2_learning2

- Para ejecutar mininet y la red, se debe hacer con la siguiente linea:
    - sudo mn --custom topologia1.py --topo mytopo --controller remote --switch ovsk --mac


#### Parte 2