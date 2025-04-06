sales={} 
def record_sales(): #Entering records into dictionary
    product=input("Enter products: ")
    quantity=int(input("Enter quantity: "))
    sales[product]=quantity
    print("Recorded sales= ",sales)
    
def total_sales(product):
    print("\nTotal sales of a product") #Total sales of a product
    for key,value in sales.items():
        if key==product:
            print(f"{key}={value} units")
            
def sort_sales(): #Sales summary in descending order 
    print("\nSales summary (Top selling products) ")
    sorted_sales = sorted(sales.items(), key=lambda x: x[1], reverse=True)
    for product, quantity in sorted_sales:
        print(f"{product}: {quantity} units")
        
while True:
    c=int(input("\nEnter choice: "))
    if c==1:
        record_sales()
    elif c==2:
        product=input("Enter product name: ")
        total_sales(product)
    elif c==3:
        sort_sales()
    else:
        break
        print("Exit")
   


