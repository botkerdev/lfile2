from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join('uploads', filename))
        return 'file uploaded successfully'

    return '''
<!DOCTYPE html>
<html>
    <head>
        <title>파일 업로드</title>
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');
body {
    background-color: #181818;
}
h1 {
    text-align: center;
    margin-top: 100px;
    font-size: 75px;
}
h2 {
    text-align: center;
    margin-top: 100px;
    font-size: 25px;
}
        </style>
    </head>
    <body>
        <h2>파일 업로드</h2>
        <form method="post" enctype="multipart/form-data">
            파일 고르기 : 
            <input type="file" name="file" id="file">
            <button type="submit">전송</button>
        </form>
    </body>
</html>
    '''

@app.route('/uploads/<filename>', methods=['GET'])
def download_file(filename):
    try:
        return send_file(os.path.join('uploads', filename), attachment_filename=filename)
    except:
        return 'file not found'

if __name__ == '__main__':
    app.run(debug=True)
