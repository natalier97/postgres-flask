from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#configured flask to use postgres
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://natalie:1234@localhost/school'

#initializing the sqlalchemy extension
db = SQLAlchemy(app)

class Students(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    birthdate = db.Column(db.Date)
    address_id = db.Column(db.Integer)

@app.route('/students')
def get_students():
    # similar to using SELECT * FROM students from psql;
    students = Students.query.all() 
    # print(students)
    json_students = [{'id':stud.id, 'first_name':stud.first_name, 'last_name':stud.last_name, 'birthdate':stud.birthdate, 'address_id':stud.address_id} for stud in students]
    response = jsonify(json_students)
    return response


#/student_names/: Returns an array of student objects holding only the keys of 'first_name' and 'last_name' along with their corresponding values.
@app.route('/student_names/', methods=['GET'])
def get_student_names():
    students = Students.query.all()
    json_students = [{'first_name':stud.first_name, 'last_name':stud.last_name} for stud in students]
    response = jsonify(json_students)
    return response
    
    # name_array = []
    # response = get_students()
    # for stud_obj in response:
    #     name_dict = {}
    #     name_dict['first_name'] = stud_obj.get('first_name')
    #     name_dict['last_name'] = stud_obj.get('last_name')
    #     name_array.append(name_dict)
    # return name_array




if __name__ == '__main__':
    app.run(debug=True)
