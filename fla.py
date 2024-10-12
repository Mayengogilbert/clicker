from flask import Flask, request
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print("clicked")
        return "clicked"
    return """
    <html>
     <body>
     <form method="POST">
     <button type="submit">CLICK HERE</button>
     </form>
     </body>
    </html>
    """
if __name__ == '__main__':
    app.run(debug=True)
