
# BlackCurve Python API Library 
<img alt='BlackCurve' src="https://blackcurve.io/api/docs/_images/blackcurve-logo.png" width="250">

## API Documentation  
Documentation for the BlackCurve endpoints can be found [here](https://blackcurve.io/api/docs/index.html).  

## Requirements  
* Python 2.7+
* [Requests](http://docs.python-requests.org/en/master/) HTTP library for python v2.0 or above.  
  
## Installation
> `$ pip install requests`  
> `$ pip install blackcurve_api`

## Basic Usage
### Initiate a Connection
You just need your subdomain and a access token to get started
 ```python
	from blackcurve_api import BlackCurveAPI	
	bc = BlackCurveAPI({{ your_subdomain }}, {{ access_token }})	
```
### Reload a Access Token
Need a new access token, or just misplaced the old one?
 ```python
	bc = BlackCurveAPI({{ your_subdomain }})
	token = bc.get_access_token({{ client_key }}, {{ client_secret }})
	print(token)	
```
This will also update your BlackCurveAPI instance with the new token so you can immediately carry on with requests.

### Get Prices
Get a list of current Prices
 ```python
	# get all the prices
	bc.prices().all()
	
	# get all prices
	prices = bc.prices().all()
	print('You have {} prices'.format(len(prices)))
			
	# get a price for a single product by id
	bc.prices().find('42')
	
	# filter specific product columns
	bc.prices(columns=['Price', 'Product ID']).all()
	
	# filter geography
	bc.prices(geography='UK').all()
	
	# filter by column value -- price >= 5
	bc.prices(price_gte=5).all()
	
```

### Data Sources Info
Get column and data type information about your data sources
 ```python
	# get all the data sources
	bc.data_sources_info().all()
	# get a single data source
	bc.data_sources_info().find('Sales History').all()
```
### Data Sources
Get a list of all of the data in a given source
 ```python
	# get all of the data from sales history
	bc.data_sources().find('Sales History').all()
	# get just the volume and product id columns in sales history
	bc.data_sources(columns=['Volume', 'Product ID']).find('Sales History').all()
	# filter by column value -- price >= 5
	bc.data_sources(price_gte=5).find('Sales History').all()
	
	# get a generator for all the pages returned in sales history
	sales_history = bc.data_sources().find('Sales History').all()
	page = 1
	for x in sales_history:
		print('Page %s of Sales History: %s' % (page, x))
		page += 1
```




