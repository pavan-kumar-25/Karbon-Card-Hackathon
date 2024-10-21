from flask import Flask, render_template, request, redirect, url_for
import json
from model import probe_model_5l_profit

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            data = json.load(file) 
            # print("Uploaded data:", data)  # Debugging output

            if "data" not in data:
                return "Invalid data structure", 400  

            result = probe_model_5l_profit(data["data"])  
            return render_template('result.html', result=result)
    

    return render_template('upload.html')



if __name__ == '__main__':
    app.run(debug=True)
