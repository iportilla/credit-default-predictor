# Credit Default Prediction Platform 🚀

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Docker Compose](https://img.shields.io/badge/docker-compose-blue)](https://docs.docker.com/compose/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

This project provides a full pipeline to:

- Train a machine learning model to predict credit card payment defaults.
- Serve the model with a **Flask API** (REST endpoint).
- Interact with predictions through a **Streamlit Web UI**.
- Deploy everything via **Docker Compose**.

Lazy model loading  
Healthcheck support  
Streamlit interactive predictions  
Ready for scaling and extension!

---

## Project Structure

```
credit-default-predictor/
│
├── api/             # Flask API server (predict endpoint)
│   ├── app.py
│   ├── Dockerfile
│   └── data/raw/    # Training data CSV
│
├── ui/              # Streamlit frontend
│   ├── streamlit_app.py
│   ├── Dockerfile
│
├── training/        # Training scripts
│   ├── main.py
│   └── output/      # Saved models (.pkl files)
│
├── docker-compose.yml
├── README.md
└── requirements.txt (optional)
```

---

## Quickstart

### 1. Clone the Repository

```bash
git clone https://github.com/iportilla/credit-default-predictor.git
cd credit-default-predictor
```

### 2. Build the Containers

```bash
make build
```

### 3. Train the Model

Enter the API container:

```bash
docker compose run api bash
```

Inside the container:

```bash
python training/main.py
exit
```

### 4. Start the Services

```bash
make up
```

- Flask API: [http://localhost:5000](http://localhost:5000)
- Streamlit UI: [http://localhost:8501](http://localhost:8501)

### 5. Check status of running containers

```bash
make ps
```
---

## API Endpoint Documentation

### POST `/predict`

Send JSON payload:

```json
{
  "input_data": {
    "columns": [0,1,2,...],
    "index": [0,1],
    "data": [[feature values], [feature values]]
  }
}
```

**Response:**

```json
{
  "predictions": [
    {
      "index": 0,
      "prediction": 1,
      "default_probability": 0.85
    }
  ]
}
```

---

## Architecture

```
+----------------+             +---------------+            +-----------------+
|  User Browser  |  <--->      | Streamlit UI  |  <--->     |  Flask API      |
| (localhost:8501)            | (localhost:8501)            | (localhost:5000)|
+----------------+             +---------------+            +-----------------+
```

- Streamlit uploads JSON → Calls Flask API → Receives prediction results.

---

## Tech Stack

- Python 3.11
- Scikit-learn 1.4.2
- Numpy 1.26.4
- Flask
- Streamlit
- Docker + Docker Compose

---

## Screenshots (Optional)

> _Add screenshots of the Streamlit UI uploading JSON, and prediction results displayed nicely._

---

## Contribution Guidelines

- Open a Pull Request if you'd like to add new features (e.g., multiple model support).
- Feel free to submit Issues for bugs or suggestions!

---

## License

Distributed under the MIT License.  
See `LICENSE` file for more information.

---

## Author

- **Your Name** - [iportilla](https://github.com/iportilla)

---
