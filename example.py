from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__, template_folder="app/templates")

USERS_FILE = "users.json"

# Загружаем пользователей из файла, если он существует
if os.path.exists(USERS_FILE):
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        users = json.load(f)
else:
    users = []

@app.route("/users/new", methods=["GET"])
def users_new():
    return render_template("users/new.html")

@app.route("/users/create", methods=["POST"])
def users_create():
    name = request.form.get("name")
    email = request.form.get("email")
    new_id = max([user["id"] for user in users], default=0) + 1
    new_user = {"id": new_id, "name": name, "email": email}
    users.append(new_user)

    # Сохраняем всех пользователей в файл
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

    # Редирект на /users/
    return redirect("/users/")

@app.route("/users/", methods=["GET"])
def users_index():
    query = request.args.get("query", "").lower()
    if query:
        filtered_users = [user for user in users if query in user["name"].lower()]
    else:
        filtered_users = users
    return render_template("users/index.html", users=filtered_users, query=query)

if __name__ == "__main__":
    app.run(debug=True)
