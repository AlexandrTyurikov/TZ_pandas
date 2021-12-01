import requests
import pandas as pd


API_KEY = 'BQY5ekM08yJ1j0FS211gS8xCKaRuE994'


def run_query(query):
	headers = {'X-API-KEY': API_KEY}
	request = requests.post('https://graphql.bitquery.io/',json={'query': query}, headers=headers)
	if request.status_code == 200: return request.json()
	else: raise Exception('Query failed and return code is {}.{}'.format(request.status_code, query))


def get_swap_prices(token_address, base_address, since):
	query = '''
	{
  		ethereum(network: ethereum) {
    		dexTrades(
      			date: {since: "%s"}
      			quoteCurrency: {is: "%s"}
      			baseCurrency: {is: "%s"}
      			exchangeName: {in: ["<Uniswap v2>", "Balancer", "<Curve>", "SushiSwap"]}
    ) {
      		timeInterval {
        	minute(format: "%%FT%%TZ", count: 1)
      }
      		price: quotePrice(calculate: average)
    	}
  	}
	}
	''' % (since,base_address,token_address)
	result = run_query(query)['data']['ethereum']['dexTrades']
	df = pd.DataFrame(result)
	
	df['timeInterval'] = df['timeInterval'].apply(lambda x: x['minute'][:-10] + ' '+ x['minute'][11:-4])
	df.rename({'timeInterval': 'time'}, axis=1, inplace=True)
	
	return df
