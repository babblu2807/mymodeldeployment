from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

@app.route('/welcome')
def welcome():
        return render_template('index.html')
@app.route('/suces/<int:score>')
def suce(score):
 return render_template('result.html',s=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',s=score)

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result="fail"
    else:
        result="suce"
    return redirect(url_for(result,score=marks))


@app.route('/submit',methods=['POST','GET'])
def getdetails():
    total_score=0
    if request.method=='POST':
        s=int(request.form['science'])
        m=int(request.form['math'])
        avg=float((s+m)/2)
        return redirect(url_for('fail',score=avg))

if __name__=='__main__':
    app.run(debug=True)
