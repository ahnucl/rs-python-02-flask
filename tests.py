import pytest
import requests

# CRUD
BASE_URL = 'http://127.0.0.1:5000'
tasks = []


def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_body = response.json()
    assert "message" in response_body
    assert "id" in response_body
    tasks.append(response_body['id'])


def test_get_tasks():
    response = requests.get(f'{BASE_URL}/tasks')
    assert response.status_code == 200
    response_body = response.json()
    assert 'tasks' in response_body
    assert 'total_tasks' in response_body


def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_body = response.json()
        assert task_id == response_body['id']


def  test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            # "completed": False,
            "description": "Nova descrição",
            "title": "Título atualizado",
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        assert response.status_code == 200
        response_body = response.json()
        assert "message" in response_body
        
        # Verificando alteração
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_body = response.json()
        assert response_body["title"] == payload["title"]
        assert response_body["description"] == payload["description"]
        # assert response_body["completed"] == payload["completed"]


def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404
        
        