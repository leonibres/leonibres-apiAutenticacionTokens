---

### **API de Autenticación con Tokens**

Esta es una API desarrollada con Django y Django REST 
Framework que implementa un sistema de autenticación basado en tokens. Permite realizar operaciones básicas como el registro de usuarios, inicio de sesión y consulta del perfil del usuario autenticado.
---

### **Características**
- **Registro de usuarios:** Permite crear nuevos usuarios proporcionando un nombre de usuario, contraseña y correo electrónico.
- **Inicio de sesión:** Genera un token de autenticación para usuarios registrados.
- **Consulta de perfil:** Permite a los usuarios autenticados obtener sus datos personales.
- **Autenticación basada en tokens:** Protege las rutas sensibles mediante tokens de autenticación.

---

### **Requisitos**
- Python 3.10 o superior.
- Django 5.1.7.
- Django REST Framework.
- Entorno virtual configurado.

---

### **Endpoints**
1. **Registro de usuario**
   - **URL:** `/register`
   - **Método:** `POST`
   - **Descripción:** Registra un nuevo usuario y devuelve un token de autenticación.

2. **Inicio de sesión**
   - **URL:** `/login`
   - **Método:** `POST`
   - **Descripción:** Autentica al usuario y devuelve un token de autenticación.

3. **Consulta de perfil**
   - **URL:** `/profile`
   - **Método:** `GET`
   - **Descripción:** Devuelve los datos del usuario autenticado. Requiere un token válido.

4. **Página de inicio**
   - **URL:** `/`
   - **Método:** `GET`
   - **Descripción:** Devuelve un mensaje de bienvenida.

---

### **Cómo usar**
1. Clona este repositorio:
   ```bash
   git clone <https://github.com/leonibres/leonibres-apiAutenticacionTokens.git>
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd apiAutenticaciónTokens
   ```
3. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   source venv/bin/activate  # En Linux/Mac
   ```
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
5. Realiza las migraciones:
   ```bash
   python manage.py migrate
   ```
6. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

---

### **Pruebas**
Puedes usar herramientas como **Postman** o **Thunder Client** para probar los endpoints. Asegúrate de incluir el token de autenticación en las solicitudes protegidas.

---

### **Contribuciones**
Las contribuciones son bienvenidas. Si deseas colaborar, por favor abre un issue o envía un pull request.

---

### **Licencia**
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---
