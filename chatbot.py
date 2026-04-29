from database import (
    get_all_courses,
    search_course,
    get_faq_answer,
    save_unknown_question
)


def format_course(course):
    if not course:
        return "Sorry, I could not find that course."

    return f"""
<b>Course Name:</b> {course[1]}<br>
<b>Duration:</b> {course[2]}<br>
<b>Fee:</b> {course[3]}<br>
<b>Entry Requirement:</b> {course[4]}<br>
<b>Career Path:</b> {course[5]}
"""


def get_bot_response(user_input):
    message = user_input.lower().strip()

    faq_answer = get_faq_answer(message)
    if faq_answer:
        return faq_answer

    if "course" in message or "courses" in message or "available" in message:
        courses = get_all_courses()
        response = "<b>Available Courses:</b><br><br>"

        for course in courses:
            response += f"""
🎓 <b>{course[1]}</b><br>
Duration: {course[2]}<br>
Fee: {course[3]}<br><br>
"""
        return response

    elif "hnd" in message or "computing" in message:
        return format_course(search_course("HND Computing"))

    elif "business" in message:
        return format_course(search_course("Diploma in Business"))

    elif "english" in message:
        return format_course(search_course("English Certificate"))

    elif "it" in message:
        return format_course(search_course("Diploma in IT"))

    elif "fee" in message or "price" in message:
        return "Please type the course name. Example: HND Computing fee"

    elif "duration" in message:
        return "Please type the course name. Example: HND Computing duration"

    elif "requirement" in message or "qualification" in message:
        return "Please type the course name. Example: HND Computing requirement"

    elif "apply" in message or "register" in message:
        return "Please fill the student inquiry form with your name, phone number, and interested course."

    else:
        save_unknown_question(user_input)
        return """
I do not know this answer yet. Your question has been saved for admin training.<br>
After admin adds an answer, I can answer this question next time.
"""