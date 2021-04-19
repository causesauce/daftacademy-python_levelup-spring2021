from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import datetime


class Patient(BaseModel):
    name: str
    surname: str


app = FastAPI()

counter = 1


@app.post("/register", status_code=201)
def process_client(patient: Patient):
    global counter
    id = counter
    name = patient.name
    surname = patient.surname
    today_date = datetime.datetime.today()
    number_of_letters = letters_num(patient)
    injection_date = today_date + datetime.timedelta(days=number_of_letters)
    counter += 1

    return {
        "id": id,
        "name": name,
        "surname": surname,
        "register_date": today_date.strftime('%Y-%m-%d'),
        "vaccination_date": injection_date.strftime('%Y-%m-%d')
    }


def letters_num(patient: Patient):
    letters_counter = 0
    for i in patient.name+patient.surname:
        if i.isalpha():
            letters_counter += 1
    return letters_counter


if __name__ == '__main__':
    uvicorn.run(app)
