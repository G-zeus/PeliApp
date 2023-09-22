# BackEnd

Api rest construida con FastApi para consumir la informacion [themoviedb](https://www.themoviedb.org/). Se implementó el patron de diseño adapter para manejar el fetch de datos. 
## Configuración del proyecto
Lo primero es instalar las dependencias de python que se encuentran en el archivo [requirements.txt](requirements.txt). Se recomienda usar un ambiente virtual con la version **3.10** de **Python**
``` shell
python3 -m venv .venv
source .venv/bin/activate 
pip install -r requirements.txt
```
### Configuración de variables
Se deben configurar las variables del archivo .env donde

```
TMDB_API_URL="https://api.themoviedb.org/3"
TMDB_IMG_URL="https://image.tmdb.org/t/p/w300"
TMDB_AUTH_TOKEN="Bearer tmdb_Access_Token "
```
*Para obtener el tmdb_Access_Token es necesario estar registrado en [themoviedb](https://www.themoviedb.org/) y entrar [aqui](https://www.themoviedb.org/settings/api) para obtenerlo*


Para tener el archivo .env y sus variables basta con

```shell
cp .env.example .env
```

### Levantar el servidor

Solo resta correr el servido de Flask con el comando

```
uvicorn app:app 
```


