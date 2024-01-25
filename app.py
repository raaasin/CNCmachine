from flask import Flask, render_template, request
import google.generativeai as genai
from flask import jsonify
app = Flask(__name__)

genai.configure(api_key="AIzaSyDWflxCyU3_pSzXjW-k91I9G6mvzUQ2q2U")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def get_message(message):
    response = chat.send_message(message)
    response.resolve()
    print(response.text)
    return response.text
flag = 0
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cnc_name = request.form['cnc_name']
        material = request.form['material']
        additional_criteria = request.form['additional_criteria']
        message = f"Pretend to be a CNC machine expert/chatbot,now answer this, {cnc_name} for {material}, {additional_criteria} help me find a perfect CNC machine for this purpose, make sure to mention only one cnc machine and give 2 lines description about it thats it nothing else."
        return render_template('result.html', initiate=message)

    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['message']
    #print("recieved",user_message)
    chat_response = get_message(user_message)  
    return jsonify({'response': chat_response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)

