from dotenv import load_dotenv
import os
from decouple import config
# 방법 1
load_dotenv()
client_id = os.getenv('Client_ID')
print('방법1 :',client_id)
# 방법 2
client_id = config('Client_ID')
print('방법2 :',client_id)
