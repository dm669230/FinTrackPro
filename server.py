import uvicorn
# from app.main import app

if __name__ == "__main__":
    try:
        uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to exit...")
