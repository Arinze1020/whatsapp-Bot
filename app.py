from flask import Flask, request 
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)
@app.route('/')
def Home():
	return "<h1> Hi am wbot</h1>"

@app.route('/sms',methods=['post'])
def sms_reply():
	msg = request.form.get("Body")
	resp = MessagingResponse()
	resp.message("you said:{}".format(msg))
	return str(resp)
if __name__ == '__main__':
	app.run(debug=True)