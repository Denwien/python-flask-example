from flask import Flask, render_template

app = Flask(__name__)

@app.route('/users/<int:user_id>')
def show_user(user_id):
    user = {"id": user_id, "username": f"user{user_id}"}
    return render_template("users/show.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)
