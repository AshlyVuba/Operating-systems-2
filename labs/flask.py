from flask import Flask, render_template
app = Flask(__name)

@app.route('/')
def student_details():
    students = fetch_students()  # Call the function to fetch student details
    return render_template('student_details.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
bash portion
python your_flask_app.py
