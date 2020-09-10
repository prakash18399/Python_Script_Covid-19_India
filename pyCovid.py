import socket
import requests
import matplotlib.pyplot as plt

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


num = []
cases = ['total','recovered','deaths','active']

try:
		socket.create_connection(("www.google.com",80))
		api = "https://api.covidindiatracker.com/total.json"
		res = requests.get(api)
		json = res.json()

		t = json['confirmed']
		r = json['recovered']
		d = json['deaths']
		a = json['active']
		
		num.append(t)
		
		num.append(r)
	
		num.append(d)

		num.append(a)

		print(num)

except OSError as e:
		print(e)


plt.pie(num, labels = cases , explode = [0,0.05,0.2,0.1] , shadow = True , startangle = 45 , colors = ['lightskyblue','g','r','orange'] , autopct = "%0.2f%%")
plt.title("Covid-19 Cases", fontsize = 18)
plt.show()

