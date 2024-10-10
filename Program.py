#1.Add product
#2.Update product
#3.Delete product
#4.Get product by PId
#5.Get all products
#6.Get products by category
#7.Get products between prices

class Product:
    def __init__(self, Pid, Pname,Pcategory, Pprice, Pquantity) -> None:
        self.Pid=Pid
        self.Pname=Pname
        self.Pcategory=Pcategory
        self.Pprice=Pprice
        self.Pquantity=Pquantity
    
    def __repr__(self):
        return f"Product(ID: {self.Pid}, Name: {self.Pname}, Category: {self.Pcategory}, Price: {self.Pprice}, Quantity: {self.Pquantity})"
        
class ProductOperations:
    def __init__(self) -> None:
        self.products=[]
        
    def addProducts(self, product):
        self.products.append(product)
        print(f"Product added: {product}")
        
    def updateProducts(self, Pid, Pname=None, Pcategory=None, Pprice=None, Pquantity=None):
        for product in self.products:
            if product.Pid == Pid:
                if Pname:
                    product.Pname=Pname 
                if Pcategory:
                    product.Pcategory=Pcategory
                if Pprice:
                    product.Pprice=Pprice
                if Pquantity:
                    product.Pquantity=Pquantity
                print(f"Product details updated: {product}")
                return
            print("Product Not Found")
    
    def deleteProducts(self,Pid):
        for product in self.products:
            if product.Pid==Pid:
                self.products.remove(product)
                print(f"Product deleted successfully!")
                return
            print("Product not found")
    
    def getProductsById(self,Pid):
        for product in self.products:
            if product.Pid==Pid:
                return product
            return "Product not found"
    
    def getAllProducts(self):
        return self.products if self.products else "No products available"
    
    def getProductsByCategory(self, Pcategory):
        filtered_products=[Product for product in self.products if product.Pcategory==Pcategory]
        return filtered_products if filtered_products else f"No products found in category: {Pcategory}"
    
    def getProductsBetweenPrice(self, low, high):
        filtered_products=[Product for product in self.products if low<=product.Pprice<=high]
        return filtered_products if filtered_products else f"No products found between price range {low} and {high}"
    
def display_menu():
    print("\nProduct Management System")
    print("1.Add Product")
    print("2.Update Product")
    print("3.Delete Product")
    print("4.Get Product By Id")
    print("5.Get All Products")
    print("6.Get Products by Category")
    print("7.Get Products Between the Price Range")
    print("8.Exit")
    
def main():
    productList=ProductOperations()
    
    while True:
        display_menu()
        choice=input("Select an option:")
        
        if choice == "1":
            Pid=int(input("Enter Product Id:"))
            Pname=input("Enter name of the product:")
            Pcategory=input("Enter category of the product:")
            Pprice=float(input("Enter product price:"))
            Pquantity=int(input("Enter quantity of the product:"))
            product= Product(Pid, Pname, Pcategory, Pprice, Pquantity)
            productList.addProducts(product)
            
        elif choice == "2":
            Pid=int(input("Enter Product Id to update:"))
            Pname=input("Enter new name of the product:") or None
            Pcategory=input("Enter category of the product:") or None
            Pprice=float(input("Enter product price:")) 
            Pprice=float(Pprice) if Pprice else None
            Pquantity=int(input("Enter quantity of the product")) 
            productList.updateProducts(Pid,Pname,Pcategory,Pprice,Pquantity)
        
        elif choice == "3":
            Pid=int(input("Enter the product id to delete:"))
            productList.deleteProducts(Pid)
        
        elif choice == "4":
            Pid=int(input("Enter Product Id:"))
            print(productList.getProductsById(Pid))
            
        elif choice == "5":
            products=productList.getAllProducts()
            print(products) 
            
        elif choice == "6":
            category=input("Enter category to filter by:")
            products=productList.getProductsByCategory(category)
            print(products)
            
        elif choice == "7":
            low=float(input("Enter lower price limit:"))
            high=float(input("Enter higher price limit:"))
            products=productList.getProductsBetweenPrice(low,high)
            print(products)
            
        elif choice == "8":
            print("Exiting the program")
            break 
        
        else:
            print("Invalid option. Please select a valid choice")
            
if __name__ == "__main__":
    main()
            
