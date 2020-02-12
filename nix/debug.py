#!/usr/bin/python

import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)

for path in os.environ["PATH"].split(":"):
    logger.info(path)
    if os.path.exists(path):
        for cmd in os.listdir(path):
            logger.info(cmd)