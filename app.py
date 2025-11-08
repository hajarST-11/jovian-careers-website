from flask import Flask 
app=Flask(__name__)

@app.route("/")
def hello():
  return "heyyy"
  
print(__name__)
if __name__ == "__main__":
    print("i am inside")
    app.run(host='0.0.0.0', port=5000, debug=True)

