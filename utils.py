import hmac
import math
import time
import base64
import hashlib


def get_guard_code(key, timestamp=time.time()):
    steam_guard_code_table = [50, 51, 52, 53, 54, 55, 56, 57, 66, 67, 68, 70, 71,
                              72, 74, 75, 77, 78, 80, 81, 82, 84, 86, 87, 88, 89]
    decoded_shared_secret = base64.b64decode(bytes(key, "utf-8"))
    time_bytes = int(int(timestamp) / 30).to_bytes(8, byteorder="big")
    time_left = 30 - int(timestamp) % 30
    hmac_generator = hmac.new(decoded_shared_secret, time_bytes, hashlib.sha1)
    hashed_data = hmac_generator.digest()
    b = hashed_data[19] & 0xF
    code_point = (hashed_data[b] & 0x7F) << 24 | \
                 (hashed_data[b + 1] & 0xFF) << 16 | \
                 (hashed_data[b + 2] & 0xFF) << 8 | \
                 (hashed_data[b + 3] & 0xFF)
    code_array = []
    for i in range(5):
        code_array.append(steam_guard_code_table[code_point % len(steam_guard_code_table)])
        code_point = math.floor(code_point / len(steam_guard_code_table))
    return ''.join(chr(i) for i in code_array), time_left
