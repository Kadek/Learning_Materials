import json
import os

class ConfigMaster():

	config = {}

	def __init__(self):
                current_path = os.path.dirname(os.path.abspath(__file__))
                self.load_config(current_path+"/config.json")

	def load_config(self, filename):
		with open(filename) as config_file:
			self.config = json.load(config_file)

if __name__ == "__main__":
	configMaster = ConfigMaster()
	print(configMaster.config)
