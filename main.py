from fastapi import FastAPI
import uvicorn
import time, psutil



app = FastAPI()

@app.post("/search")
def search(body: dict):
    print("a")

    #  const res = await fetch("http://127.0.0.1:8000/search", {
    #         method: "POST",
    #         headers: { "Content-Type": "application/json" },
    #         body: JSON.stringify({ query: embedQuery }),
    #       });


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
