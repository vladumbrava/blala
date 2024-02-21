class Sale:
    def __init__(self, product_name, category, value, month_of_sale):
        if not isinstance(product_name, str):
            raise ValueError("error")
        if not isinstance(category, str):
            raise ValueError("error")
        if category not in ["sweets", "drinks", "diary", "bakery"]:
            raise ValueError("error")
        if not isinstance(value, int):
            raise ValueError("error")
        if not isinstance(month_of_sale, int):
            raise ValueError("error")
        if month_of_sale < 1:
            raise ValueError("error")
        if month_of_sale > 12:
            raise ValueError("error")
        self.__product_name = product_name
        self.__category = category
        self.__value = value
        self.__month_of_sale = month_of_sale

    def get_product_name(self):
        return self.__product_name

    def set_product_name(self, product_name):
        if not isinstance(product_name, str):
            raise ValueError("error")
        self.__product_name = product_name

    def get_category(self):
        return self.__category

    def set_category(self, category):
        if not isinstance(category, str):
            raise ValueError("error")
        if category not in ["sweets", "drinks", "diary", "bakery"]:
            raise ValueError("error")
        self.__category = category

    def get_value(self):
        return self.__value

    def set_value(self, value):
        if not isinstance(value, int):
            raise ValueError("error")
        self.__value = value

    def get_month_of_sale(self):
        return self.__month_of_sale

    def set_month_of_sale(self, month_of_sale):
        if not isinstance(month_of_sale, int):
            raise ValueError("error")
        if month_of_sale < 1:
            raise ValueError("error")
        if month_of_sale > 12:
            raise ValueError("error")
        self.__month_of_sale = month_of_sale

    def __str__(self):
        return f"{self.__product_name}, {self.__category}, {self.__value}, {self.__month_of_sale}"
