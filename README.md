API de gestions de taches



python, flask, docker


lancement via venv



# Todo API

API REST de gestion de tâches, construite avec Flask et conteneurisée avec Docker.

## Technologies
- Python 3.12
- Flask
- Docker

## Lancer le projet avec Docker

```bash
docker build -t todo-api .
docker run -p 5000:5000 todo-api
```

## Endpoints

| Méthode | Route | Description |
|---|---|---|
| GET | /taches | Récupère toutes les tâches |
| POST | /taches | Ajoute une nouvelle tâche |

## Exemple

```bash
# Ajouter une tâche
curl -X POST http://localhost:5000/taches \
  -H "Content-Type: application/json" \
  -d '{"titre": "Apprendre Docker"}'

# Lister les tâches
curl http://localhost:5000/taches
```
