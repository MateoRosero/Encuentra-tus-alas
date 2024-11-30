# CRUD Inventario

Este proyecto es una aplicación web para la gestión de inventario y usuarios, desarrollada con Flask y MySQL. Permite a los usuarios registrarse, iniciar sesión, y gestionar productos en su inventario. Los administradores tienen privilegios adicionales para gestionar usuarios y sus roles.

## Características

- **Autenticación de Usuarios**: Registro, inicio de sesión y cierre de sesión.
- **Gestión de Vuelos**: Crear, editar y eliminar vuelos.
- **Roles de Usuario**: Asignación de roles como 'admin', 'airline', y 'passenger'.
- **Interfaz de Administración**: Los administradores pueden ver y gestionar todos los usuarios.

## Tecnologías Utilizadas

- **Backend**: Flask
- **Base de Datos**: MySQL
- **Frontend**: HTML, CSS, Bootstrap
- **Autenticación**: Flask-Login
- **Seguridad**: Werkzeug para el hash de contraseñas

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/Crud-inventario.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd Crud-inventario/Inventario
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura la base de datos en `src/app.py` y `src/database.py` con tus credenciales de MySQL.

5. Crea las tablas de la base de datos:
   ```bash
   python src/app.py
   ```

## Uso

1. Ejecuta la aplicación:
   ```bash
   python src/app.py
   ```

2. Abre tu navegador y ve a `http://localhost:5000`.

3. Regístrate o inicia sesión para comenzar a usar la aplicación.

## Estructura del Proyecto

- `src/app.py`: Archivo principal de la aplicación Flask.
- `src/templates/`: Contiene las plantillas HTML para las diferentes vistas.
- `src/database.py`: Configuración de la conexión a la base de datos MySQL.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
