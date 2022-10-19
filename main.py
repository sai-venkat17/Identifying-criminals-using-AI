from flask import Flask,request,render_template
import insert_criminal
import report_criminal


app=Flask(__name__)
@app.route('/')
def test():
    return "Main server is running"

@app.route('/insert_criminal',methods=['POST'])
def insert_criminal_route():
    print("1. Called insert criminal API")
    return insert_criminal.insert_criminal(request)

@app.route('/report_crime',methods=['POST'])
def report_crime_route():
    return report_criminal.report_criminal(request)

@app.route('/insert_criminal',methods=['GET'])
def insert_criminal_route_frontend():
    return render_template(
        'administrator_portal.html'
    )

@app.route('/report_criminal',methods=['GET'])
def report_criminal_route_frontend():
    return render_template(
        'report_crime_portal.html'
    )


