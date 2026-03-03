# Structa - App (Next.js)

A modular FastAPI backend for processing uploaded files (currently CSV support) using clean architecture principles, centralized error handling, and standardized API responses.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

### 2. Create a Virtual Environment

```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn pandas
```

### 4. Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

http://127.0.0.1:8000

Interactive documentation:

http://127.0.0.1:8000/docs
