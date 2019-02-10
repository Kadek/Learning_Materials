from influxdb import InfluxDBClient
from kafka import KafkaConsumer

from configMaster import ConfigMaster

import json

class InfluxConnector():

	configMaster = ConfigMaster()
	address = configMaster.config["address"]
	port = configMaster.config["port"]
	username = configMaster.config["username"]
	password = configMaster.config["password"]
	db = configMaster.config["db"]
	tables = configMaster.config["tables"]

	consumer = KafkaConsumer(configMaster.config["kafka_topic"], bootstrap_servers=configMaster.config["kafka_server"])

	def run(self):
		print("Listening for messages...")
		for msg in self.consumer:
			msg = msg.value
			msg = msg.decode("utf-8")
			msg = [json.loads(msg)]
			print("received msg: {}".format(msg))
			client = InfluxDBClient(self.address, self.port, self.username, self.password, self.db)
			client.write_points(msg)
			client.close()

if __name__ == "__main__":
	influxConnector = InfluxConnector()
	influxConnector.run()