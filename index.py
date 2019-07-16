
from flask import Flask,request
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def faceRecognition():
    """
    描述：负责识别照片确认照片人物身份
    """
    return 'Hello World!'

def faceInputImage():
    """
    描述：负责人脸照片上传
    """
    return 

def SpeechToText(voice):
    """
    描述：输入语音输出文字
    """
    return 

def TextToSpeech(text):
    """
    描述：输入文字转语音
    """
    return

def  Dialogue(text):
    """
    描述：文字转文字
    """
    return 
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')