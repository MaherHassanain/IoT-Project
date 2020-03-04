import logging
import asyncio

from hbmqtt.client import MQTTClient, ConnectException
from hbmqtt.mqtt.constants import QOS_1, QOS_2

logger = logging.getLogger(__name__)

config = {
    'will': {
        'topic': 'test/test',
        'message': b'Dead or alive',
        'qos': 0x01,
        'retain': True
    }
}

@asyncio.coroutine
def test_coro():
    C = MQTTClient()
    yield from C.connect('mqtt://localhost:9999')
    C.publish("Message from coro1 !!!!!!")
    logger.info("messages published")
    yield from C.disconnect()


if __name__ == '__main__':
    formatter = "[%(asctime)s] %(name)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    formatter = "%(message)s"
    logging.basicConfig(level=logging.DEBUG, format=formatter)
    asyncio.get_event_loop().run_until_complete(test_coro())
    asyncio.get_event_loop().run_forever()
