from flask import Flask, render_template, request, send_file, Response
import convert
import os

app = Flask(__name__, static_folder="build/static", template_folder="build")

@app.route('/convert', methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
            image_path = './input/image.png'
            image.save(image_path)
            
            # Save the image or perform further processing
            convert.convert(image_path)
            return send_file('./output/sheet.txt', as_attachment=True)
        return 'No image in the request'
    return 'Upload page'

@app.route('/test', methods=["GET", "POST"])
def test():
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
            print(image)
            image_path = './input/image.png'
            image.save(image_path)
            
            # Save the image or perform further processing
            return send_file('./output/sheet.txt', as_attachment=True)
        print('No image in the request')
        return 'No image in the request'
    print('Upload page')
    return 'Upload page'

    # Serve React App
@app.route('/')
def serve():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
