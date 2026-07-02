from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse

from app.database import engine, Base

# Routers
from app.routers import (
    building_router,
    room_router,
    faculty_router,
    department_router,
    section_router,
    search_router,
    
)


# Create tables on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown (add cleanup if needed)


app = FastAPI(
    title="FindMyClass",
    description="""
    FindMyClass is a smart campus navigation system that helps students and visitors locate classrooms, faculty cabins, departments, laboratories, and other campus facilities using intelligent search.
    """,
    version="1.0.0",
    docs_url=None,
    redoc_url=None,
    lifespan=lifespan
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5173",
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (make sure "static" folder exists)
app.mount("/static", StaticFiles(directory="static"), name="static")


# Include routers
app.include_router(building_router.router)
app.include_router(room_router.router)
app.include_router(department_router.router)
app.include_router(faculty_router.router)
app.include_router(section_router.router)
app.include_router(search_router.router)



# Custom Swagger UI
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui():
    openapi_url = app.openapi_url or "/openapi.json"
    swagger_ui_html = get_swagger_ui_html(
        openapi_url=openapi_url,
        title="FindMyClass",
    )

    # ✅ Convert response body to string safely
    if isinstance(swagger_ui_html.body, (bytes, bytearray)):
        html_str = swagger_ui_html.body.decode("utf-8")
    else:
        html_str = str(swagger_ui_html.body)

    custom_css = """
    <style>
    .topbar-wrapper img {
        content: url('/static/logo.png') !important;
        width: 45px !important;
        height: 45px !important;
    }

    .topbar-wrapper span {
        display: none !important;
    }
    </style>
    """

    # ✅ Inject CSS into HTML string
    modified_html = html_str.replace("</head>", custom_css + "</head>")

    return HTMLResponse(content=modified_html)


@app.get("/")
def home():
    return {"message": "Welcome to FindMyClass API"}
