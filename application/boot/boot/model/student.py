from pweb_orm import PwebModel, pweb_orm


class Student(PwebModel):
    student_name = pweb_orm.Column("student_name", pweb_orm.String(150), nullable=False)
    student_email = pweb_orm.Column("student_email", pweb_orm.String(150), nullable=False)
    student_password = pweb_orm.Column("student_password", pweb_orm.String(250), nullable=False)
    student_roll = pweb_orm.Column("student_roll", pweb_orm.Integer(), nullable=False) 
    student_registration = pweb_orm.Column("student_registration", pweb_orm.String(250), nullable=False)
    student_technology = pweb_orm.Column("student_technology", pweb_orm.String(250), nullable=False)
    student_address = pweb_orm.Column("student_address", pweb_orm.Text())

