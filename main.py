from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                 background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
             textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
   <body>
        <form method="post">
            <label for="Rotate By">Rotate By:</label>
            <input type="text" name="rot" value="0"/>
            <textarea name="text"></textarea>
            <input type="submit" />
        </form>
    </body>
</html> 
"""
def write_form(text=""):
    return form % {'text': cgi.escape(text)}

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]

    rot = int(rot)
    text = rotate_string(text, rot)
    return write_form(text)

app.run()