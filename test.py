from fastapi import FastAPI
import random
import psutil
import uvicorn

app = FastAPI()


@app.get("/api/status")
def status():
    return {"status": "Активен"}


@app.get("/api/pc")
def pc_info():
    memory = psutil.virtual_memory()

    return {
        "cpu_count": psutil.cpu_count(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_total_gb": round(memory.total / (1024 ** 3), 2),
        "memory_used_gb": round(memory.used / (1024 ** 3), 2),
        "memory_percent": memory.percent
    }


@app.get("/api/random-number")
def random_number():
    return {"random_number": random.randint(1, 1000)}


@app.get("/api/sayhello")
def say_hello(name: str):
    return {"message": f"Привет, {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
