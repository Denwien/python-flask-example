from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
import json
import os
import logging

app = Flask(__name__, template_folder="app/templates")
app.secret_key = "supersecretkey"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

USERS_FILE="users.json"

# Загрузка пользователей
try:
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            users = json.load(f)
            app.logger.debug(f"Загружено {len(users)} пользователей")
    else:
        users=[]
except Exception as e:
    users=[]
    app.logger.error(f"Ошибка при загрузке пользователей: {e}")

@app.route("/users/new", methods=["GET"])
def users_new():
    app.logger.debug("Открыта форма создания нового пользователя")
    return render_template("users/new.html")

@app.route("/users/create", methods=["POST"])
def users_create():
    name = request.form.get("name")
    email = request.form.get("email")
    new_id = max([u["id"] for u in users], default=0)+1
    new_user={"id":new_id,"name":name,"email":email}
    users.append(new_user)
    try:
        with open(USERS_FILE,"w",encoding="utf-8") as f:
            json.dump(users,f,ensure_ascii=False,indent=4)
        app.logger.debug(f"Создан пользователь {new_user}")
        flash(f"Пользователь {name} успешно создан!", "success")
    except Exception as e:
        app.logger.error(f"Ошибка при сохранении пользователя: {e}")
        flash(f"Ошибка при создании пользователя: {e}", "error")
    return redirect(url_for("users_index"))

@app.route("/users/", methods=["GET"])
def users_index():
    query = request.args.get("query","").lower()
    if query:
        filtered_users=[u for u in users if query in u["name"].lower()]
        app.logger.debug(f"Фильтрация по '{query}', найдено {len(filtered_users)}")
    else:
        filtered_users=users
        app.logger.debug(f"Просмотр всех пользователей, всего {len(filtered_users)}")

    messages = get_flashed_messages(with_categories=True)

    return render_template(
        "users/index.html",
        users=filtered_users,
        query=query,
        messages=messages,
        new_user_url=url_for("users_new")
    )

if __name__=="__main__":
    app.run(debug=True)
