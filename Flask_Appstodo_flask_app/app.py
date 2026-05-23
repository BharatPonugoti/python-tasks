# ============================================================
# IMPORT REQUIRED MODULES
# ============================================================

from flask import Flask, render_template, request, redirect, url_for


# ============================================================
# CREATE FLASK APPLICATION
# ============================================================

app = Flask(__name__)


# ============================================================
# TEMPORARY TODO STORAGE
# ============================================================

tasks = [
    {
        "id": 1,
        "title": "Complete Flask Project",
        "status": "Pending"
    },
    {
        "id": 2,
        "title": "Practice CRUD Operations",
        "status": "Completed"
    }
]


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():

    return render_template("home.html")


# ============================================================
# TASK MANAGEMENT PAGE
# ============================================================

@app.route("/tasks")
def task_page():

    return render_template(
        "tasks.html",
        tasks=tasks
    )


# ============================================================
# DASHBOARD PAGE
# ============================================================

@app.route("/dashboard")
def dashboard():

    total_tasks = len(tasks)

    completed_tasks = len([
        task for task in tasks
        if task["status"] == "Completed"
    ])

    pending_tasks = len([
        task for task in tasks
        if task["status"] == "Pending"
    ])

    return render_template(
        "dashboard.html",
        total=total_tasks,
        completed=completed_tasks,
        pending=pending_tasks
    )


# ============================================================
# ADD NEW TASK
# ============================================================

@app.route("/add", methods=["POST"])
def add_task():

    title = request.form.get("title")

    # Check Empty Input
    if title and title.strip():

        # Generate New ID
        new_id = 1

        if tasks:
            new_id = tasks[-1]["id"] + 1

        # Create New Task
        new_task = {
            "id": new_id,
            "title": title,
            "status": "Pending"
        }

        # Store Task
        tasks.append(new_task)

    return redirect(url_for("task_page"))


# ============================================================
# UPDATE TASK STATUS
# ============================================================

@app.route("/update/<int:task_id>")
def update_task(task_id):

    for task in tasks:

        if task["id"] == task_id:

            # Toggle Status
            if task["status"] == "Pending":
                task["status"] = "Completed"

            else:
                task["status"] = "Pending"

            break

    return redirect(url_for("task_page"))


# ============================================================
# DELETE TASK
# ============================================================

@app.route("/delete/<int:task_id>")
def delete_task(task_id):

    global tasks

    tasks = [
        task for task in tasks
        if task["id"] != task_id
    ]

    return redirect(url_for("task_page"))


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(debug=True)