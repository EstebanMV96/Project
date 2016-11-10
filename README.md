# Proyecto Sistemas Operativos
### Esteban Moya
### Andrés Valencia
### Paula Bolaños


#### Desarrollo
Instalar una maquina virtualbox con CentOS 7

Habilita las interfaces al iniciar(nat,bridge)

1. Crear usuario con el nombre *sistemasoperativos* para esto se utilizó el siguiente comando:

  ```bash
  # adduser sistemasoperativos
  ```

2. Se requiere instalar el gestor de descargas pip y el gestor de ambientes virtuales desarrollados en python, virtualenv, en la maquina para poder utilizar el servicio web

  ```bash
  $ cd /tmp
  $ wget https://bootstrap.pypa.io/get-pip.py
  $ python get-pip.py
  $ pip install virtualenv
  ```

    Estando en el usuario crear una carpeta que contendrá los archivos del ambiente en el que se implementará el servicio web

    ```bash
    $ mkdir environments
    ```
    Después dentro de la carpeta environments se crea y activa el ambiente de la siguiente forma:

    ```bash
    $ cd environments
    $ virtualenv flask_env
    $ . /flask_env/bin/activate
    ```
    Dentro del ambiente instalar flask

    ```bash
    $ pip install Flask
    ```

3. Para el funcionamiento del servicio se requiere abrir un en el que éste estará alojado, para el proyecto se utilizó el puerto 8088

  Para abrir un puerto en Centos 7 se requieren los siguientes pasos:
    * Iniciar el servicio *firewalld*:

    ```bash
    # service firewalld start
    ```

    * Abrir el puerto especificando la zona adecuada, número de puerto y protocolo. Para que el puerto sobreviva frente a un reinicio del servidor, al final de la línea de comando debes añadir la regla *–permanent* :

    El comando en general se vería así:

    ```bash  
    # firewall-cmd --zone=<zone> --add-port=<port_number>/<protocol> --permanent
    ```

    En este caso este fue el comando utilizado:

    ```bash
    # firewall-cmd --zone=public --add-port=8088/tcp --permanent
    ```

    * Reiniciar el servicio para que los cambios se efectúen:

    ```bash
    # firewall-cmd --reload
    ```
4. Para verificar que el puerto se ha abierto exitosamente se utilizá el siguiente comando:

  ```bash
  # firewall-cmd --list-all
  ```

  En este caso esta fue la salida del comando:

  ![][1]

  Indicando que el puerto 8088 está activo con tcp, en esa misma línea se mostrará los otros puertos que se abran en la máquina.




## Referencias y Enlaces
http://www.grupotelfor.com/blog/7-centos-7/13-linux-how-to-open-a-port-on-rhel-centos-7-firewalld <br>
https://github.com/ICESI-Training/microservices2016b/tree/master/02_intro_flask <br>
https://www.centos.org/download/ <br>
https://guides.github.com/features/mastering-markdown/ <br>


[1]: images/list.PNG
