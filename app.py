from flask import Flask, request, jsonify
app = Flask(__name__)


class Task:
    def __init__(self, id, title, description, completed):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(data['id'], data['title'], data['description'], data['completed'])
    tasks.append(new_task)
    return jsonify({'message': 'Task created successfully'}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.__dict__ for task in tasks]
    return jsonify(task_list), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        return jsonify(task.__dict__), 200
    return jsonify({'message': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        task.title = data['title']
        task.description = data['description']
        task.completed = data['completed']
        return jsonify({'message': 'Task updated successfully'}), 200
    return jsonify({'message': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        tasks.remove(task)
        return jsonify({'message': 'Task deleted successfully'}), 200
    return jsonify({'message': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
