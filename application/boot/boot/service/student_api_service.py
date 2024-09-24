from boot.dto.student_dto import StudentCreateDTO, StudentUpdateDTO, StudentDetailsDTO
from boot.model.student import Student
from pweb_form_rest import RESTDataCRUD


class StudentApiService:
    rest_data_crud = RESTDataCRUD(model=Student)

    def create(self):
        return self.rest_data_crud.create(StudentCreateDTO())

    def update(self):
        return self.rest_data_crud.update(StudentUpdateDTO())

    def details(self, model_id: int):
        return self.rest_data_crud.details(model_id, StudentDetailsDTO())

    def delete(self, model_id: int):
        return self.rest_data_crud.delete(model_id)

    def list(self):
        search_fields = ["name", "email"]
        return self.rest_data_crud.paginated_list(StudentDetailsDTO(), search_fields=search_fields)
