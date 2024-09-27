from pweb_orm import PwebModel, pweb_orm


class Student(PwebModel):
    student_name = pweb_orm.Column("name", pweb_orm.String(150), nullable=False)
    student_email = pweb_orm.Column("email", pweb_orm.String(150), nullable=False)
    student_password = pweb_orm.Column("password", pweb_orm.String(250), nullable=False)
    student_roll = pweb_orm.Column("roll", pweb_orm.Integer(), nullable=False) 
    student_registration = pweb_orm.Column("registration", pweb_orm.String(250), nullable=False)
    student_technology = pweb_orm.Column("technology", pweb_orm.String(250), nullable=False)
    student_address = pweb_orm.Column("address", pweb_orm.Text())

