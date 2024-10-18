from flask import Flask, render_template, request, redirect, url_for, session
import json
from model import probe_model_5l_profit

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and file.filename == 'data.json':
            content = file.read()
            data = json.loads(content)
            result = probe_model_5l_profit(data["data"])
            session['result'] = result  
            return redirect(url_for('show_result'))
        else:
            return 'Invalid file. Please upload data.json'
    return render_template('upload.html')

@app.route('/result')
def show_result():
    result = session.get('result', None)
    if result is None:
        return redirect(url_for('upload_file'))
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)