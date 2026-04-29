from flask import Flask, render_template, request, jsonify, redirect
from database import (
    get_all_courses,
    add_course,
    save_inquiry,
    get_unknown_questions,
    add_faq
)
from chatbot import get_bot_response

app = Flask(__name__)


@app.route("/")
def home():
    courses = get_all_courses()
    return render_template("index.html", courses=courses)


@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"]
    reply = get_bot_response(message)
    return jsonify({"reply": reply})


@app.route("/inquiry", methods=["POST"])
def inquiry():
    name = request.form["student_name"]
    phone = request.form["phone"]
    course = request.form["course"]

    save_inquiry(name, phone, course)
    return redirect("/")


@app.route("/admin")
def admin():
    courses = get_all_courses()
    return render_template("admin.html", courses=courses)


@app.route("/add_course", methods=["POST"])
def add_course_route():
    add_course(
        request.form["course_name"],
        request.form["duration"],
        request.form["fee"],
        request.form["entry_requirement"],
        request.form["career_path"]
    )
    return redirect("/admin")


@app.route("/train")
def train():
    questions = get_unknown_questions()
    return render_template("train.html", questions=questions)


@app.route("/add_answer", methods=["POST"])
def add_answer():
    question = request.form["question"]
    answer = request.form["answer"]

    add_faq(question, answer)
    return redirect("/train")


if __name__ == "__main__":
    app.run(debug=True)