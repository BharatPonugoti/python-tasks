from flask import Blueprint, render_template, request

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        print(username)
        print(password)

        # Dummy Login
        if username == "admin" and password == "admin123":

            return """
            <h1 style='text-align:center;
                       margin-top:100px;
                       color:green;
                       font-size:50px;'>

                Login Successful ✅

            </h1>
            """

        else:

            return """
            <h1 style='text-align:center;
                       margin-top:100px;
                       color:red;
                       font-size:50px;'>

                Invalid Username or Password ❌

            </h1>
            """

    return render_template("login.html")