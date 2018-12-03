from influxdb import InfluxDBClient

class DBConnector():

	address = "localhost"
	port = "8086"
	username = "root"
	password = "root"
	dbs = ["coin", "market"]

	def save(self, data, data_type):
		if(data_type not in self.dbs):
			return "No such database"

		client = InfluxDBClient(self.address, self.port, self.username, self.password, data_type)
		client.write_points(data)
		client.close()

if __name__ == "__main__":
	db = DBConnector()

	data = [{'fields': {'change': '-22.37%', 'volume': '$54,346', 'price': '$0.002931', 'link': '/currencies/wetoken/', 'name': 'WeToken'}, 'tags': {'acronym': 'WT'}, 'measurement': 'coin'}]
	print(db.save(data, "coin"))

	data = [{'fields': {'volume %': '49.14', 'category': 'Spot', 'price': '\n$0.013649\n', 'volume': '\n$499,926\n', 'fee type': 'Percentage', 'updated': 'Recently', 'acronym': 'DAC/ETH'}, 'tags': {'name': 'HADAX'}, 'measurement': 'market'}]
	print(db.save(data, "market"))