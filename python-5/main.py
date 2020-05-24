from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

def classify_by_phone_number(records):
    for record in records:
        date_start = datetime.fromtimestamp(record['start'])
        date_end = datetime.fromtimestamp(record['end'])
        
        record['price'] = calculate_price_duration(date_start, date_end)
        
    new_records = create_new_records(records)
    new_records = sorted(new_records, key=lambda x: x['total'], reverse=True)
    
    return new_records

def create_new_records(records):
    # Map
    # records_map = list(map(lambda x: {
    #     'source': x['source'], 'total': x['price']
    # }, records))

    new_records = []
    
    for record in records:
        i = 0

        for new_record in new_records:
            if new_record['source'] == record['source']:
                i = 1
                total = new_record['total'] + record['price']
                new_record['total'] = round(total, 2)
                break
                
        if i == 0:
            new_records.append({
                'source': record['source'],
                'total': round(record['price'], 2)
                
            })

    return new_records


def calculate_price_duration(date_start, date_end):    
    duration = None
    price = None

    if (date_start.hour > 6 and date_start.hour < 22)  and (date_end.hour < 22
    and date_end.hour > 6):
        duration = date_end - date_start
        duration = int(duration.seconds / 60) # Transformando em minutos
        price = 0.36 + (duration * 0.09)

    elif (date_start.hour > 22 or date_start.hour < 6) and (date_end.hour < 24
    or date_end.hour < 6):
        duration = date_end - date_start
        price = 0.36 

    else:
        hours22 = datetime(date_start.year, date_start.month, date_start.day, 22, 0, 0, 0)
        if (date_start.hour >= 6 and date_start.hour <= 22 ) and ( date_end.hour > 22 
        and date_end.hour < 6):
            duration = date_start - hours22
            duration = int(duration.seconds / 60) # Transformando em minutos
            price = 0.36 + (duration * 0.09)
            
        else:
            duration = date_end - hours22
            duration = int(duration.seconds / 60) # Transformando em minutos
            price = 0.36 + (duration * 0.09)
            
    return price

final_records = classify_by_phone_number(records)
print(final_records)
# print(len(final_records))