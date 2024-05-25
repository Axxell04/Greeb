from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import sender_mails

class ContextContact(BaseModel):
    contact_mail: str
    message: str

app = FastAPI()
origins = ["http://192.168.1.14:5173", "http://192.168.1.14:4173"]

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory="static"), "static")

@app.get("/")
async def root():
    return FileResponse("static/dist/index.html")

@app.get("/api/get_projects")
async def get_projects():
    return FileResponse("projects.json")

@app.post("/api/send_mail")
async def send_email(context_contact : ContextContact, backgound_task: BackgroundTasks):
    backgound_task.add_task(sender_mails.send_mail, context_contact.message, context_contact.contact_mail)
    return {"message": "Mensaje enviado con éxito"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=7777)