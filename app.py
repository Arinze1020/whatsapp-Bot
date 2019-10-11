from flask import Flask, request 
from twilio.twiml.messaging_response import MessagingResponse
from utlis import fetch_reply
app = Flask(__name__)
@app.route('/')
def Home():
	return "<h1> Hi i'm wbot</h1>"

@app.route('/sms',methods=['post'])
def sms_reply():
	msg = request.form.get("Body")
	phone_no = request.form.get("From")
	reply = fetch_reply(msg, phone_no)
	resp = MessagingResponse()
	resp.message(reply)
	return str(resp)
if __name__ == '__main__':
	app.run(debug=True)