from confluent_kafka import Consumer, KafkaException

def assignment_callback(consumer, partitions):
    for p in partitions:
        print(f'Assigned to {p.topic}, partition {p.partition}')

if __name__ == '__main__':
    config = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'hello_group',
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': False,

    }
    consumer = Consumer(config)
    consumer.subscribe(['hello_topic'], on_assign=assignment_callback)

    try:
        while True:
            event = consumer.poll(1.0)
            if event is None:
                continue
            if event.error():
                raise KafkaException(event.error())
            else:
                val = event.value().decode('utf8')
                partition = event.partition()
                print(f'Received: {val} from partition {partition}    ')

    except KeyboardInterrupt:
        print('Canceled by user.')
    finally:
        consumer.close()