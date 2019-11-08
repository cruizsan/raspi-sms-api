from flask import Flask, jsonify, request

from subprocess import Popen, PIPE
import re
import shlex

app = Flask(__name__)

def console(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    out, err = p.communicate()
    return (p.returncode, out, err)

@app.route('/send/sms', methods=["GET", "POST"])
def send_sms():
    number = request.values.get("number")
    text = shlex.quote(request.values.get("text"))
    print(request.values)
    code, out, err = console(' '.join(['gammu', 'sendsms', 'TEXT', number, '-text', text]))
    output = str(out)
    answer = re.search('answer\.\.(.*),', output, re.IGNORECASE)
    if answer:
        answer = str(answer.group(1))
    reference = re.search('reference=(\d+).*', output, re.IGNORECASE)
    if reference:
        reference = str(reference.group(1))
    raw = {
      "code": str(code),
      "out": output,
      "err": str(out),
    }
    return jsonify(raw=raw, reference=reference, answer=answer)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888)

