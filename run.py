import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key="randomstring123"
messages = []

def add_messages(username, message):
    """Add message to the 'messages' list"""
    npw = datetime.now().strftime("%H:%M:%S")
    message_dict = {"timestamp": now, "from": username, "message": message}
    messages.append(messages_dict)



@app.route('/', methods=['GET', 'POST'])
def index():
    """Main Page with Instruction"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")

    

    @app.route('/username')
    def user(username):
        """Display chat messages"""
        return render_template("chat.html", username = username, chat_messages = messages)

    @app.route('/<username>/<message>')
    def send_message(username, message):
        """Create a new message and redirect to chat page"""
        add_messagesformat(username, message)
        return redirect("/" + username)   

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
