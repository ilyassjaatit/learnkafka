from json import dumps

from kafka import KafkaProducer


class Producer:
    """Base producer kafka"""
    USER_TOPIC = 'backend-user'

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers='broker:29092',
            value_serializer=lambda x: dumps(x).encode('utf-8')
        )

    def send(self, data):
        self.producer.send(self.USER_TOPIC, data).add_callback(self._on_send_success).add_errback(self._on_send_error)

    def _on_send_error(self, excp):
        print('This is terrifying {}'.format(excp))

    def _on_send_success(self, metadata):
        print(metadata.topic)
        print(metadata)
