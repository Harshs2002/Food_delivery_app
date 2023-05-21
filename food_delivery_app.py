class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount

# Creating food items
food1 = FoodItem('1', 'Biryani', '1 plate', 'Rs.220', '5% discount')
food2 = FoodItem('2', 'Rumali Roti', '1 piece', 'Rs.20', '5% discount')
food3 = FoodItem('3', 'Chicken 65', '1 plate', 'Rs.260', '5% discount')
food4 = FoodItem('4', 'Thumbs Up', '750 ml', 'Rs.30', '5% discount')

print(food1.food_id, food1.name, food1.quantity, food1.price, food1.discount)
print(food2.food_id, food2.name, food2.quantity, food2.price, food2.discount)
print(food3.food_id, food3.name, food3.quantity, food3.price, food3.discount)


def check_stock(stock):
    if stock >= 50:
        return "Stock available"
    else:
        return "Stock unavailable"

stock_check = check_stock(60)
print(stock_check)

print("\nView list of all food items:")
food_items = ['Chicken Biryani', 'Chicken 65', 'Rumali Roti', 'Thumbs Up']
for i in food_items:
    print(i)

def remove_item_from_list(food_list):
    if food_list == ['Chicken Biryani', 'Chicken 65', 'Rumali Roti', 'Thumbs Up']:
        food_list.pop(0)

food_list = ['Chicken Biryani', 'Chicken 65', 'Rumali Roti', 'Thumbs Up']
print("\nRemoving item from the list:")
remove_item_from_list(food_list)
print(food_list)


class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

    def registration(self):
        return "Registration completed successfully"

    def login(self):
        return "User logged in to the application"

    def place_new_order(self):
        print("Placing a new order")

    def view_order_history(self):
        print("Viewing order history")

    def update_profile(self):
        print("Updating profile")

# Creating a user object
user = User('Akber', '799548533', 'mdakber@gmail', 'Hyderabad', 'pathan')

print(user.registration())
print(user.login())

print("\nUser Options:")
print("1. Place New Order")
print("2. Order History")
print("3. Update Profile")

user_choice = input("Enter your choice: ")

if user_choice == '1':
    user.place_new_order()
elif user_choice == '2':
    user.view_order_history()
elif user_choice == '3':
    user.update_profile()


class Restaurant:
    def __init__(self):
        self.food_items = [
            {'name': 'Tandoori Chicken', 'quantity': '4 pieces', 'price': 'INR 240'},
            {'name': 'Vegan Burger', 'quantity': '1 piece', 'price': 'INR 320'},
            {'name': 'Truffle Cake', 'quantity': '500g', 'price': 'INR 900'}
        ]
    def view_food_items(self):
        print("\nView list of all food items:")
        for index, food_item in enumerate(self.food_items, start=1):
            name = food_item['name']
            quantity = food_item['quantity']
            price = food_item['price']
            print(f"{index}. {name} ({quantity}) [{price}]")

restaurant = Restaurant()
restaurant.view_food_items()

class Order:
    def __init__(self):
        self.selected_items = []

    def place_order(self):
        print("\nPlacing order...")
        if len(self.selected_items) > 0:
            print("Selected items:")
            for item in self.selected_items:
                print(item)
            print("Order placed successfully!")
        else:
            print("No items selected. Please select items first.")

    def select_items(self):
        selected_indices = input("Enter the indices of the items to select (comma-separated): ")
        indices = [int(index.strip()) for index in selected_indices.split(',')]
        for index in indices:
            if index >= 1 and index <= len(restaurant.food_items):
                self.selected_items.append(restaurant.food_items[index - 1]['name'])

order = Order()

print("\nSelect food items:")
restaurant.view_food_items()
order.select_items()

print("\nSelected items:")
for item in order.selected_items:
    print(item)

order.place_order()

    
    
# OUTPUT
1 Biryani 1 plate Rs.220 5% discount
2 Rumali Roti 1 piece Rs.20 5% discount
3 Chicken 65 1 plate Rs.260 5% discount
Stock available

View list of all food items:
Chicken Biryani
Chicken 65
Rumali Roti
Thumbs Up

Removing item from the list:
['Chicken 65', 'Rumali Roti', 'Thumbs Up']
Registration completed successfully
User logged in to the application

User Options:
1. Place New Order
2. Order History
3. Update Profile
Enter your choice: 1
Placing a new order

View list of all food items:
1. Tandoori Chicken (4 pieces) [INR 240]
2. Vegan Burger (1 piece) [INR 320]
3. Truffle Cake (500g) [INR 900]

Select food items:

View list of all food items:
1. Tandoori Chicken (4 pieces) [INR 240]
2. Vegan Burger (1 piece) [INR 320]
3. Truffle Cake (500g) [INR 900]
Enter the indices of the items to select (comma-separated): 1,2

Selected items:
Tandoori Chicken
Vegan Burger

Placing order...
Selected items:
Tandoori Chicken
Vegan Burger
Order placed successfully!


