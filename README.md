# QA Automation — Lebane

## Descripción del proyecto

Este repositorio contiene pruebas automatizadas para la plataforma **Lebane**, una aplicación de gestión para empresas constructoras y desarrolladoras inmobiliarias.

El proyecto forma parte del ejercicio técnico de QA Automation y tiene como objetivo validar funcionalidades relacionadas con la creación de proyectos y la gestión de listas de precios y unidades.

Las pruebas se desarrollan utilizando **Python, Selenium WebDriver y Pytest**, con foco en la validación funcional de los principales flujos de la aplicación.

## Tecnologías utilizadas

- **Python:** lenguaje de programación utilizado para desarrollar los tests.
- **Selenium WebDriver:** automatización de la interacción con el navegador.
- **Pytest:** ejecución y organización de las pruebas automatizadas.
- **Google Chrome:** navegador utilizado para ejecutar los tests.
- **Git y GitHub:** control de versiones y almacenamiento del proyecto.

## Ambiente de pruebas

- **Aplicación:** [Lebane — Ambiente de testing](https://tst.lebane.app)
- **Navegador:** Google Chrome.
- **Credenciales:** las proporcionadas para el ejercicio técnico.

> Por seguridad, las credenciales de acceso no deben incluirse en el repositorio.

## Estructura del proyecto

```text
QA-Automation-Lebane/
│
├── Test/
│   ├── Test_validar_login.py
│   ├── Test_crear_proyecto.py
│   └── __init__.py
│
├── Utils/
│   └── __init__.py
│
├── conftest.py
├── .gitignore
└── README.md
```

- **Test/**: contiene los casos de prueba automatizados.
- **Test_validar_login.py**: valida el inicio de sesión en la aplicación.
- **Test_crear_proyecto.py**: automatiza el flujo de acceso al formulario de creación de proyectos y las validaciones correspondientes.
- **Utils/**: destinada a las funciones auxiliares reutilizables.
- **conftest.py**: contiene la configuración y los fixtures compartidos por los tests.
- **.gitignore**: excluye del control de versiones los archivos y carpetas que no deben subirse al repositorio.

## Casos de prueba implementados

### 1. Validación de inicio de sesión

**Objetivo:** verificar que el usuario pueda iniciar sesión correctamente.

Validaciones principales:

- Acceso a la aplicación.
- Envío de las credenciales.
- Inicio de sesión exitoso.

### 2. Creación de un nuevo proyecto

**Objetivo:** validar el flujo de acceso y creación de un proyecto.

Validaciones principales:

- Inicio de sesión previo.
- Visualización de la página principal.
- Selección de la opción «Agregar proyecto».
- Redirección al formulario de creación.
- Verificación de la URL y del título del formulario.
- Validación del flujo de creación del proyecto.

## Escenarios contemplados para la funcionalidad de listas de precios

De acuerdo con los requerimientos del ejercicio, la cobertura funcional debe ampliarse para incluir los siguientes escenarios:

| ID | Escenario | Resultado esperado |
|---|---|---|
| CP-03 | Crear un proyecto con lista de precios inicial | Se crea el proyecto y su lista de precios inicial. |
| CP-04 | Agregar una unidad manualmente | La unidad aparece con el precio ingresado. |
| CP-05 | Cargar unidades mediante un archivo Excel | Se crea una nueva lista con las unidades del archivo. |
| CP-06 | Modificar el precio de una unidad | El precio actualizado se refleja en la lista correspondiente. |
| CP-07 | Eliminar una unidad de una lista | La unidad desaparece y la lista continúa existiendo si contiene otras unidades. |
| CP-08 | Eliminar la última unidad de una lista | La lista de precios se elimina automáticamente. |
| CP-09 | Verificar la eliminación de una unidad sin lista de precios | La unidad también se elimina, según la regla de negocio. |

Estos escenarios representan la cobertura funcional prevista para completar el ejercicio; deben considerarse pendientes hasta que sus respectivas pruebas automatizadas estén implementadas y ejecutadas.

## Casos adicionales que se podrían probar

Además de los escenarios solicitados, propongo evaluar los siguientes casos:

- **Datos obligatorios vacíos:** verificar que el sistema impida guardar un proyecto o una unidad cuando falten campos requeridos.
- **Precios inválidos:** comprobar que no se acepten valores negativos, texto u otros formatos no permitidos.
- **Precios iguales a cero:** validar el comportamiento del sistema cuando se ingresa un precio de cero.
- **Archivo Excel inválido:** verificar el manejo de archivos con formato incorrecto, estructura incompleta o sin datos.
- **Archivo Excel sin unidades:** comprobar que el sistema informe adecuadamente cuando el archivo no contiene registros para importar.
- **Nombres duplicados:** evaluar si se permiten proyectos, listas o unidades con nombres repetidos.
- **Persistencia de los cambios:** comprobar que los precios y las unidades continúen actualizados después de recargar la página.
- **Mensajes de confirmación y error:** validar que las operaciones informen claramente si finalizaron correctamente o si ocurrió un problema.

Estos casos adicionales ayudarían a detectar errores de validación, integridad de datos y experiencia de usuario.

## Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/Jimeromero21/QA-Automation-Lebane.git
cd QA-Automation-Lebane
```

### 2. Crear un entorno virtual

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```bash
python -m pip install selenium pytest
```

Si el proyecto incorpora nuevas dependencias, deberán agregarse a un archivo `requirements.txt` para facilitar la instalación reproducible del entorno.

## Ejecución de las pruebas

Para ejecutar todos los tests desde la raíz del repositorio:

```bash
python -m pytest -v
```

Para ejecutar únicamente la prueba de inicio de sesión:

```bash
python -m pytest -v Test/Test_validar_login.py
```

Para ejecutar únicamente la prueba de creación de proyecto:

```bash
python -m pytest -v Test/Test_crear_proyecto.py
```

La opción `-v` permite visualizar el nombre y el resultado de cada prueba ejecutada.

## Decisiones de diseño

- **Separación de responsabilidades:** los tests se organizan por funcionalidad para facilitar su mantenimiento.
- **Reutilización de funciones:** las acciones comunes, como el inicio de sesión, se centralizan en funciones auxiliares cuando corresponde.
- **Esperas explícitas:** se utilizan esperas de Selenium para interactuar con elementos cuando están disponibles, evitando depender exclusivamente de pausas fijas.
- **Aserciones:** se validan las URLs, los elementos visibles y los resultados esperados de cada flujo.
- **Fixtures compartidos:** la configuración del navegador se centraliza para reutilizarla entre diferentes pruebas.
- **Control de versiones:** los cambios se registran mediante Git y se publican en GitHub.

## Próximas mejoras

- Completar la automatización de los siete escenarios requeridos para listas de precios y unidades.
- Incorporar datos de prueba reutilizables y únicos para evitar duplicados.
- Agregar validaciones negativas y casos límite.
- Generar reportes de ejecución.
- Incorporar un archivo `requirements.txt`.
- Mejorar la gestión de errores y las evidencias de fallos.

## Repositorio

[QA-Automation-Lebane — GitHub](https://github.com/Jimeromero21/QA-Automation-Lebane)

Proyecto desarrollado como parte de un ejercicio técnico de QA Automation, utilizando Python, Selenium WebDriver y Pytest.
