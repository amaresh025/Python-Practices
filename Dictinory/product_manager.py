orders = [ {"id": 1, "price": "100", "qty": "2"}, 
          {"id": 2, "price": "abc", "qty": "1"}, 
          {"id": 3, "price": "50", "qty": "x"}, 
          {"id": 4, "price": "200", "qty": "3"} ]

def product_manager(orders):
    invalid_orders = []
    valid_orders = []
    grand_total = 0

    for item in orders:
        try:
            price = int(item["price"])
            qty = int(item["qty"])
            total = price * qty

            valid_orders.append({
                "id": item["id"],
                "total": total
            })

            grand_total += total

        except ValueError:
            invalid_orders.append(item["id"])

    return {
        "valid_orders": valid_orders,
        "invalid_orders": invalid_orders,
        "grand_total": grand_total
    }
print(product_manager(orders))
