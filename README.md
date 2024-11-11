Aquí creo un método que inserta un nuevo usuario con los datos (nombre, apellido, email, descripción y sueldo) en la tabla usuarios de la base de datos.
![Texto alternativo](imagenes/create.png)

Método que elimina la tabla usuarios si ya existe y lugo crea una nueva tabla usuarios con las columnas id, nombre, apellido, email, descripcion y sueldo en la base de datos.
![Texto alternativo](imagenes/create_table.png)

Este método elimina un usuario por su ID que luego devuelve un mensaje de confirmación a la hora de realizarse correctamente.
![Texto alternativo](imagenes/delete.png)

Aquí leemos los usuarios que hay en la tabla y los imprime uno por uno.
![Texto alternativo](imagenes/read.png)

Actualizamos la descripción y/o el salario de un usuario en la tabla de usuarios según el usuario_id que hayamos escrito.
![Texto alternativo](imagenes/update.png)

Y estos son los ajustes del docker y el contenedor.
![Texto alternativo](imagenes/docker_compose.png)
