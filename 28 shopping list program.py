#this program allows users to create a shopping list. 
# Functionlities : Add items, Remove items, View items


def add_item (shopping_list_param):
    item_input = input("Enter item you want to add:")
    shopping_list_param.append(item_input)
    print("Item added successfully")

def remove_item(shopping_list_param):
    item_input = input("Enter item you want to remove:")
    if item_input in shopping_list_param:
        shopping_list_param.remove(item_input)
        print("item removed successfullly")
    else:
        print("the item intended to remove , is not inside the list")
        
def view_list(shopping_list_param):
    print("\nlist of items:")                    
    for item in shopping_list_param:
        print(item)
        
print("welcome to shopping list creator")        
print("\nOptions:")
print("Enter 1 to add item to the list")
print("Enter 2 to remove item from the list")
print("Enter 3 to view all items in the list")
print("Enter 4 to exit the program")

shopping_list = []

while True:
    choice_input = int(input("\nEnter your choice:"))
    
    if choice_input == 1:
        add_item(shopping_list)
    elif choice_input ==2:
        add_item(shopping_list)
    elif choice_input == 3:
        add_item(shopping_list)
    elif choice_input == 4:
        print("Thank you for using the program") 
    break           