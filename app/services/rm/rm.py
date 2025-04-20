import pika
from fastapi import APIRouter, Body, HTTPException, status, Depends
from database.database import get_session
from models.request import Request, CreateRequest
from sqlmodel import Session

connection_params=pika.ConnectionParameters(
    host='rabbitmq',
    port=5672,
    virtual_host='/',
    credentials=pika.PlainCredentials(
        username='rabbitmq',
        password='strongpassword'
    ),
    heartbeat=30,
    blocked_connection_timeout=2
)

def send_task(user_id:int, create_request:CreateRequest, session:Session):
    
    
    
    
    
    connection=pika.BlockingConnection(connection_params)
    channel=connection.channel()

    queue_name='ml_task_queue'

    channel.queue_declare(queue=queue_name)

    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=message
    )

    connection.close()