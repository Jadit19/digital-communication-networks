# Assignment 1: Bonus Question

## Setup

You'll need OpenCV to run this. Install it using:

```sh
pip3 install opencv-python
```

In a terminal, navigate to this directory and run the command:

```sh
python3 server.py
```

Fire up a new terminal, navigate to this directory and run the command:

```sh
python3 client.py
```

You may fire up any number of clients (till 10) you want but make sure that only a single server is running. If you face any issues, try changing line #53 of [server.py](./server.py) to fit the port and maximum number of connections accoring to your needs. Change the [client.py](./client.py) code accordingly to hit the changed server port.

## Directory Structure

```
.
├── client.py
├── README.md
└── server.py
```
