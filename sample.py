import time
import os
import datetime

greeting = os.getenv("GREETINGS", "hello")
greeting_jp = os.getenv("GREETINGS_JP", "konnichiwa")
time.sleep(20)
out = f'{greeting} in Japanese is {greeting_jp}'
for i in range(19):
	print(i, out, flush=True)
	time.sleep(3)

