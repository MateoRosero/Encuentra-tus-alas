# Proyecto de Inventario y Gestión de Vuelos

Este proyecto es una aplicación web desarrollada con Flask que permite gestionar un inventario de productos y administrar vuelos y reservas. Incluye funcionalidades para usuarios con diferentes roles, como pasajeros, aerolíneas y administradores, además de una funcionalidad de check-in para los pasajeros y el administrador puede generar un reporte de discrepancias con el check-in y filtrar por fecha.

## Características

- **Gestión de Usuarios**: Registro, inicio de sesión y roles de usuario (pasajero, aerolínea, administrador).
- **Gestión de Vuelos**: Las aerolíneas pueden crear y editar vuelos.
- **Reservas de Vuelos**: Los usuarios pueden buscar vuelos y realizar reservas.
- **Check-In**: Funcionalidad para realizar el check-in de reservas.
- **Panel de Administración**: Los administradores pueden gestionar usuarios y generar reportes de discrepancias.

## Requisitos

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Login
- MySQL

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd Crud-inventario/Inventario
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Configura la base de datos en `app.py`:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario:contraseña@localhost/dbInventario'
   ```
5. Ejecuta la aplicación:
   ```bash
   python src/app.py
   ```

## Uso

- **Inicio de Sesión**: Accede a la aplicación y utiliza las credenciales para iniciar sesión.
- **Registro**: Crea una cuenta nueva con un rol asignado automáticamente según el correo electrónico.
- **Gestión de Productos**: Añade, edita y visualiza productos desde el panel de usuario.
- **Gestión de Vuelos**: Las aerolíneas pueden gestionar vuelos desde su panel exclusivo.
- **Reservas**: Busca y reserva vuelos disponibles.
- **Check-In**: Realiza el check-in de tus reservas.
- **Administración**: Los administradores pueden gestionar usuarios y ver reportes de discrepancias.

## Roles de Usuario

- **Pasajero**: Puede gestionar su inventario de productos y realizar reservas de vuelos.
- **Aerolínea**: Puede crear y editar vuelos.
- **Administrador**: Tiene acceso a todas las funcionalidades, incluyendo la gestión de usuarios y reportes.

## Seguridad

- Las contraseñas se almacenan de forma segura utilizando `werkzeug.security`.
- Se requiere autenticación para acceder a la mayoría de las rutas.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Autor

- **Nombre**: André Rosero
- **Correo**: andre.rosero@udla.edu.ec

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
