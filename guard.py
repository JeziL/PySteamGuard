#!/usr/bin/env python3

import sched
from utils import *
from config import SHARED_SECRET

if __name__ == "__main__":
    s = sched.scheduler(time.time, time.sleep)

    def update_guard_code():
        code, sec = get_guard_code(SHARED_SECRET, time.time())
        print("{0}    Update in {1}s ".format(code, sec), end="\r")
        s.enter(1, 1, update_guard_code)

    s.enter(1, 1, update_guard_code)
    s.run()
