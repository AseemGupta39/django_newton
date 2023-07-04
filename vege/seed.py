from faker import Faker
from random import randint as rd
fake = Faker()
from . models import Student,StudentID,Department

def seed_db(n=10) -> None:
    try:
        for _ in range(0,n):
            department_objs=Department.objects.all()
            department=department_objs[rd(0,len(department_objs)-1)]
            student_id = f'STU_0{rd(100,999)}'
            student_name=fake.name()
            student_email=fake.email()
            student_age=rd(20,30)
            student_address=fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)

            student_obj = Student.objects.create(    
                department = department,                      
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address
            )
    except Exception as e:
        print(e)

        # print(student_email,student_name,student_address,student_age)

# seed_db()