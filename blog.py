from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from datetime import datetime

app = Flask(__name__)
api = Api(app)

settings = {
	"site-name" : "",
	"logo" : "",
	"slider" : "",
	"text" : "O Nás",
	"last-actualization" : None
}

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def not_in_setting(setting_id):
	if setting_id not in settings:
		abort(404, f"nastavení {setting_id} neexistuje")

parser = reqparse.RequestParser()

class general_settings(Resource):
	def get(self, setting_id):
		not_in_setting(setting_id)
		if setting_id in ["site-name", "logo", "text"]:
			if isinstance(setting_id, str) == False or len(setting_id) > 100:  #pouze site-name kratší jak 100
				abort(404, f"jméno stránky {setting_id} nelze použít")
		return {setting_id : settings[setting_id]}

	def put(self, setting_id):
		not_in_setting(setting_id)
		settings["last-actualization"] = get_timestamp()
		settings[setting_id] = request.form["data"]
		return {setting_id : settings[setting_id]}
		
actions = {
	"name" : "",
	"date" : None,
	"text" : "",
	"photo" : None,

}

def not_in_actions(action_id):
	if action_id not in actions:
		abort(404, f"akce {action_id} neexistuje")


class events(Resource):
	def get(self, action_id):
		not_in_actions(action_id)
		if action_id in ["name", "photo", "text"]:
			if isinstance(action_id, str)  == False:
				abort(404, f"akce {action_id} nelze použít")
		return {action_id : actions[action_id]}

	def post(self, action_id):
		not_in_actions(action_id)
		pass

	def put(self, action_id):
		not_in_actions(action_id)
		pass

	def delete(self, action_id):
		not_in_actions(action_id)
		pass

"""
class news(Resource):
	def get(self):
		return {"hello":"world"}

	def post(self):
		pass

	def put(self):
		pass

	def delete(self):
		pass"""

api.add_resource(general_settings, "/general_settings/<string:setting_id>")
"""api.add_resource(events, "/events")
api.add_resource(news, "/news")"""

if __name__ == "__main__":
	app.run(debug=True)

"""
curl http://localhost:5000/general_settings/site-name -d "data=1" -X PUT

"""