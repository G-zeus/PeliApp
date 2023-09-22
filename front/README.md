# FrontEnd

Se realizó una pequeña aplicación con React.js donde se consume una rest api 
que funciona como proxy en el consumo de los servicios de [themoviedb](https://www.themoviedb.org/),.

## Configuración del proyecto
### Instalación de dependencias
Se deben instalar las dependencias de node para el correcto funcionamiento
``` shell
cd front && npm install
```
### Configuración de variables
Se deben configurar las variables del archivo .env donde

```
REACT_APP_API_URL= 'URL_del_servicio_FastApi'
```

Para tener el archivo .env y sus variables basta con

```shell
cp .env.example .env
```

### Levantar el servidor

Solo resta correr el servido de vue con

```shell
npm run serve
```


