from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyDWflxCyU3_pSzXjW-k91I9G6mvzUQ2q2U")

def get_message(message):
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    response = chat.send_message(message, stream=True)
    response.resolve()
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        cnc_name = request.form['cnc_name']
        material = request.form['material']
        additional_criteria = request.form['additional_criteria']

        # Build the message for the API call
        message = f"i want to use it at {cnc_name} for this operation ${material}, with additional criteria ${additional_criteria} just provide the name of one single cnc thats it nothing else"
        answer = get_message(message)

        newmess=f"Describe about The CNC machine '{answer}' in a few short lines"
        about=newmess

        return render_template('result.html', answer=answer, about=about)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
