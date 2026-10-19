# Playwright con Python — Ejercicios 1 al 8

**Materia:** Validación y Verificación de Programas  
**Institución:** CENT 35 "Prof. Julián José Godoy"  
**Carrera:** Desarrollo de Software — 3° año  
**Alumno:** Karim Homsi

## Objetivo

Migrar a Python los ocho ejercicios realizados previamente con
Playwright y Java, incorporando pruebas automatizadas y evidencias.

## Tecnologías

- Python 3.12.10.
- Playwright.
- pytest y pytest-playwright.
- Visual Studio Code.
- Git y GitHub.

## Ejercicios

1. Navegar a una página.
2. Obtener y verificar el título.
3. Hacer clic en un enlace.
4. Completar un campo con fill.
5. Login completo: escenario exitoso y contraseña incorrecta.
6. Verificar que un mensaje sea visible.
7. Guardar una captura de pantalla.
8. Navegar mediante enlaces y regresar con go_back.

La suite contiene nueve pruebas, porque el ejercicio 5 tiene dos escenarios.

## Organización

- `tests/`: pruebas de los ocho ejercicios.
- `pages/login_page.py`: Page Object reutilizado en los ejercicios 5, 6 y 7.
- `pytest.ini`: configuración de descubrimiento, trazas y capturas ante fallas.
- `requirements.txt`: dependencias y versiones.
- `.gitignore`: exclusión del entorno virtual, cachés y evidencias generadas.

## Instalación en Windows

Desde la raíz del proyecto:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m playwright install chromium
```

## Ejecutar todas las pruebas

Sin mostrar el navegador:

```powershell
.\.venv\Scripts\python.exe -m pytest
```

Mostrando el navegador y ralentizando las acciones:

```powershell
.\.venv\Scripts\python.exe -m pytest --headed --slowmo 500
```

## Evidencias

- Captura del ejercicio 7: `screenshots/ejercicio07-login-exitoso.png`.
- Trazas de las pruebas: dentro de `test-results/`.
- Capturas automáticas ante fallas: dentro de `test-results/`.

Estas evidencias se generan localmente y no se incluyen en el repositorio.