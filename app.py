from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cnc_name = request.form['cnc_name']
        material = request.form['material']
        additional_criteria = request.form['additional_criteria']
        message = f"""Pretend to be a CNC machine expert/chatbot,now answer this, I want possibly a {cnc_name} for {material}, {additional_criteria} help me find a perfect CNC machine for this purpose, make sure to mention only one cnc machine and give 2 lines description about it thats it nothing else. ALso remember you can only answer related to CNC's and nothing else Here is how you will answer,
                    Toolname:
                    Reasoning in bullet points:
                    Conclusion/brief description about the tool:
                    then finally ask the me if I have any further questions."""
        return render_template('result.html', initiate=message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)

