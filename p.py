transactions = [
    {"item": "Laptop", "category": "Electronics", "price": 1200.00, "quantity": 2},
    {"item": "Mouse", "category": "Electronics", "price": 45.00, "quantity": 5},
    {"item": "Notebook", "category": "Stationery", "price": 12.00, "quantity": 10},
    {"item": "Desk", "category": "Furniture", "price": 250.00, "quantity": 1},
    {"item": "Monitor", "category": "Electronics", "price": 300.00, "quantity": 3},
    {"item": "Pen", "category": "Stationery", "price": 3.00, "quantity": 50}
]

output = {}
electronics_price = 0
stationery_price = 0

for i in transactions:
    if i.get('category') not in output:
        output[i.get('category')] = {
            'total_revenue':i.get('price')*i.get('quantity'),
            'most_expensive':i.get('item')
        }
    else:
        if output.get(i.get('category')).get('total_revenue') > i.get('price')*i.get('quantity'):
            output[i.get('category')] = {
                'total_revenue':output.get(i.get('category')).get('total_revenue') + (i.get('price')*i.get('quantity')),
                'most_expensive': output.get(i.get('category')).get('most_expensive')
            }
        else:
            output[i.get('category')] = {
                'total_revenue':output.get(i.get('category')).get('total_revenue') + (i.get('price')*i.get('quantity')),
                'most_expensive': i.get('item')
            }
import json
with open('data,json','w',encoding='utf-8') as f:
    json.dump(output,f,indent=4) 