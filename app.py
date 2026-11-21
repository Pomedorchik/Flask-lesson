from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


USERS = {
    "admin": "admin123",
}


@app.route("/")
def index():
    """Главная страница: показываем форму авторизации."""
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = ""
    error = None

    try:
        
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if not username or not password:
            error = "Заполните оба поля: имя пользователя и пароль."
        elif USERS.get(username) != password:
            error = "Неверное имя пользователя или пароль."
    except Exception:
        error = "Произошла непредвиденная ошибка. Попробуйте ещё раз."

    if error:
        return render_template("index.html", error=error, username=username)
    return redirect(url_for("welcome", username=username))


@app.route("/welcome")
def welcome():
    username = request.args.get("username", "гость")
    return render_template("login.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)
