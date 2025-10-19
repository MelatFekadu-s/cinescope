# 🎬 CineScope API

CineScope is a RESTful API built with **Django** and **Django REST Framework (DRF)** that allows users to manage movies, post reviews, and interact with other users’ movie opinions. It’s designed to provide a clean and scalable backend for any movie-related application — from review aggregators to recommendation engines.

---

## 🚀 Features

- 🔹 **Movies Management**
  - Add, update, delete, and list movies
- 🔹 **Reviews Management**
  - Add, edit, and delete reviews
  - View reviews per movie
  - Filter and sort reviews
- 🔹 **User Management**
  - Create and manage user accounts
  - View reviews by user
- 🔹 **Authentication**
  - Secure endpoints with JWT or session-based auth (Week 4 feature)
- 🔹 **Database**
  - SQLite for development
  - PostgreSQL for production
- 🔹 **Deployment**
  - Deployed on Heroku or PythonAnywhere

---

## 🏗️ Tech Stack

| Component | Technology |
|------------|-------------|
| Backend Framework | Django + Django REST Framework |
| Database (Dev) | SQLite |
| Database (Prod) | PostgreSQL |
| Deployment | Heroku / PythonAnywhere |
| Authentication | Django Auth / JWT |

---

## 🧱 Models

### 1. **User**
- `id`
- `username`
- `email`
- `password`
- `date_joined`

### 2. **Movie**
- `id`
- `title`
- `description`
- `release_date`
- `genre`
- `created_at`

### 3. **Review**
- `id`
- `user` (ForeignKey → User)
- `movie` (ForeignKey → Movie)
- `rating` (IntegerField)
- `comment` (TextField)
- `created_at`

---

## 🔗 API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/movies/` | GET, POST | List or create movies |
| `/movies/{id}/` | GET, PUT, DELETE | Retrieve, update, or delete a movie |
| `/movies/{id}/reviews/` | GET | List all reviews for a movie |
| `/reviews/` | GET, POST | List or create reviews |
| `/reviews/{id}/` | GET, PUT, DELETE | Manage a specific review |
| `/users/` | GET, POST | List or create users |
| `/users/{id}/reviews/` | GET | List reviews by a specific user |

---

## 🗓️ Project Timeline

| Week | Tasks |
|------|-------|
| **Week 1** | Setup project, create models, and configure settings |
| **Week 2** | Implement core endpoints for movies, users, and reviews |
| **Week 3** | Add filtering and sorting for reviews (e.g., by rating or date) |
| **Week 4** | Add authentication (JWT/session), user permissions, and secure routes |
| **Week 5** | Deploy the app to Heroku or PythonAnywhere and perform final testing |

---

