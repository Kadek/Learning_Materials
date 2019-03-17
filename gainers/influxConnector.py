from influxdb import InfluxDBClient
from kafka import KafkaConsumer

from configMaster import ConfigMaster
from influxDataTransformer import InfluxDataTransformer

import json

class InfluxConnector():

	configMaster = ConfigMaster()
	address = configMaster.config["influx_address"]
	port = configMaster.config["influx_port"]
	username = configMaster.config["influx_username"]
	password = configMaster.config["influx_password"]
	db = configMaster.config["influx_db"]

	consumer = KafkaConsumer(configMaster.config["kafka_topic"], bootstrap_servers=configMaster.config["kafka_server"])

	def run(self):
		print("Listening for messages...")
		for message in self.consumer:
			print("Received message: {}".format(message))

			message = self.decode_message(message)
			print("Decoded message: {}".format(message))

			message = self.parse_message(message)
			print("Parsed message: {}".format(message))

			self.save_message(message)
			print("Message saved.")

	def decode_message(self, message):
		message = message.value
		message = message.decode("utf-8")
		message = json.loads(message)
		return message

	def parse_message(self, message):
		influxDataTransformer = InfluxDataTransformer()
		return influxDataTransformer.parse_message(message)

	def save_message(self, message):
		client = InfluxDBClient(self.address, self.port, self.username, self.password, self.db)
		client.write_points(message)
		client.close()		

if __name__ == "__main__":
	influxConnector = InfluxConnector()
	influxConnector.run()