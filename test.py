import os
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/',methods=['GET'])
def test():
    return Response("It works!")

if __name__ == "__main__":
    app.run(debug=True)
