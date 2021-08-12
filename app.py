from flask import Flask,render_template,request
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pins = [18,21,20]
GPIO.setup(pins,GPIO.OUT)
app = Flask(__name__)
@app.route('/',methods = ['POST','GET'])
def home():
    if request.method=='POST':
        status = [request.form['red status'],request.form['green status'],request.form['blue status']]
        if status[0]=='on':
            GPIO.output(18,True)
        if status[1]=='on':
            GPIO.output(21,True)
        if status[2]=='on':
            GPIO.output(20,True)
        if status[0]=='off':
            GPIO.output(18,False)
        if status[1]=='off':
            GPIO.output(21,False)
        if status[2]=='off':
            GPIO.output(20,False)
    return render_template('GPIO control.html')
if __name__=='__main__':
    app.run(debug=True)
