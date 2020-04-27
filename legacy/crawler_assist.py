#-*- coding: utf-8 -*-
import random
import time
from selenium.webdriver.common.keys import Keys


def crawling_term(threshold):
    rand_num = random.randrange(3,threshold)
    # term 0.3 ~ 3.0
    time_num = rand_num / float(10)
    time.sleep(time_num)

    return time_num


def crawling_scroll(body):
    body.send_keys(Keys.PAGE_DOWN)

    return 0