from influxdb import InfluxDBClient
from kafka import KafkaProducer

from configMaster import ConfigMaster

import json

class KafkaPublisher():

	configMaster = ConfigMaster()
	producer = KafkaProducer(bootstrap_servers=configMaster.config["kafka_server"])
	topic_name = configMaster.config["kafka_topic"]

	def publish(self, data):
		data = json.dumps(data[0])
		data = data.encode("utf-8")
		self.producer.send(self.topic_name, data)
		self.producer.flush()