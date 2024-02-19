from main import StudentsInMLOps

def test_enroll_and_drop_students():
    classroom = StudentsInMLOps()
    classroom.enrollStudents(5)
    assert classroom.getTotalStrength() == 5
    classroom.dropStudents(2)
    assert classroom.getTotalStrength() == 3
    classroom.dropStudents(5)  # Dropping more students than present should reset to 0
    assert classroom.getTotalStrength() == 0

def test_get_class_name():
    classroom = StudentsInMLOps()
    assert classroom.getClassName() == "MLOps Basics"
