from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from main import getPrediction
import os

#create a folder the save the uploaded image
UPLOAD_FOLDER = 'static/images/'

#Create an app object using the Flask class. 
app = Flask(__name__, static_folder="static")

# Set the secret key for session management
# Set the secret key for secure session management and cookie encryption
# The secret key ensures data integrity and prevents tampering by unauthorized users
# Replace the default value with a unique and confidential secret key for enhanced security

app.secret_key = "secret key" 

#Define the upload folder to save images uploaded by the user. 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Defining the home route
# The decorator below associates the URL's relative route with the corresponding function.
# In this case, the index function is assigned to '/', which represents the root directory of the application.
# When the app is running, accessing the root URL will render the index.html template.
# The render_template function is responsible for locating the HTML file within the templates folder.
@app.route('/')
@app.route('/')
def index():
    return render_template('index.html')

#Post decorator to submit the form. 
@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)  #Use this werkzeug method to secure filename. 
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            #getPrediction(filename)
            label = getPrediction(filename)
            flash(label)
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            flash(full_filename)
            return redirect('/')
@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/source-code')
def source_code():
    return redirect('https://github.com/NedaMhv/Ham10000/blob/main/skin_cancer_final.ipynb')


if __name__ == "__main__":
    app.run(debug=True)
