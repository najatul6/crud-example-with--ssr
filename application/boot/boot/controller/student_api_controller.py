from boot.dto.student_dto import StudentCreateDTO, StudentDetailsDTO, StudentUpdateDTO
from boot.service.student_api_service import StudentApiService
from pweb import Blueprint
from pweb_form_rest import pweb_endpoint, pweb_paginate_endpoint

student_api_url_prefix = "/api/v1/students"
student_api_controller = Blueprint(
    "student_api_controller",
    __name__,
    url_prefix=student_api_url_prefix
)
student_api_service = StudentApiService()


@student_api_controller.route("/create", methods=['POST'])
@pweb_endpoint(request_obj=StudentCreateDTO, pweb_message_response=True)
def create():
    return student_api_service.create()


@student_api_controller.route("/details/<int:id>", methods=['GET'])
@pweb_endpoint(response_obj=StudentDetailsDTO)
def details(id: int):
    return student_api_service.details(id)


@student_api_controller.route("/update", methods=['POST'])
@pweb_endpoint(request_obj=StudentUpdateDTO, pweb_message_response=True)
def update():
    return student_api_service.update()


@student_api_controller.route("/delete/<int:id>", methods=['DELETE'])
@pweb_endpoint()
def delete(id: int):
    return student_api_service.delete(id)


@student_api_controller.route("/list", methods=['GET'])
@pweb_paginate_endpoint(response_obj=StudentDetailsDTO)
def list():
    return student_api_service.list()
