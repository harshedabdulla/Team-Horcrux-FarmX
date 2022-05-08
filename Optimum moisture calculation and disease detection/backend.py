from gevent import monkey; monkey.patch_all()
from flask import Flask, Response, render_template, stream_with_context, request
from gevent.pywsgi import WSGIServer
import json
import csv
import time
import plant_check
import READEACH
import TELLHOMEPAGE

def conditon_send(condit):
    with open("condition.csv",mode='w',newline="") as csvfile :     
        mywriter=csv.writer(csvfile)
        mywriter.writerow(condit) 
        csvfile.close()

def check_motor(a) :
  if a == '1' :
    return "ON"
  elif a == '0' :
    return "OFF"

def send_value(value):
  with open("value.csv",mode='w',newline="") as csvfile :
    mywriter=csv.writer(csvfile)
    mywriter.writerow(value)
    csvfile.close()
   

app = Flask(__name__)

@app.route("/")
def render_index():
  return render_template("hackton.html")

@app.route("/mishalfile")
def render_mishal():
  return render_template("mishalfile.html")

@app.route("/farm-page")
def render_farm():
  return render_template("farm.html")

@app.route("/farm_listen")
def farm_listen():

  def respond_to_client():
    
    
    while True:
        sector_moisture = []
        sector_motor = []
        sector_plant = [] 
        sector_plant_health = []
        sector_shadow = []

        for r in range(1,10) :
          sector_moisture.append(READEACH.moist(r))

        for r in range(1,10) :
          sector_motor.append(check_motor(READEACH.motor(r)))
          

        for r in range(1,10) :
          sector_plant.append(plant_check.sec_color(READEACH.color(r)))
          
        for r in range(1,10):
          sector_plant_health.append(plant_check.check_health(READEACH.color(r)))

        for r in range(1,10):
          sector_shadow.append(plant_check.sec_shadow(READEACH.color(r)))


        _data = json.dumps({"sector_plant" : sector_plant,"sector_motor" : sector_motor,"sector_moisture" : sector_moisture,"sector_plant_health" : sector_plant_health,"sec_shadow":sector_shadow})
        yield f"id: 1\ndata: {_data}\nevent: online\n\n"
        time.sleep(1)
  return Response(respond_to_client(), mimetype='text/event-stream')
  

@app.route('/farm-page/button', methods=['POST'])
def feedback():
  conditon_send("0")
  coordinates = request.form.get("coordinates")
  print(coordinates)
  
  send_value(coordinates)
  with open("section_coordinate.csv",mode='w') as csvfile :    
    mywriter=csv.writer(csvfile)
    mywriter.writerow([coordinates]) 
    csvfile.close()
  return render_template("farm.html")

@app.route("/listen")
def listen():

  def respond_to_client():
    while True:
        avg_humidity = 0
        avg_moisture = 0 
        avg_temp= 0


        for r in range(1,10) :
          avg_humidity = int(READEACH.moist(r))
          avg_humidity += avg_humidity
        for r in range(1,10) :
          avg_temp = int(READEACH.temp(r))
          avg_temp += avg_temp
        for r in range(1,10) :
          avg_moisture = int(READEACH.moist(r))
          avg_moisture += avg_moisture
          
        avg_moisture = round(avg_moisture/9,2)
        avg_humidity = round(avg_humidity/9,2)
        avg_temp = round(avg_temp/9,2)

        _data = json.dumps({"Humidity": avg_humidity, "Tempreature": avg_temp,"Moisture" : avg_moisture})
        yield f"id: 1\ndata: {_data}\nevent: online\n\n"
        time.sleep(0.1)
  return Response(respond_to_client(), mimetype='text/event-stream')


@app.route("/test")
def test():
  colors = {0:'brown', 3:'yellow', 6:"red", 5:"green"}
  def respond_to_test():
    while True:
        
        x= 5#TELLHOMEPAGE.crx()
        y = 4
        colornum = 0
        color = colors[colornum]

        

        _data = json.dumps({"color" : color, 'x':x, 'y':y,"x" : x})
        yield f"id: 1\ndata: {_data}\nevent: online\n\n"
        time.sleep(0.1)
  return Response(respond_to_test(), mimetype='text/event-stream')
                                                                    #WSGI - Web Server Gateway Interface
if __name__ == "__main__":
 
  http_server = WSGIServer(("127.0.0.1", 8080), app)
  http_server.serve_forever() 