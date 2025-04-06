# FacturDash

[![Screenshot-from-2025-04-06-23-42-37.png](https://i.postimg.cc/QCkVyHzs/Screenshot-from-2025-04-06-23-42-37.png)](https://postimg.cc/T51RyYGH)

FacturDash es una herramienta diseñada para extraer información clave de facturas normalizadas. Como no tenia facturas cree un script (generate.py) para generarlas normalizadas, para normalizar facturas normales tomariamos ese modelo y a traves de un modelo GPT de OpenAI las normalizamos. A partir de ahí, al ejecutar app.py genera un dashboard interactiva con las métricas mas importantes. Todo el código está en mi GitHub. Para cualquier problema o propuesta: juanglezm3@gmail.com

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Vas a necesitar una api-keys: (solo si tienes que normalizar tus facturas, contactarme para ello, tengo que añadir el script para hacerlo ya que esto
es solo una demostración)

* [OpenAI Api-Key](https://platform.openai.com/api-keys) -> Enlace para obtenerla.

En primer lugar crea un archivo .env, ahí guardaras tus claves con el siguiente par clave valor:

* OPENAI_API_KEY = "tu_api_key" (esta será tu api_key de Google Places, no cambies el nombre)

### Pre-requisitos 📋

Todos los requerimientos estan en requirements.txt:
```bash
  pip install -r requirements.txt
```
He utilizado python 3.12.3, para perfecta compatibilidad utilizar misma versión.

### Instalación 🔧

_Creamos un virtual environment_

_Linux/MacOS:_

```
python3 -m venv nombre_venv
source nombre_venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

_Windows_

```
python3 -m venv nombre_venv
nombre venv\Scripts\activate.bat
pip install -r requirements.txt
python3 app.py
```

_Ya tendrias la herramienta corriendo en tu maquina local_

## Construido con 🛠️

* [Flask](https://flask.palletsprojects.com/en/stable/) - El framework web usado
* [fitz](https://pythonclcoding.medium.com/pdf-manipulation-using-python-fitz-library-619227d59f3d) - Procesamiento de archivos PDF
* [re](https://docs.python.org/3/library/re.html) - Operaciones con expresiones regulares
* [Chart.js](https://www.chartjs.org/) - Visualización interactiva de datos


## Licencia 📄

Mira el archivo [LICENSE.md](LICENSE.md) para detalles. Si quieres usar esta herramienta para tu uso personal, agrega un enlace a este repositorio en tu readme por favor. Espero que sea de utilidad.

## Mis redes sociales 🌐

* Comenta a otros sobre este proyecto 📢
* Mis redes sociales son: 
* [Tiktok](https://www.tiktok.com/@jgmdev) 
* [Linkedin](https://www.linkedin.com/in/jgmdatascience/) 
