from influxdb import InfluxDBClient

from configMaster import ConfigMaster

class DBConnector():

	configMaster = ConfigMaster()
	address = configMaster.config["address"]
	port = configMaster.config["port"]
	username = configMaster.config["username"]
	password = configMaster.config["password"]
	db = configMaster.config["db"]
	tables = configMaster.config["tables"]

	def save(self, data, data_type):
		if(data_type not in self.tables):
			return "No such database"

		client = InfluxDBClient(self.address, self.port, self.username, self.password, self.db)
		client.write_points(data)
		client.close()

if __name__ == "__main__":
	db = DBConnector()

	data = [{'fields': {'change': '-22.37%', 'volume': '$54,346', 'price': '$0.002931', 'link': '/currencies/wetoken/', 'name': 'WeToken'}, 'tags': {'acronym': 'WT', 'timespan': 'gainers-1h'}, 'measurement': 'coin'}]
	print(db.save(data, "coin"))

	data = [{'fields': {'volume %': '49.14', 'category': 'Spot', 'price': '\n$0.013649\n', 'volume': '\n$499,926\n', 'fee type': 'Percentage', 'updated': 'Recently', 'acronym': 'DAC/ETH'}, 'tags': {'name': 'HADAX'}, 'measurement': 'market'}]
	print(db.save(data, "market"))