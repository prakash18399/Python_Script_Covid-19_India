import requests

data = requests.get('https://api.rootnet.in/covid19-in/stats/latest').json()
length1 = len(data['data']['unofficial-summary'])
length2 = len(data['data']['regional'])

for i in range(length1):
	print("*****************************************************")
	print("Total Covid-19 Cases in India\t",data['data']['unofficial-summary'][i]['total'])
	print("*****************************************************")
	print("Total Recovered Cases in India\t",data['data']['unofficial-summary'][i]['recovered'])
	print("*****************************************************")
	print("Total Active Cases in India\t",data['data']['unofficial-summary'][i]['active'])
	print("*****************************************************")
	print("Total Deaths Cases in India\t",data['data']['unofficial-summary'][i]['deaths'])
	print("*****************************************************")
	print("\n\n")

for j in range(length2):
	print("*****************************************************")
	print("\t",data['data']['regional'][j]['loc'])
	print("*****************************************************")
	print("Confirmed Indian Cases \t",data['data']['regional'][j]['confirmedCasesIndian'])
	print("*****************************************************")
	print("Recovered Cases \t",data['data']['regional'][j]['discharged'])
	print("*****************************************************")
	print("Death Cases     \t",data['data']['regional'][j]['deaths'])
	print("*****************************************************")
	print("\n\n")


