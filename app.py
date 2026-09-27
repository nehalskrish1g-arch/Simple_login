from flask import Flask, request, render_template

app = Flask(__name__)

# 3-digit password for the demonstration
CORRECT_PASSWORD = "143"


@app.route("/", methods=["GET", "POST"])
def login():

    message = ""
    success = False

    if request.method == "POST":

        password = request.form.get("password")

        if password == CORRECT_PASSWORD:
            message = "Login successful! 🎉"
            success = True
        else:
            message = "Invalid password!"

    return render_template(
        "login.html",
        message=message,
        success=success
    )


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)