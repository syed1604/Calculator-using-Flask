from flask import Flask,request,jsonify,render_template
app=Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/math", methods=["POST","GET"])
def calc():
    if request.method=="POST":
        operation=request.form['operation']
        n1=int(request.form['num1'])
        n2=int(request.form['num2'])
        if operation =="+":
            res=n1+n2
            result=res
        elif operation =="-":
            res=n1-n2
            result=res
        elif operation =="*":
            res=n1*n2
            result=res
        elif operation =="/":
            res=n1/n2
            result=res
    return render_template('index.html',input1=n1,input2=n2,operation=operation,result=result,calculation_success=True)



@app.route("/postman", methods=["POST"])
def calct():
    if request.method=="POST":
        operation=request.json['operation']
        n1=int(request.json['num1'])
        n2=int(request.json['num2'])
        if operation =="Add":
            res=n1+n2
            result=f'{n1}+{n2} = {res}'
        if operation =="Sub":
            res=n1-n2
            result=f'{n1}-{n2} = {res}'
        if operation =="Mul":
            res=n1*n2
            result=f'{n1}x{n2} = {res}'
        if operation =="Div":
            res=n1/n2
            result=f'{n1}/{n2} = {res}'
            
    return (result)

if __name__=="__main__":        
    app.run(debug=True)