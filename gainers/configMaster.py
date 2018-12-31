import json

class ConfigMaster():

	config = {}

	def __init__(self):
		self.load_config("config.json")

	def load_config(self, filename):
		with open(filename) as config_file:
			self.config = json.load(config_file)

if __name__ == "__main__":
	configMaster = ConfigMaster()
	print(configMaster.config)