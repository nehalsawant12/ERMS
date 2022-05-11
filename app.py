from flask import Flask,render_template,request
from flask.helpers import url_for
from werkzeug.utils import redirect

import database as db
from models import Employee
import os 
app = Flask(__name__)


@app.route("/")
def index():
    emplist=db.all()
    return render_template('index.html',emplist=emplist)


    
@app.route("/empform")
def empform():
    emp = Employee()  # object is empty
    return render_template("empform.html",action="Save", emp=emp)

@app.route("/Edit/<int:eid>")
def emp_Edit(eid):
    emp = db.get(eid)
    return render_template("empform.html",action="Update" , emp=emp)

# by default every URL handle only get method not a post.
@app.route("/empsave", methods=["POST"])
def empsave():
    ename = request.form.get('ename')
    esalary = request.form['esalary']
    image = request.files['eimage']
    eimage = image.filename
    print(os.getcwd())
    imgpath = os.path.join("static\\uploadedimage",eimage)
    image.save(imgpath)
    db.create(ename,esalary,imgpath)
    return redirect(url_for('index'))

@app.route("/Delete/<int:eid>")
def Delete_emp(eid):
    db.Delete(eid)
    return redirect(url_for('index'))

@app.route("/empUpdate", methods = ['POST'])
def empUpdate():
    eid = request.form.get('eid')
    ename = request.form.get('ename')
    esalary = request.form['esalary']
    image = request.files['eimage']
    print(image,type(image),image.filename)
    if image.filename == "":
        emp = db.get(eid)
        imgpath = emp.eimage
    else:
        eimage = image.filename
        imgpath = os.path.join("static/uploadedimage",eimage)
        image.save(imgpath)
    db.update(ename,esalary,imgpath,eid)
    return redirect(url_for('index'))


if __name__=="__main__":
    app.run(debug=True)