from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash,check_password_hash
from database.database import get_db_connection
from flask import Blueprint
auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form.get("name").strip()
        email = request.form.get("email").strip().lower()
        password = request.form.get("password")

        if not full_name or not email or not password:
            flash("Please fill all fields.", "warning")
            return redirect(url_for("auth.register"))
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check Existing User
        cursor.execute(
            "SELECT id FROM users WHERE email=?",
            (email,)
        )
        existing_user = cursor.fetchone()
        if existing_user:
            flash("Email already registered.", "danger")
            conn.close()
            return redirect(url_for("auth.register"))

        hashed_password = generate_password_hash(password)
        cursor.execute(
            """
            INSERT INTO users
            (full_name,email,password_hash)
            VALUES(?,?,?)
            """,
            (
                full_name,
                email,
                hashed_password
            )
        )

        conn.commit()
        flash("Registration Successful. Please Login.", "success")
        conn.close()
        return redirect(url_for("auth.login"))
    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email").strip().lower()
        password = request.form.get("password")

        if not email or not password:
            flash("Please enter Email and Password.", "warning")
            return redirect(url_for("auth.login"))

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email=?
            """,
            (email,)
        )
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(
            user["password_hash"],
            password
        ):
            session["logged_in"] = True
            session["user_id"] = user["id"]
            session["full_name"] = user["full_name"]
            session["email"] = user["email"]

            flash(f"Welcome back, {user['full_name']}!", "success")
            return redirect(url_for("dashboard.dashboard_page"))
        
        flash("Invalid Email or Password.", "danger")
    return render_template("login.html")

@auth.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect(url_for("auth.login"))