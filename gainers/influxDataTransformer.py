class InfluxDataTransformer():

	data_types = {
		"coin": "coin_transformer", 
		"market": "market_transformer"
	}
	
	def parse_message(self, data):
		func = getattr(self, self.data_types[data["table"]])
		return func(data)

	def coin_transformer(self, data):
		result = {}
		result["measurement"] = "coin"

		tags = ["acronym", "timespan"]
		tags_data = {}
		for tag in tags:
			tags_data[tag] = data[tag]
			del data[tag]
		result["tags"] = tags_data

		del data["table"]
		result["fields"] = data

		return [result]

	def market_transformer(self, data):
		result = {}
		result["measurement"] = "market"

		result["tags"] = {"name": data["name"]}
		del data["name"]
		
		del data["table"]
		result["fields"] = data

		return [result]

if __name__ == "__main__":
	dt = InfluxDataTransformer()

	json = {"measurement": "mydb", "fee type": "Percentage", "price": "\n$0.013649\n", "volume": "\n$499,926\n", "category": "Spot", "name": "HADAX", "volume %": "49.14", "acronym": "DAC/ETH", "updated": "Recently"}
	print(dt.transform(json, "market"))
	
	json = {"change": "-22.37%", "acronym": "WT", "name": "WeToken", "price": "$0.002931", "volume": "$54,346", "link": "/currencies/wetoken/", "timespan": "1d"}
	print(dt.transform(json, "coin"))
