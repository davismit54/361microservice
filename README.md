# 361microservice
Microservice provided for 361 class

See "Sequence Diagram.png"

Communication Contract:
1. Set up communication port via zmq
Example:

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

2. Send JSON as string
Example:

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
socket.send_string(sample_json)

3. Receive image that is a ".png" file that can be used as desired
Example

rcv_msg = socket.recv()
