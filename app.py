from flask import Flask, render_template, request, redirect   #➡️ Import Flask to create the app, and render_template to return HTML files from the templates/ folder.
from todo import list_tasks, add_task      #➡️ Reuse the list_tasks() function you already wrote to fetch tasks from the database.
from todo import delete_task


app = Flask(__name__)

@app.route('/')
def index():
    tasks = list_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    description = request.form['description']
    add_task(description)
    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    delete_task(id)
    return redirect('/')
    
if __name__ == '__main__':       #➡️ Run the app in debug mode so you get error messages while developing.
    app.run(debug=True)
