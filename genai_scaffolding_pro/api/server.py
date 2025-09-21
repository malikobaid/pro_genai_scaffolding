from fastapi import FastAPI

from genai_scaffolding_pro.api.main import create_app

app: FastAPI = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "genai_scaffolding_pro.api.server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
