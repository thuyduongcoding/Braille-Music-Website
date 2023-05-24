from flask import Flask, render_template, request, send_file
import convert

app = Flask(__name__)

@app.route('/convert', methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
            image_path = './input/image.png'
            image.save(image_path)
            
            # Save the image or perform further processing
            convert.convert(image_path)
            return send_file('./output/sheet.brf')
        return 'No image in the request'
    return 'Upload page'

@app.route('/hello')
def hello():
    return 'Testing sucess'

if __name__ == '__main__':
    app.run()