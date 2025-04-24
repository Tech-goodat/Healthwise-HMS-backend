# 🏥 Healthwise HMS API

A basic Health Information System API built with **Flask**. This system allows doctors to manage clients and create health programs. It includes secure user authentication, client management, and RESTful endpoints for integration.

---

## 🚀 Features

- 🔐 Doctor Signup & Login (JWT authentication)
- 🧑‍⚕️ Client Registration (by doctors only)
- 🔍 Search Clients by Username
- 📂 Create Health Programs
- 📬 Expose Client Profile via Email (for integration with other systems)

---

## 🛠 Tech Stack

- **Flask** (REST API)
- **Flask-JWT-Extended** (Authentication)
- **Flask-Bcrypt** (Password Hashing)
- **SQLAlchemy** (ORM)
- **Flask-Migrate** (Database Migrations)
- **SQLite** (Database)
- **CORS Support** (for frontend integration)

---

## 📦 Installation & Setup

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/healthwise-api.git
cd healthwise-api
```

2. **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Database Setup**

```bash
flask db init
flask db migrate
flask db upgrade
```

5. **Run the Application**

```bash
python app.py
```

Visit: `http://localhost:5555/`

---

## 📚 API Endpoints

### 🌐 Index

```http
GET /
```
Returns: "Welcome to Healthwise HMS API!"

---

## 👨‍⚕️ Doctor Authentication

### Signup

```http
POST /doc_signup
```

**Request Body:**

```json
{
  "username": "drsmith",
  "email": "drsmith@example.com",
  "department": "Pediatrics",
  "description": "Expert in child care",
  "phone_number": "0712345678",
  "profile_picture": "https://link.to/image.jpg",
  "password": "securepassword"
}
```

### Login

```http
POST /doc_login
```

**Request Body:**

```json
{
  "email": "drsmith@example.com",
  "password": "securepassword"
}
```

Returns JWT token and doctor profile.

---

## 👩‍⚕️ Client Management

### Register a Client (Doctors only)

```http
POST /client_signup
```

🔒 Requires `Authorization: Bearer <token>`

**Request Body:**

```json
{
  "username": "janedoe",
  "email": "jane@example.com",
  "phone_number": "0700000000",
  "gender": "female",
  "age": 28
}
```

### Search Clients by Username

```http
GET /client_search/<query>
```

**Example:**

```http
GET /client_search/jane
```

🔒 Requires `Authorization: Bearer <token>`

### Get Client Profile by Email

```http
GET /client_profile/<email>
```

**Example:**

```http
GET /client_profile/jane@example.com
```

🔒 Requires `Authorization: Bearer <token>`

---

## 📘 Programs

### Create Health Program

```http
POST /program
```

🔒 Requires `Authorization: Bearer <token>`

**Request Body:**

```json
{
  "name": "Mental Health Support",
  "description": "Program for mental health awareness",
  "slogan": "Your mind matters",
  "program_manager": "drsmith@example.com"
}
```

---

## 🔐 Authentication

After login or signup, you will receive a JWT token:

```json
{
  "access_token": "your.jwt.token"
}
```

Use it for protected endpoints:

```http
Authorization: Bearer <your.jwt.token>
```

---

## 👥 Models

### 🧑‍⚕️ Docs

- `username`
- `email`
- `department`
- `description`
- `phone_number`
- `profile_picture`
- `password`

### 👤 Client

- `username`
- `email`
- `phone_number`
- `gender`
- `age`

### 📘 Program

- `name`
- `description`
- `slogan`
- `program_manager`

---

## 📬 Client Profile Exposure

Expose a client’s profile by email (if authenticated):

```http
GET /client_profile/jane@example.com
```

Useful for frontend dashboards and integration.

---

## 🧪 Testing

Use Postman or `curl`:

```bash
curl -H "Authorization: Bearer <token>" http://localhost:5555/client_profile/jane@example.com
```

---

## 📄 License

MIT License – Free to use, modify, and distribute.

---

## 🤝 Contributing

Pull requests are welcome! Please ensure your code is clean and documented.

