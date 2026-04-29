import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="edulearn_db"
    )


def get_all_courses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


def search_course(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM courses WHERE LOWER(course_name) LIKE %s",
        ("%" + keyword.lower() + "%",)
    )
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    return data


def add_course(course_name, duration, fee, entry_requirement, career_path):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO courses 
        (course_name, duration, fee, entry_requirement, career_path)
        VALUES (%s, %s, %s, %s, %s)
    """, (course_name, duration, fee, entry_requirement, career_path))
    conn.commit()
    cursor.close()
    conn.close()


def get_faq_answer(user_question):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM faq")
    faqs = cursor.fetchall()
    cursor.close()
    conn.close()

    user_question = user_question.lower()

    for question, answer in faqs:
        if question.lower() in user_question or user_question in question.lower():
            return answer

    return None


def add_faq(question, answer):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO faq (question, answer) VALUES (%s, %s)",
        (question, answer)
    )
    conn.commit()
    cursor.close()
    conn.close()


def save_unknown_question(question):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO unknown_questions (question) VALUES (%s)",
        (question,)
    )
    conn.commit()
    cursor.close()
    conn.close()


def get_unknown_questions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM unknown_questions ORDER BY id DESC")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


def save_inquiry(name, phone, course):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO student_inquiries (student_name, phone, course)
        VALUES (%s, %s, %s)
    """, (name, phone, course))
    conn.commit()
    cursor.close()
    conn.close()