from flask import Flask, render_template, request, redirect
from todo import (
    list_tasks,
    add_task,
    delete_task,
    toggle_task,
    calculate_progress
)

app = Flask(__name__)

@app.route('/')
def index():
    tasks = list_tasks()
    progress = calculate_progress()
    return render_template('index.html', tasks=tasks, progress=progress)

@app.route('/add', methods=['POST'])
def add():
    description = request.form['description']
    add_task(description)
    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    delete_task(id)
    return redirect('/')

@app.route('/toggle/<int:id>', methods=['POST'])
def toggle(id):
    toggle_task(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
