import pika
import json
import uuid
import threading
import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI(title="Homework Tracker Async API")
JOBS = {} # In-memory БД (id: {status, result})

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")

class JobRequest(BaseModel):
    title: str
    deadline: str

def consume_results():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
            channel = connection.channel()
            channel.queue_declare(queue='results')
            
            def callback(ch, method, properties, body):
                data = json.loads(body)
                job_id = data["id"]
                if job_id in JOBS:
                    JOBS[job_id]["status"] = "DONE"
                    JOBS[job_id]["result"] = data["result"]
                    JOBS[job_id]["completedAt"] = data["completedAt"]
                ch.basic_ack(delivery_tag=method.delivery_tag)

            channel.basic_consume(queue='results', on_message_callback=callback, auto_ack=False)
            channel.start_consuming()
        except Exception:
            time.sleep(5)

@app.on_event("startup")
def startup_event():
    threading.Thread(target=consume_results, daemon=True).start()

@app.post("/jobs", status_code=202)
def create_job(request: JobRequest):
    job_id = str(uuid.uuid4())
    JOBS[job_id] = {"status": "ACCEPTED", "result": None, "title": request.title}
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue='tasks')
    channel.basic_publish(
        exchange='',
        routing_key='tasks',
        body=json.dumps({"id": job_id, "title": request.title, "deadline": request.deadline}),
        properties=pika.BasicProperties(delivery_mode=2)
    )
    connection.close()
    
    return {"id": job_id, "status": "ACCEPTED"}

@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    if job_id not in JOBS:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"id": job_id, **JOBS[job_id]}