# PCM Restaurante - v. 1.0



## Autor
Javier Revilla
jrevilla55@gmail.com
- Creado:         28 Oct 2019
- Actualizado:   	8 Nov 2019


## Sitio web en Heroku
https://pcm-restaurant-jrevilla.herokuapp.com


## Documentación Django
- https://docs.djangoproject.com/es/2.2/	(ES)



## Descripción
- Aplicación web para la atención de menús de restaurantes.
- Para asistir a los Mozos y Cocineros, en sus tareas cotidianas.


## Descripción Orientada Objeto
- Existen 3 Clases fundamentales: Menu, Item (platos) y Familia. 

- Familias: los tipos de platos que van a ser manejados en el Restaurante. 
	- Campos
		- name
		- idx (ordenamiento)

- Item: el plato en sí. 
	- Campos
		- name
		- family (relación ManyToMany)
		- description 
		- price
		- image
		- notes_cook
		- notes_waiter

- Menu: el menú del día. Contiene los diferentes platos que se van a servir durante el día. 
	- Campos
		- name 
		- date 
		- items	(relación ManyToMany)
		- family (auxiliar)

## Manejo de imágenes por URL
- Todas la imágenes son URLs que pueden ser modificados por el usuario. 
- Actualmente, mis imágenes están en Cloudinary (https://cloudinary.com/).
- Pero el usuario puede utilizar cualquier repositorio. 



## Arquitectura
- Base de Datos: Postgres.
- Hosting en la nube: Heroku. 
- Plataforma de desarrollo: Django-Python. 
- Repositorio del código fuente: GitHub.


## Dependencias
- Whitenoise 		(https://github.com/evansd/whitenoise).
- Gunicorn 			(https://github.com/benoitc/gunicorn).
- Dj-Database-Url 	(https://github.com/jacobian/dj-database-url).
- Psycopg2 			(https://github.com/psycopg/psycopg2)
- Pytz				(https://github.com/stub42/pytz)
- Sqlparse			(https://github.com/andialbrecht/sqlparse)
- ProjetoLMS		(https://github.com/adrriano/projeto-lms-pagina-principal)



## Tests
- Django tiene herramientas sofisticadas para la construcción de Tests unitarios y de integración
- Incluímos algunos tests que verifican el funcionamiento de las páginas HTML generadas por el servidor. 
- También testeamos algunas funciones de nuestros Clases. 
'''
	python manage.py test
'''


Desafío 
--------
Desarrollar una aplicación web para la atención de menús de restaurantes.


Recomendaciones
----------------
- **Utilizar cualquier base de datos y cualquier lenguaje de programación.**

- Desplegar en algún proveedor gratuito, ejemplo: https://heroku.com 

- Poner el código fuente en github.com
	- Agregar como desarrollador a: lab51.epic@gmail.com 


- No es necesario 
	- registro de usuarios
	- cobros en línea ni facturación ni reportes. 

- Usuarios o vistas para:
	- Mozo 
	- Cocinero 

- Trata de hacer una aplicación mínima pero intuitiva, pensando más en el Mozo y Cocinero como usuarios.


## Entregables
1. Código fuente en Github
2. Aplicación web funcionando (url) de preferencia en Heroku


## Tiempo máximo
	Viernes 08 al final del día.


