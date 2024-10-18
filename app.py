from crypt import methods
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


@app.route('/tasks', methods=['GET'])
def get_talks():
    task_list = [task.to_dict() for task in tasks]

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for task in tasks:
        if task.id == id:
            return jsonify(task.to_dict())

    return jsonify({'message': 'Não foi possível encontrar atividade'}), 404


@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task_to_update = None
    
    for task in tasks:
        if task.id == id:
            task_to_update = task
            break
    
    if task_to_update == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    data = request.get_json()
    task_to_update.title = data['title']
    task_to_update.description = data['description']
    # task_to_update.completed = data['completed'] # Deveria ser atualizado só no PATCH
    
    return jsonify({"message": "Tarefa atualizada com sucesso"})


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task_to_delete = None
    
    for task in tasks:
        if task.id == id:
            task_to_delete = task
            break
    
    if not task_to_delete:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    tasks.remove(task_to_delete)
    return jsonify({"message": "Tarefa removida com sucesso"})


if __name__ == '__main__': # Execução manual
    app.run(debug=True) # Apenas para desenvolvimento

