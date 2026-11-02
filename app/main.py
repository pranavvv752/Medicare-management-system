from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.database import get_all_doctors
from fastapi import Form
from fastapi.responses import RedirectResponse
from app.database import (
    create_appointment,
    get_all_doctors,
    get_all_appointments,
    update_appointment_status,
    delete_appointment,
    create_review
)


app=FastAPI(title='Medicare Managemnent System')
templates=Jinja2Templates(directory='templates')
app.mount("/static",StaticFiles(directory='static'),name='static')


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='index.html'
    )

@app.get("/doctors")
def doctors(request:Request):
    doctors_list= get_all_doctors()
    return templates.TemplateResponse(
        request=request,
        name="doctors.html",
        context={"doctors":doctors_list}
    )


@app.get("/appointments")
def appointment_form(request:Request):
    doctor_list= get_all_doctors()

    return templates.TemplateResponse(
        request=request,
        name="appointment.html",
        context={"doctors":doctor_list}
    )
@app.post("/appointments")
def book_appointment(
        patient_name: str=Form(...),
        age:int= Form(...),
        health_issue:str=Form(...),
        doctor_id:int=Form(...),
        appointment_date:str=Form(...),
        appointment_time:str=Form(...),
        
):
    create_appointment(
        patient_name,
        age,
        health_issue,
        doctor_id,
        appointment_date,
        appointment_time
    )

    return RedirectResponse(
        url="/appointments/success",
        status_code=303
    )



@app.get("/appointments/success")
def appointment_success(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="appointment_success.html"
    )



@app.get("/manage-appointments")
def manage_appointments(request: Request):
    appointments= get_all_appointments()

    return templates.TemplateResponse(
        request=request,
        name="manage_appointments.html",
        context={"appointments":appointments}
    )


@app.post("/appointments/{appointment_id}/confirm")
def confirm_appointment(appointment_id : int):
    update_appointment_status(appointment_id,"Confirmed")

    return RedirectResponse(
        url="/manage-appointments",
        status_code=303
    )

@app.post("/appointments/{appointment_id}/cancel")
def cancel_appointment(appointment_id:int):
    update_appointment_status(appointment_id,"Cancelled")

    return RedirectResponse(
        url="/manage-appointments",
        status_code=303
    )

@app.post("/appointments/{appointment_id}/delete")
def remove_appointment(appointment_id:int):
    delete_appointment(appointment_id)

    return RedirectResponse(
        url="/manage-appointments",
        status_code=303
    )

@app.get("/reviews")
def review_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="review.html",
        context={}
    )

@app.post("/reviews")
def submit_review(
    patient_name: str=Form(...),
    feedback: str=Form(...),
    rating: int=Form(...)
):
    create_review(patient_name, feedback, rating)

    return RedirectResponse(
        url="/reviews",
        status_code=303
    )
