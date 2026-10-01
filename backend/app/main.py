from fastapi import FastAPI

app = FastAPI(title="boulder-deals backend")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
