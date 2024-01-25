
import google.generativeai as genai
import sys
import time
genai.configure(api_key="AIzaSyDWflxCyU3_pSzXjW-k91I9G6mvzUQ2q2U")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def get_message(message):
    response = chat.send_message(message, stream=True)
    for chunks in response:
        words = chunks.text.split()
        for word in words:
            print(word, end=' ')
            sys.stdout.flush()
            time.sleep(0.05) 