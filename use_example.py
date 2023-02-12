import zmq
import time
import os

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)
sample_json = """{
  "firstName": "Kenneth",
  "lastName": "Street",
  "id": 1,
  "budget": 1000,
  "categories":
    {
      "housing":
      {
        "rent": 500,
        "electricity": 50,
        "cable": 25
      },
      "charity":
      {
        "church": 25
      }
    }
}"""
file_path = os.getcwd()+'/' + 'program'
file_name = 'new_chart.png'
destfile = file_path + '/' +file_name

if os.path.isfile(destfile):
    os.remove(destfile)
    time.sleep(2)



    #send_msg = input("sending a message")
def send_json(j_string):
    socket.send_string(j_string)
    rcv_msg = socket.recv()
    print("received message")
    f = open(destfile, 'wb')
    f.write(rcv_msg)
    f.close()

while True:
    prompt = input("send a JSON? y/n")
    if prompt == 'y':
        send_json(sample_json)
