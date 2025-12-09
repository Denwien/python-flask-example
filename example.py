from flask import Flask, render_template, request

app = Flask(__name__, template_folder="app/templates")

users = [
    {"id": 1, "name": "mike"},
    {"id": 2, "name": "mishel"},
    {"id": 3, "name": "adel"},
    {"id": 4, "name": "keks"},
    {"id": 5, "name": "kamila"},
]

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
