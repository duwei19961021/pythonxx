# -*- coding: utf-8 -*-
import logging
import traceback
logger1 = logging.basicConfig(filename="error.log",
                              format='%(asctime)s - %(name)s - %(levelname)s -%(module)s: %(message)s',
                              level=30)
def func():
    try:
        a = a + 1
    except Exception as e:
        msg = traceback.format_exc()
        logging.error(msg)
func()