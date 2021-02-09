from fastapi import FastAPI

app = FastAPI()


@app.get('hc')
def health_check():
    return {"status": "OK"}
