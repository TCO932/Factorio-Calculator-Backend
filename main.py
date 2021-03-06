from server import keep_alive
import os
import logging

logger = logging.getLogger('factorio')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='factorio.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

keep_alive()
