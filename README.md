# Sistema de Registro de Visitantes

Aplicación de escritorio desarrollada en Python utilizando Tkinter, que permite gestionar el registro de visitantes en una oficina mediante operaciones CRUD (Crear, Leer, Eliminar).

## 🧩 Arquitectura

El proyecto está organizado en capas siguiendo buenas prácticas de Programación Orientada a Objetos:

visitas_app/
│
├── main.py
├── modelos/
│   └── visitante.py
├── servicios/
│   └── visita_servicio.py
└── ui/
    └── app_tkinter.py

- Modelos: Definición de la clase Visitante.
- Servicios: Lógica del sistema (CRUD).
- UI: Interfaz gráfica con Tkinter.
- Main: Punto de entrada del programa.

## ⚙️ Requisitos

- Python 3.x
- Librería Tkinter (incluida en Python)

## 🚀 Cómo ejecutar

1. Clonar el repositorio:
   git clone https://github.com/TU-USUARIO/tarea_poo_visitas.git

2. Ingresar a la carpeta:
   cd visitas_app

3. Ejecutar el programa:
   python main.py

## ✅ Funcionalidades

- Registrar visitantes
- Visualizar lista en tabla
- Eliminar registros
- Limpiar campos del formulario
- Validación de datos

## 👨‍💻 Autor

Luis Asencio
