import pika
import json
import time
import datetime
import os
from datetime import datetime as dt

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")

def process_deadline(title, deadline_str):
    print(f" [x] Анализирую дедлайн для задачи: {title}", flush=True)
    time.sleep(3) # Имитация сложной логики (например, запрос к нейросети для текста)
    
    try:
        # Пытаемся распарсить дату (ожидаем формат ГГГГ-ММ-ДД)
        deadline_date = dt.strptime(deadline_str, "%Y-%m-%d")
        today = dt.now()
        days_left = (deadline_date - today).days
        
        if days_left > 0:
            result = f"Напоминание создано! До дедлайна задачи '{title}' осталось {days_left} дн."
        elif days_left == 0:
            result = f"Внимание! Дедлайн задачи '{title}' — СЕГОДНЯ!"
        else:
            result = f"Дедлайн задачи '{title}' уже прошел ({abs(days_left)} дн. назад)."
    except ValueError:
        result = f"Напоминание для '{title}' создано. (Не удалось распознать формат даты: {deadline_str})"
        
    return result

def main():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
            channel = connection.channel()
            
            channel.queue_declare(queue='tasks')
            channel.queue_declare(queue='results')
            
            def callback(ch, method, properties, body):
                data = json.loads(body)
                job_id = data["id"]
                title = data["title"]
                deadline = data["deadline"]
                
                result_text = process_deadline(title, deadline)
                completed_at = datetime.datetime.now().isoformat()
                
                channel.basic_publish(
                    exchange='',
                    routing_key='results',
                    body=json.dumps({"id": job_id, "result": result_text, "completedAt": completed_at})
                )
                print(f" [x] Результат анализа {job_id} отправлен.", flush=True)
                ch.basic_ack(delivery_tag=method.delivery_tag)

            channel.basic_consume(queue='tasks', on_message_callback=callback, auto_ack=False)
            print(' [*] Ожидание новых задач для анализа...', flush=True)
            channel.start_consuming()
        except Exception:
            print("Ожидание RabbitMQ...", flush=True)
            time.sleep(5)

if __name__ == '__main__':
    main()