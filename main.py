from domain.sale import Sale
from infrastructure.saleRepository import SaleRepository

def main():
    salerepo = SaleRepository()
    sale1 = Sale("Pizza", "bakery", 35, 1)
    sale2 = Sale("Fanta", "drinks", 10, 7)
    sale3 = Sale("Carrot-Cake", "sweets", 25, 8)
    sale4 = Sale("Bread", "bakery", 5, 9)
    sale5 = Sale("Water", "drinks", 3, 12)
    sale6 = Sale("Ciabatta", "bakery", 20, 6)
    sales = [sale1, sale2, sale3, sale4, sale5, sale6]
    salerepo.set_sales(sales)

    while True:
        print("\nMenu")
        print("1. Print sales")
        print("2. Add sale")
        print("3. Get sales from category")
        print("4. Get seasons")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print(salerepo)

        if choice == 2:
            try:
                product_name = input("pn = ")
                category = input("cat= ")
                value = int(input("val= "))
                month_of_sale = int(input("mon= "))
                sale = Sale(product_name,category,value,month_of_sale)
                salerepo.add_sale(sale)
            except ValueError as e:
                print(e)

        if choice == 3:
            category = input("cat= ")
            print(salerepo.get_sales_of_category(category))

if __name__ == "__main__":
    main()