import zmq
import time
import json
import matplotlib.pyplot as plt
import os

#Set Up Port
port = '5556'
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect('tcp://localhost:%s' % port)

waiting = True

def json_to_budget(path=str):

    #define Chart data
    labels = []
    sizes = []


    data = json.loads(msg)


    total_budget = data['budget']
    for category in data['categories']:
        cat_dict = data['categories'][category]
        labels.append(category)
        sum = 0
        for sub_cat in cat_dict:
            sum += cat_dict[sub_cat]
        sizes.append(sum)

    allocated = 0
    for amount in sizes:
        allocated += amount

    unallocated = total_budget - allocated
    labels.append("Unallocated")
    sizes.append(unallocated)


    #make chart
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')
    print("made new chart " + str(time.time()))
    plt.savefig('micro/chart.png')

def received_message(msg):
    output = msg.decode()
    json_to_budget(output)

def send_file(name):
    size = os.stat(name).st_size
    target = open(name,'rb')
    file = target.read(size)
    if file:
        socket.send(file)

while waiting:
    msg = socket.recv()
    print("received message")
    time.sleep(3)
    received_message(msg)
    send_file('micro/chart.png')

