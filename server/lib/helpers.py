#!/usr/bin/env python3
import random
import string


def randomStr(size):
    source = string.ascii_letters + string.digits
    result_str = "".join((random.choice(source) for i in range(size)))
    return result_str
