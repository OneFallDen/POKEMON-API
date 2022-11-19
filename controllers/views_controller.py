from fastapi.responses import FileResponse


def homepage():
    return FileResponse("views/homepage.html")
