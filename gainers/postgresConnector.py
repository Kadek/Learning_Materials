import psycopg2
from kafka import KafkaConsumer

from configMaster import ConfigMaster
from postgresDataTransformer import PostgresDataTransformer

import json

class PostgresConnector():

	configMaster = ConfigMaster()
	address = configMaster.config["postgres_address"]
	port = configMaster.config["postgres_port"]
	username = configMaster.config["postgres_username"]
	password = configMaster.config["postgres_password"]
	db = configMaster.config["postgres_db"]
	schema = configMaster.config["postgres_schema"]

	consumer = KafkaConsumer(configMaster.config["kafka_topic"], bootstrap_servers=configMaster.config["kafka_server"])

	def run(self):
		print("Listening for messages...")
		for message in self.consumer:
			print("Received message: {}".format(message))

			message = self.decode_message(message)
			print("Decoded message: {}".format(message))

			(message, table_name) = self.parse_message(message)
			print("Parsed message: {}".format(message))

			(sql_statement, parameters) = self.prepare_statement(message, table_name)
			print("Prepared SQL query: {} {}".format(sql_statement, parameters))

			self.save_message(sql_statement, parameters)
			print("Message saved.")

	def decode_message(self, message):
		message = message.value
		message = message.decode("utf-8")
		message = json.loads(message)
		return message

	def parse_message(self, message):
		postgresDataTransformer = PostgresDataTransformer()
		return postgresDataTransformer.parse_message(message)

	def prepare_statement(self, message, table_name):
		parameters = []

		column_names = self.schema[table_name].copy()
		table_size = len(column_names)
		column_names.append("entry_time")
		column_names = ", ".join(column_names)

		value_placeholders = ",".join(["%s"] * table_size)
		value_placeholders += ", CURRENT_TIMESTAMP"

		sql_statement = "INSERT INTO {}({}) VALUES ({})".format(
				table_name, 
				column_names,
				value_placeholders
			)

		parameters = tuple(message[attribute] for attribute in self.schema[table_name])

		return (sql_statement, parameters)

	def save_message(self, sql_statement, parameters):
		client = psycopg2.connect(host=self.address,database=self.db, user=self.username, password=self.password, port=self.port)
		
		cursor = client.cursor()
		cursor.execute(sql_statement, parameters)
		client.commit()
		cursor.close()

		if client is not None:
			client.close()

if __name__ == "__main__":
	postgresConnector = PostgresConnector()
	postgresConnector.run()