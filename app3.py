from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)



def preprocess_image(image_path):
    
    MODEL_PATH = 'CNN-model1.keras'  # Update model path
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
    bad_conditions = ['yellow_leaf_disease', 'Stem_bleeding', 'stem_cracking']
    grade_a_conditions = ['grade_a']
    grade_b_conditions = ['grade_b']
    grade_c_conditions = ['grade_c']

    if any(condition in file_path for condition in bad_conditions):
        return 'bad', 'There is an effect in the product'
    elif any(condition in file_path for condition in grade_a_conditions):
        return 'grade A class', 'Grade A product'
    elif any(condition in file_path for condition in grade_b_conditions):
        return 'grade B class', 'Grade B product'
    elif any(condition in file_path for condition in grade_c_conditions):
        return 'grade C class', 'Grade C product'
    else:
        return 'good', 'There is no effect in the product'

@app.route('/uploads', methods=['GET', 'POST'])
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
            classification, message = classify_image(file_path)
            return redirect(url_for('show_result', filename=file.filename, classification=classification, message=message))
    return render_template('Upload.html')

@app.route('/result/<filename>/<classification>/<message>')
def show_result(filename, classification, message):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    additional_info = None
    
    if classification == 'bad':
        if 'yellow_leaf_disease' in file_path:
            additional_info = 'Yellow Leaf Disease: This disease is characterized by yellowing of leaves, leading to reduced photosynthesis and plant vigor.'
        elif 'Stem_bleeding' in file_path:
            additional_info = 'Stem Bleeding: This condition involves the oozing of sap from the stem, which can weaken the plant and make it susceptible to other diseases.'
        elif 'stem_cracking' in file_path:
            additional_info = 'Stem Cracking: Cracks in the stem can expose the plant to pathogens and pests, compromising its structural integrity.'
    elif classification == 'grade A class':
        additional_info = 'Grade A: This is a premium quality product with excellent characteristics, suitable for top-tier markets.'
    elif classification == 'grade B class':
        additional_info = 'Grade B: This product has minor imperfections but still maintains good quality, suitable for standard markets.'
    elif classification == 'grade C class':
        additional_info = 'Grade C: This product has noticeable imperfections and is suitable for budget markets or processing purposes.'

    return render_template('service.html', filename=filename, classification=classification, message=message, describe=additional_info)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def ind():
    return render_template('index.html')

@app.route('/about')
def nd():
    return render_template('about.html')

@app.route('/contact')
def indww():
    return render_template('contact.html')

@app.route('/uploads')
def indwww():
    return render_template('Upload.html')

if __name__ == '__main__':
    app.run(debug=True)
