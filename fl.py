from flask import request, jsonify
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

"""def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))"""

@app.route("/general-settings", methods=["GET","PUT"])
def h():
	return """<h1>Distant Reading Archive</h1>
	<p>This site is a prototype API for distant reading of science fiction novels.</p>"""

@app.route("/events", methods=["GET","POST","PUT","DELETE"])

app.run()


