from boot.model.student import Student
from pweb_form_rest import fields, PWebRestDTO


class StudentDetailsDTO(PWebRestDTO):
    class Meta:
        model = Student
        load_instance = True

    name = fields.String(required=True, error_messages={"required": "Please enter name"})
    roll= fields.Integer(required=True, error_messages={"required": "Please enter roll"})
    registration = fields.String(required=True, error_messages={"required": "Please enter registration"})
    technology = fields.String(required=True, error_messages={"required": "Please enter technology"})
    email = fields.Email(required=True, error_messages={"required": "Please enter email"})
    address = fields.String(allow_none=True)


class StudentCreateDTO(StudentDetailsDTO):
    class Meta:
        model = Student
        load_instance = True

    password = fields.String(required=True, error_messages={"required": "Please enter password"})


class StudentUpdateDTO(StudentDetailsDTO):
    class Meta:
        model = Student
        load_instance = True

    id = fields.Integer(required=True, error_messages={"required": "Please enter id"})
