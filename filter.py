def check_product(title,price,product):

    title=title.lower()

    for keyword in product["required_keywords"]:
        if keyword.lower() not in title:
            return False

    for keyword in product["exclude_keywords"]:
        if keyword.lower() in title:
            return False

    if price < product["min_price"]:
        return False

    if price > product["max_price"]:
        return False

    return True