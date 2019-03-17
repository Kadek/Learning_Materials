from influxdb import InfluxDBClient
from kafka import KafkaProducer

from configMaster import ConfigMaster

import json

class KafkaPublisher():

	configMaster = ConfigMaster()
	producer = KafkaProducer(bootstrap_servers=configMaster.config["kafka_server"])
	topic_name = configMaster.config["kafka_topic"]

	def publish(self, data):
		print("Publishing message: {}".format(data))
		data = json.dumps(data)
		data = data.encode("utf-8")
		self.producer.send(self.topic_name, data)
		self.producer.flush()