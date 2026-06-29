from fastapi import FastAPI

app = FastAPI(
    title = "Ai Manga Recommendation System",
    version = "1.0.0",
    description = "Backend API for Manga, MAnhwa, and Manhua Recomendation System"
)

@app.get("/")
def home():
    return {
        "status" : "success",
        "message" : "Welcome to Ai Manga Recommendation System🚀",  
        "version" : "1.0.0"
    }
