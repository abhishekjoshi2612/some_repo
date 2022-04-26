from flask import Flask, request, jsonify
import engine
app = Flask(__name__)

file = open("img.txt","r")
string = file.read()

@app.route('/', methods=['POST'])
def hello_world():
    data = request.json
    ans = engine.extract_text(data['img_data'])
    # print(request)
    print(data)
    print(ans)
    return jsonify(ans)

if __name__ == '__main__':
   app.run(debug=True)