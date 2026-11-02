
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import text


load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

connection_url = URL.create(
    drivername="mysql+pymysql",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=int(DB_PORT),
    database=DB_NAME,
)

engine = create_engine(connection_url)


def get_all_doctors():
    with engine.connect() as connection:
        result= connection.execute(
            text('select * from doctors')

        )

        doctors=result.mappings().all()
        return doctors


def create_appointment(
    patient_name,
    age,
    health_issue,
    doctor_id,
    appointment_date,
    appointment_time
):
    with engine.begin() as connection:
        connection.execute(
            text("""
                INSERT INTO appointments
                (
                    patient_name,
                    age,
                    health_issues,
                    doctor_id,
                    appointment_date,
                    appointment_time
                )
                VALUES
                (
                    :patient_name,
                    :age,
                    :health_issue,
                    :doctor_id,
                    :appointment_date,
                    :appointment_time
                )
            """),
            {
                "patient_name": patient_name,
                "age": age,
                "health_issue": health_issue,
                "doctor_id": doctor_id,
                "appointment_date": appointment_date,
                "appointment_time": appointment_time
            }
        )



def get_all_appointments():
    with engine.connect() as connection:
        result=connection.execute(
            text("""
            SELECT 
            a.appointment_id,
            a.patient_name,
            a.age,
            a.health_issues,
            a.appointment_date,
            a.appointment_time,
            a.status,
            d.name as doctor_name,
            d.specialisation
            FROM appointments a
            JOIN doctors d
            on a.doctor_id=d.doctor_id
            order by a.appointment_id DESC """)
        )

        appointments =result.mappings().all()
        return appointments



def update_appointment_status(appointment_id,new_status):
    with engine.begin() as connection:
        connection.execute(
            text(
                """ UPDATE appointments
                SET status =:status
                WHERE appointment_id=:appointment_id"""
            ),
            {
                "status":new_status,
                "appointment_id":appointment_id
            }
        )


def delete_appointment(appointment_id):
    with engine.begin() as connection:
        connection.execute(
            text(""" DELETE FROM appointments
            WHERE appointment_id = :appointment_id"""
        ),
{
    "appointment_id": appointment_id
}
)


def create_review(patient_name, feedback, rating):
    with engine.begin() as connection:
        connection.execute(
            text(""" INSERT INTO reviews
            (patient_name, feedback, rating)
            VALUES
            (:patient_name, :feedback, :rating)"""),
            {
                "patient_name":patient_name,
                "feedback":feedback,
                "rating":rating
            }
        )