# Week 4 — Flask API (Weather & History Microservice)

A simple Flask API project built as part of my API Learning Series (Week 4).
This week focuses on understanding how APIs work **from the server side** — building and running your own REST endpoints instead of just consuming them.

---

## 📚 Overview

The goal of Week 4 is to learn **backend fundamentals** using Flask:

* How an API server handles HTTP methods (GET, POST, etc.)
* How to return JSON responses, errors, and metadata
* How to structure and secure a Flask app
* How to log requests and test locally

This project replaces the earlier “Weather CLI” and “Node.js CLI” weeks by switching perspective: instead of calling APIs, you *build one.*

---

## 🧠 What You’ll Learn

| Concept               | Description                                                |
| --------------------- | ---------------------------------------------------------- |
| Flask setup           | Create and run a simple server with endpoints              |
| Routing               | Handle different HTTP methods and paths                    |
| Error handling        | Return clean JSON responses for 404 and 500s               |
| Environment variables | Use `.env` safely without committing secrets               |
| Logging               | Write rotating logs for API activity                       |
| Git hygiene           | Avoid leaking secrets and manage repo connections properly |

---

## ⚙️ Tech Stack

* **Language:** Python 3.13
* **Framework:** Flask
* **Logging:** `logging` + `RotatingFileHandler`
* **Environment:** `python-dotenv`
* **Version Control:** Git + GitHub (org: [James-api-lab](https://github.com/James-api-lab))

---

## 🗂️ Project Structure

```
Week 4 - Flask API/
│
├── app.py              # Main Flask application
├── config.py           # App configuration (version, debug mode, etc.)
├── .gitignore          # Excludes venv, logs, env files
├── .env.example        # Example environment variable template
├── README.md           # This file
└── data/               # (Optional) Logs or sample data folder
```

---

## 🚀 Running Locally

```bash
# 1. Activate virtual environment (Windows)
.venv\Scripts\activate

# 2. Install dependencies
pip install flask python-dotenv

# 3. Run the app
python app.py
```

Visit → [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧩 Example Routes

| Route      | Method | Description                                  |
| ---------- | ------ | -------------------------------------------- |
| `/`        | GET    | Home route confirming the server is live     |
| `/health`  | GET    | Returns uptime and version info              |
| `/meta`    | GET    | Returns app metadata (author, version, docs) |
| `/boom`    | GET    | Triggers a test 500 error with clean JSON    |
| `/headers` | GET    | Returns request headers for debugging        |

---

## 🛡️ Security Practices

✅ `.env` is ignored by Git and only `.env.example` is shared
✅ Git history cleaned of API keys using `git-filter-repo`
✅ Repository now uses GitHub push protection for secrets
✅ Safe logging enabled (no sensitive data written to logs)

---

## 🧱️ Next Steps

* [ ] Add `/math/add`, `/math/subtract`, `/math/multiply` routes (Day 2)
* [ ] Accept query and JSON body params
* [ ] Learn structured response models (status, data, message)
* [ ] Push new feature branches safely to GitHub org

---

## 🔹 Repository

🔗 [https://github.com/James-api-lab/week4-flask-api](https://github.com/James-api-lab/week4-flask-api)
