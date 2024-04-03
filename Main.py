def Calculate_ticket_price(age, height, price):
    if age < 16 or age > 80 or height < 100 or height > 200 or price <= 0 or price > 1000000:
        return -1
    if age < 24 or age > 65:
        if height <= 140:
            price = price * 0.7
        else:
            price = price * 0.8
    else:
        if height <= 140:
            price = price * 0.85
        else:
            price = price
    return price


