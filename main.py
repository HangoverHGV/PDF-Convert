from flask import Flask, render_template, redirect, url_for, send_file, request
import convert
import os


app = Flask(__name__)
app.secret_key='akbhidsbvai'
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():

    dir_path = r'files'
    convert.CreateAndDelete(dir_path)
    
    savePath = 'files/'

    file = request.files['pdf']
    if not file:
        return redirect(url_for('index'))
    file.save(savePath + file.filename)
    filePath = savePath + str(os.path.basename(file.filename))
    fileName, fileextension = os.path.splitext(file.filename)

    destination = 'files/' 
    path = 'files/' + fileName + '.docx'
    convert.convert_pdf2docx(filePath, destination)
    var = send_file(path, as_attachment=True)

    return var



if __name__ == "__main__":
    app.run(host='0.0.0.0')



