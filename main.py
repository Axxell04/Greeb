import uvicorn
from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), "static")

@app.get("/")
async def root():
    return FileResponse("static/html/inicio.html")

@app.get("/proyectos")
async def proyectos():
    return FileResponse("static/html/proyectos.html")

@app.get("/api/get_projects")
async def get_projects():
    return FileResponse("projects.json")


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=7777)