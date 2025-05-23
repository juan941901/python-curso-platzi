# python-curso-platzi

# Biblioteca estándar de Python (versión 3.12)

La **biblioteca estándar de Python** es el conjunto de módulos y paquetes que se incluyen *por defecto* al instalar Python, sin necesidad de instalaciones adicionales. En la versión 3.12 (y versiones recientes), esta biblioteca es muy amplia y está organizada por categorías funcionales. A continuación se enumeran **todos los módulos estándar** oficialmente listados en la documentación de Python, agrupados por categorías para facilitar su comprensión. (Los nombres de módulos se indican entre comillas invertidas, p. ej. `os`). Todos estos módulos están distribuidos con la instalación base de Python.

## Servicios de procesamiento de texto

* `string` – operaciones comunes con cadenas de texto.
* `re` – expresiones regulares (regex).
* `difflib` – cálculo de diferencias (comparación de texto).
* `textwrap` – formato de texto en párrafos.
* `unicodedata` – base de datos Unicode.
* `stringprep` – preparación de cadenas para protocolos.
* `readline`, `rlcompleter` – entrada interactiva y autocompletado.

## Servicios de datos binarios

* `struct` – empaquetado de datos binarios.
* `codecs` – codificación y decodificación de datos.

## Tipos de datos

* `datetime`, `zoneinfo`, `calendar` – manejo de fechas y zonas horarias.
* `collections`, `collections.abc` – tipos de contenedores.
* `heapq`, `bisect`, `array` – estructuras de datos eficientes.
* `weakref`, `types`, `copy`, `pprint`, `reprlib` – referencia, copia, representación.
* `enum`, `graphlib` – enumeraciones y grafos.

## Módulos numéricos y matemáticos

* `numbers`, `math`, `cmath` – funciones matemáticas y complejos.
* `decimal`, `fractions`, `random`, `statistics` – números precisos y estadística.

## Programación funcional

* `itertools`, `functools`, `operator` – herramientas de alto orden.

## Acceso a archivos y directorios

* `pathlib`, `os.path`, `stat`, `filecmp`, `tempfile`, `glob`, `fnmatch`, `linecache`, `shutil` – manejo de archivos y rutas.

## Persistencia de datos

* `pickle`, `copyreg`, `shelve`, `marshal` – serialización.
* `dbm`, `sqlite3` – almacenamiento y bases de datos simples.

## Compresión y archivado de datos

* `zlib`, `gzip`, `bz2`, `lzma` – compresión.
* `zipfile`, `tarfile` – archivos comprimidos.

## Formatos de archivos

* `csv`, `configparser`, `tomllib`, `netrc`, `plistlib` – lectura/escritura de formatos comunes.

## Servicios criptográficos

* `hashlib`, `hmac`, `secrets` – hash, autenticación y generación de secretos.

## Servicios del sistema operativo

* `os`, `io`, `time`, `logging`, `platform`, `errno`, `ctypes` – funciones de sistema.
* `logging.config`, `logging.handlers` – configuración avanzada de logs.

## Línea de comandos

* `argparse`, `optparse`, `getpass`, `fileinput`, `curses`, `curses.textpad`, `curses.ascii`, `curses.panel` – herramientas CLI.

## Ejecución concurrente

* `threading`, `multiprocessing`, `subprocess`, `sched`, `queue`, `contextvars`, `_thread`, `concurrent.futures` – paralelismo y tareas.
* `multiprocessing.shared_memory` – memoria compartida entre procesos.

## Redes y comunicación entre procesos

* `asyncio`, `socket`, `ssl`, `select`, `selectors`, `signal`, `mmap` – redes, asíncrono y memoria compartida.

## Datos de Internet

* `email`, `json`, `mailbox`, `mimetypes`, `base64`, `binascii`, `quopri` – formatos de datos comunes en la web.

## Procesamiento de marcado estructurado

* `html`, `html.parser`, `html.entities` – manejo de HTML.
* `xml.etree.ElementTree`, `xml.dom`, `xml.dom.minidom`, `xml.dom.pulldom`, `xml.sax`, `xml.parsers.expat` – procesamiento de XML.

## Protocolos de Internet

* `webbrowser`, `wsgiref`, `urllib`, `urllib.request`, `urllib.response`, `urllib.parse`, `urllib.error`, `http`, `http.client`, `http.server`, `ftplib`, `poplib`, `imaplib`, `nntplib`, `smtplib`, `uuid`, `socketserver`, `xmlrpc`, `ipaddress`, `email`, `cgi`, `cgitb` – navegación, HTTP y correo.

## Herramientas para pruebas

* `unittest`, `doctest`, `unittest.mock`, `test` – pruebas automatizadas.

## Depuración y perfilado

* `bdb`, `faulthandler`, `pdb`, `timeit`, `trace`, `tracemalloc`, `profile`, `cProfile` – debugging y medición de rendimiento.

## Entorno de ejecución de Python

* `sys`, `builtins`, `__main__`, `warnings`, `contextlib`, `abc`, `atexit`, `traceback`, `site`, `__future__`, `gc`, `inspect`, `sysconfig`, `types`, `platform`, `importlib` – introspección y entorno.

## Importación de módulos

* `importlib`, `pkgutil`, `modulefinder`, `runpy`, `zipimport` – control de importaciones.

## Módulos para compilación

* `compileall`, `py_compile`, `dis`, `opcode`, `ast`, `symtable`, `token`, `tokenize` – compilación de código.

## Extensiones en C/C++ y Python embebido

* `ctypes`, `cffi`, `cython`, `pybind11` (no todos son parte del core, algunos son externos).
