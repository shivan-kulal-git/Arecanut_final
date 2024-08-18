from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
MODEL_PATH = 'CNN-model1.keras'  # Update model path
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
   
    img_array = preprocess_image(file_path)
            # Predict the class probabilities
    predictions = model.predict(img_array)
            # Get the predicted class label
    predicted_class = np.argmax(predictions)
            # You can convert class index to class name using your dataset class labels
    class_names = ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7', 'class8', 'class9']
    predicted_label = class_names[predicted_class]

 
def classify_image(file_path):
    bad_conditions = ['yellow_leaf_disease', 'Stem_bleeding', 'stem_cracking', 'Mahali_Koleroga']
    # Determine if the file is in a bad condition folder
    if any(condition in file_path for condition in bad_conditions):
        return 'bad,There is effect in the product '
    else:
        return  'There is no effect in the product'

@app.route('/aboutus', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            classification = classify_image(file_path)
            # Redirect to result page with filename and classification
            return redirect(url_for('show_result', filename=file.filename, classification=classification))
    # Render the index.html template for GET requests or if form submission failed
    return render_template('Upload.html')

@app.route('/result/<filename>/<classification>')
def show_result(filename, classification):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    additional_info = None
    if classification == 'bad,There is effect in the product ':
        # Provide additional information for bad conditions
        additional_info = {
            'yellow_leaf_disease': 'Information about yellow leaf disease.',
            'Stem_bleeding': 'Information about stem bleeding.',
            'stem_cracking': 'Information about stem cracking.',
            'Mahali_Koleroga': 'Information about Mahali Koleroga.'
        }.get(classification, 'Additional information not available.')
    
    return render_template('service.html', filename=filename, classification=classification, additional_info=additional_info)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def ind():
    return render_template('index.html')

@app.route('/about')
def nd():
    return render_template('about.html')

@app.route('/aboutus')
def ndd():
    return render_template('Upload.html')

@app.route('/contact')
def indww():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
