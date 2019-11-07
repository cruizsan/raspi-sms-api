from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)


@app.route('/send/sms', methods=["GET", "POST"])
def send_sms():
    number = request.values.get("number")
    text = request.values.get("text")
    return jsonify(
        msg=subprocess.check_output(['gammu', 'sendsms', 'TEXT', number, '-text', text])
    )


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8888)
