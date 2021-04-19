from fastapi import FastAPI, Response
import uvicorn
from pydantic import BaseModel
import datetime


class PatientModel(BaseModel):
    name: str
    surname: str


class Patient:
    def __init__(self, patient_id, name, surname, register_date, injection_date):
        self.patient_id = patient_id
        self.name = name
        self.surname = surname
        self.register_date = register_date
        self.injection_date = injection_date


patients = list()
app = FastAPI()

counter = 1


@app.get("/patient/{patient_id}", status_code=200)
def get_client(patient_id: int, response: Response):

    if patient_id < 1:
        response.status_code = 400
        return response

    patient = None
    for i in patients:
        if patient_id == i.patient_id:
            patient = i
    if patient is None:
        response.status_code = 404
        return response

    return {
        "id": patient.patient_id,
        "name": patient.name,
        "surname": patient.surname,
        "register_date": patient.register_date,
        "vaccination_date": patient.injection_date
    }


@app.post("/register", status_code=201)
def process_client(patient: PatientModel):
    global counter
    patient_id = counter
    name = patient.name
    surname = patient.surname
    today_date = datetime.datetime.today()
    number_of_letters = letters_num(patient)
    injection_date = today_date + datetime.timedelta(days=number_of_letters)
    counter += 1
    today_date = today_date.strftime('%Y-%m-%d')
    injection_date = injection_date.strftime('%Y-%m-%d')
    patients.append(Patient(patient_id, name, surname, today_date, injection_date))
    return {
        "id": patient_id,
        "name": name,
        "surname": surname,
        "register_date": today_date,
        "vaccination_date": injection_date
    }


def letters_num(patient: PatientModel):
    letters_counter = 0
    for i in patient.name + patient.surname:
        if i.isalpha():
            letters_counter += 1
    return letters_counter


if __name__ == '__main__':
    uvicorn.run(app)
