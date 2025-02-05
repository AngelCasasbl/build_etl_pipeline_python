# Proyecto de Migración Recurrente entre MySQL y PostgreSQL

## Descripción
Este proyecto tiene como objetivo la simulación de una migración recurrente de datos desde una base de datos MySQL hacia PostgreSQL. Se enfoca en la actualización total de las tablas `employees`, `dept_manager`, `dept_emp`, `salaries` y `titles`. Aunque el código se ejecuta manualmente, lo recomendable es programar su ejecución utilizando herramientas como Docker, cron jobs o Apache Airflow para mayor automatización y eficiencia.

> **Nota:** Este código está basado en una adaptación de diversos recursos y metodologías disponibles en línea.

## Tecnologías Utilizadas
- **Python** (versión recomendada: 3.x)
- **SQLAlchemy** para la conexión a bases de datos
- **pandas** para la manipulación de datos
- **pymysql** para la conexión con MySQL
- **dotenv** para la gestión de variables de entorno
- **PostgreSQL** y **MySQL** como bases de datos destino y origen
- **Docker, cron jobs, Apache Airflow** (opcional para automatización)

## Estructura del Proyecto
```
/
|-- main.py  # Archivo principal con la lógica de ETL
|-- .env     # Archivo con las variables de entorno (no debe subirse a repositorios públicos)
|-- requirements.txt  # Dependencias del proyecto
|-- Dockerfile  # Archivo de configuración para ejecutar en Docker (opcional)
|-- README.md  # Documentación del proyecto
```

## Instalación y Configuración
### 1. Clonar el Repositorio
```bash
git clone https://github.com/AngelCasasbl/build_etl_pipeline_python.git
cd build_etl_pipeline_python
```

### 2. Crear un Entorno Virtual (Opcional pero Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate  # En Windows
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno
Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:
```ini
# Credenciales de PostgreSQL
PGUSER=tu_usuario
PGPASS=tu_contraseña
PGHOST=tu_host
PGPORT=5432
PGDB=tu_base_de_datos

# Credenciales de MySQL
MyUSER=tu_usuario
MyPASS=tu_contraseña
MyHOST=tu_host
MyPORT=3306
MyDB=tu_base_de_datos
```

## Uso del Proyecto
Ejecutar el script principal:
```bash
python main.py
```

El script realiza las siguientes acciones:
1. Carga las variables de entorno.
2. Establece la conexión con MySQL y PostgreSQL.
3. Extrae los datos de las tablas `employees`, `dept_manager`, `dept_emp`, `salaries` y `titles` de MySQL.
4. Carga los datos en PostgreSQL con el prefijo `stg_` en cada tabla.
5. Muestra mensajes en consola sobre el estado del proceso.

## Automatización del Proyecto
Para programar la ejecución automática del script, se pueden utilizar las siguientes opciones:
- **Cron Jobs (Linux)**: Agregar una tarea cron para ejecutar el script en intervalos regulares.
- **Apache Airflow**: Definir un DAG que ejecute el proceso con dependencias controladas.
- **Docker**: Contenerizar el proceso para facilitar su despliegue en diferentes entornos.


## Funciones Principales
### `test_connection(engine)`
Verifica la conexión a la base de datos especificada.

### `extract_mysql()`
- Se conecta a MySQL.
- Obtiene las tablas requeridas.
- Extrae los datos y los envía a PostgreSQL.

### `load_in_postgres(df, tbl)`
- Se conecta a PostgreSQL.
- Carga los datos extraídos en una tabla temporal (`stg_<nombre_tabla>`).

## Posibles Errores y Soluciones
- **Error de conexión**: Verifica que las credenciales y los puertos sean correctos.
- **Tabla no encontrada**: Asegúrate de que las tablas existen en la base de datos de origen.
- **Error de dependencias**: Ejecuta `pip install -r requirements.txt` nuevamente.

## Contribución
Si deseas contribuir, por favor sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una rama con tu función (`git checkout -b mi-funcionalidad`).
3. Realiza tus cambios y confirma (`git commit -m 'Agregada nueva funcionalidad'`).
4. Sube tus cambios (`git push origin mi-funcionalidad`).
5. Abre un Pull Request.

## Licencia
Puedes usarlo y modificarlo libremente.

## Autor
[Luis angel casas ballestas] - [Angelcasasbl@gmail.com]

