def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True :
        display_menu()
        choice = input("Enter the item to add:")
        if choice == '1':
            item = input('Which item are you adding? -> ')
            shopping = shopping_list.append(item) 
            return shopping_list
        elif choice == '2':
            item = input('Which item are you taking out? -> ')
            if item not in shopping_list:
                print(f"Sorry,but{item} is not in your shopping list")
                return shopping_list
            else: 
                shopping =shopping_list.remove(item)
                return shopping_list
        if choice == '3':
            shopping_list
            return shopping_list
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
              
               


cart = main()
print(cart)
