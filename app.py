from flask import Flask, jsonify, request
from models.tasks import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso", "task": new_task.__dict__})

if __name__ == '__main__': # Execução manual
    app.run(debug=True) # Apenas para desenvolvimento