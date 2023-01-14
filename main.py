from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def mainRoute():
    return jsonify('Welcome to quran api by TamDev')

@app.route('/getArabicTxt/<urlAudio>')
def arabicTxt(urlAudio):
   
    # arabTxt = urlAudio
    return urlAudio


if(__name__ == '__main__'):
    app.run(debug=True)