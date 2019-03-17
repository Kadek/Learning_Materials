class PostgresDataTransformer():

	data_types = {
		"coin": "coin_transformer", 
		"market": "market_transformer"
	}
	
	def parse_message(self, data):
		func = getattr(self, self.data_types[data["table"]])
		return func(data)

	def coin_transformer(self, data):
		table_name = data["table"]
		del data["table"]

		data["change"] = data["change"][:-1]
		data["price"] = data["price"][1:]
		data["volume"] = data["volume"][1:].replace(",", "")

		return [data, table_name]

	def market_transformer(self, data):
		table_name = data["table"]
		del data["table"]

		data["fee_type"] = data["fee type"]
		del data["fee type"]
		
		data["price"] = data["price"].strip()[1:]
		data["volume"] = data["volume"].strip()[1:].replace(",", "")
		data["volume_share"] = data["volume %"]

		return [data, table_name]

if __name__ == "__main__":
	dt = PostgresDataTransformer()

	json = {"table": "market", "fee type": "Percentage", "price": "\n$0.013649\n", "volume": "\n$499,926\n", "category": "Spot", "name": "HADAX", "volume %": "49.14", "acronym": "DAC/ETH", "updated": "Recently"}
	print(dt.transform(json))
	
	json = {"table": "coin", "change": "-22.37%", "acronym": "WT", "name": "WeToken", "price": "$0.002931", "volume": "$54,346", "link": "/currencies/wetoken/", "timespan": "1d"}
	print(dt.transform(json))
