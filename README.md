# Kafka

Запуск Kafka в Docker:
```
docker-compose up -d
```

Создание Kafka topic'а с именем hello_topic и 6 партициями:
```
docker compose exec broker \
  kafka-topics --create \
    --topic hello_topic \
    --bootstrap-server localhost:9092 \
    --partitions 6
```

Установка confluent_kafka:
```
pip install confluent-kafka
```

Запуск producer'а:
```
python producer.py
```

Результат работы producer'а:

<img width="255" alt="producer" src="https://github.com/AndrewLeonoff/Kafka/assets/133394759/d322d8de-d2c3-47ab-9bda-2e07bbc7d3e0">


Запуск consumer'а:
```
python consumer.py
```

Результат работы consumer'а:

<img width="300" alt="consumer" src="https://github.com/AndrewLeonoff/Kafka/assets/133394759/e39bbecc-b495-4f23-bef6-2aaf3c831f6c">
