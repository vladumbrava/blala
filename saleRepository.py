from domain.sale import Sale

class SaleRepository:
    def __init__(self)
        self.__sales = []

    def get_sales(self):
        return self.__sales

    def set_sales(self, sales):
        self.__sales = sales

    def add_sale(self, sale):
        if not isinstance(sale, Sale):
            raise ValueError("error")
        self.__sales.append(sale)

    def get_sales_of_category(self, category):
        result = ""
        for sal in self.__sales:
            if sal.get_category() == category:
                result += f"{sal}\n"
        return result

    def get_season(self):
        spring = ""
        summer = ""
        fall = ""
        winter = ""
        for sal in self.__sales:
            if sal.get_month_of_sale() in [3,4,5]:
                spring += f"{sal}\n"
        for sal in self.__sales:
            if sal.get_month_of_sale() in [6,7,8]:
                summer += f"{sal}\n"
        for sal in self.__sales:
            if sal.get_month_of_sale() in [9,10,11]:
                fall += f"{sal}\n"
        for sal in self.__sales:
            if sal.get_month_of_sale() in [12,1,2]:
                winter += f"{sal}\n"

    def __str__(self):
        result = ""
        for sal in self.__sales:
            result += f"{sal}\n"
        return result