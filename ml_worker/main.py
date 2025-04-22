from app.services.crud.user import get_user_by_id
import json
from mlrunner import MlRunner
from fastapi import Depends
from app.database.database import get_session
from app.services.rm.rabbitmq import RabbitMQ


ml_runner = MlRunner()
rabbitmq = RabbitMQ()


def process_message(ch, method, properties, body):


    data_for_request=json.loads(body)
    user_id = data_for_request['user_id']
    image_path = data_for_request['image_path']
    user=get_user_by_id(user_id,session=Depends(get_session))



    response=ml_runner.get_prediction(image_path=image_path, user=user)



rabbitmq.consume(queue_name="ml_request", callback=process_message)










