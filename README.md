# python-csv-to-json-array
## Description
Converts *csv* files to *JSON Array* with Python. 

Give an input file like:

| order_id 	| item_name 	| id 	| price 	| source_price 	| purchase_method 	| quantity 	| status 	| hold_reason 	| assigned_pickup_source 	| pickup_agent_id 	|
|----------	|-----------	|----	|-------	|--------------	|-----------------	|----------	|--------	|-------------	|------------------------	|-----------------	|
|          	|           	|    	|       	|              	|                 	|          	|        	|             	|                        	|                 	|
|          	|           	|    	|       	|              	|                 	|          	|        	|             	|                        	|                 	|
|          	|           	|    	|       	|              	|                 	|          	|        	|             	|                        	|                 	|

e.g. :
```json
order_id,item_name,id,price,source_price,purchase_method,quantity,status,hold_reason,assigned_pickup_source,pickup_agent_id
10378,Remax RM-201 Wired Earphone,22245,280,256,Cash,7,Stock Confirmed,,Unilever Bangladesh Limited,27
10381,Real Fruit Power Apple Juice +1 FREE,22250,100,55,Cash,1,Stock Confirmed,,Unilever Bangladesh Limited,27
10381,Assassin’s Creed Rouge(Remastered) ,22249,55,35,Cash,1,Out Of Stock,,Game Shop,27
10382,Nioh,22251,100,73,Cash,1,Stock Confirmed,Stock Unavailable,Game Shop,27
10385,TP-LINK TL-WR841N,22262,100,73,Cash,1,Stock Confirmed,,TP - Link Shop,27
```

will generate:


```json
[
    {
        "order_id": "10378", 
        "items": [
            {
                "status": "Stock Confirmed", 
                "pickup_agent_id": "27", 
                "item_name": "Remax RM-201 Wired Earphone", 
                "price": "280", 
                "hold_reason": "", 
                "purchase_method": "Cash", 
                "assigned_pickup_source": "Unilever Bangladesh Limited", 
                "source_price": "256", 
                "id": "22245", 
                "quantity": "7"
            }
        ]
    }, 
    {
        "order_id": "10381", 
        "items": [
            {
                "status": "Stock Confirmed", 
                "pickup_agent_id": "27", 
                "item_name": "Real Fruit Power Apple Juice +1 FREE", 
                "price": "100", 
                "hold_reason": "", 
                "purchase_method": "Cash", 
                "assigned_pickup_source": "Unilever Bangladesh Limited", 
                "source_price": "55", 
                "id": "22250", 
                "quantity": "1"
            }, 
            {
                "status": "Out Of Stock", 
                "pickup_agent_id": "27", 
                "item_name": "Assassin\u2019s Creed Rouge(Remastered) ", 
                "price": "55", 
                "hold_reason": "", 
                "purchase_method": "Cash", 
                "assigned_pickup_source": "Game Shop", 
                "source_price": "35", 
                "id": "22249", 
                "quantity": "1"
            }
        ]
    }, 
    {
        "order_id": "10382", 
        "items": [
            {
                "status": "Stock Confirmed", 
                "pickup_agent_id": "27", 
                "item_name": "Nioh", 
                "price": "100", 
                "hold_reason": "Stock Unavailable", 
                "purchase_method": "Cash", 
                "assigned_pickup_source": "Game Shop", 
                "source_price": "73", 
                "id": "22251", 
                "quantity": "1"
            }
        ]
    }, 
    {
        "order_id": "10385", 
        "items": [
            {
                "status": "Stock Confirmed", 
                "pickup_agent_id": "27", 
                "item_name": "TP-LINK TL-WR841N", 
                "price": "100", 
                "hold_reason": "", 
                "purchase_method": "Cash", 
                "assigned_pickup_source": "TP - Link Shop", 
                "source_price": "73", 
                "id": "22262", 
                "quantity": "1"
            }
        ]
    }
]
```

## Prerequisites
**Python 2.7** 

### Usage
```py
# Add csv file and run it from terminal
> python script.py
