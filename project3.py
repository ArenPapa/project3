import os
import sqlite3
import time
import datetime
from datetime import datetime, timedelta
import bcrypt
from kivy.graphics import Color, Line, RoundedRectangle
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput  
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
import numpy as np

Window.maximize()

db_directory = "/Users/areneun/Desktop/project3"
database = os.path.join(db_directory, "project3.db")

failed_attempts = {}

def hash_password(password):
    
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def check_password(password, hashed_password):
    """Checks if the provided password matches the stored hash."""
    return bcrypt.checkpw(password.encode(), hashed_password)

def initialize_db():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            points INTEGER NOT NULL,
            last_transaction INTEGER NOT NULL
        )
    """)
    
    cursor.execute("PRAGMA table_info(users)")
    columns = [column[1] for column in cursor.fetchall()]
    if 'visit_count' not in columns:
        cursor.execute("ALTER TABLE users ADD COLUMN visit_count INTEGER DEFAULT 0")
    if 'last_visit' not in columns:
        cursor.execute("ALTER TABLE users ADD COLUMN last_visit DATE")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            order_details TEXT NOT NULL,
            total_price REAL NOT NULL,
            payment_method TEXT NOT NULL,
            status TEXT NOT NULL,
            table_number INTEGER NOT NULL,
            address TEXT NOT NULL DEFAULT ''
        )
    """)

    cursor.execute("PRAGMA table_info(orders)")
    columns = [column[1] for column in cursor.fetchall()]
    if 'table_number' not in columns:
        cursor.execute("ALTER TABLE orders ADD COLUMN table_number INTEGER NOT NULL DEFAULT 1")
    if 'address' not in columns:
        cursor.execute("ALTER TABLE orders ADD COLUMN address TEXT NOT NULL DEFAULT ''")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS drivers (
            driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            earnings REAL NOT NULL,
            rating REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu_items (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT UNIQUE NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            feedback TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notifications (
            notification_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            read INTEGER DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS delivery_orders (
            delivery_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            postal_code TEXT NOT NULL,
            home_or_work TEXT NOT NULL,
            name_in_bell TEXT
        )
    """)

    conn.commit()

    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cursor.fetchone():
        admin_hash = hash_password("adminpassword")
        cursor.execute("INSERT INTO users (username, password, role, points, last_transaction) VALUES (?, ?, ?, ?, ?)",
                       ("admin", admin_hash, "admin", 0, 0))
        conn.commit()

    conn.close()
    populate_menu()  # Populate the menu items after initializing the database


def sanitize_input(text):
    return "".join(c for c in text.strip() if c.isalnum() or c in "_-.")

def populate_menu():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM menu_items")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return
    
    menu_items = [
        ("Big-Eye Tuna Sushi", "Sushi", 8.99),
        ("Fatty Albacore Tuna", "Sushi", 9.99),
        ("Salmon", "Sushi", 7.99),
        ("Onion Salmon", "Sushi", 8.49),
        ("Broiled Fatty Salmon", "Sushi", 9.49),
        ("Broiled Salmon with Basil Sauce", "Sushi", 9.99),
        ("Seabream", "Sushi", 8.99),
        ("Flounder Fin", "Sushi", 9.49),
        ("Bonito Sushi", "Sushi", 8.99),
        ("Cured Fatty Mackerel Sushi", "Sushi", 8.49),
        ("Fatty Amberjack Sushi", "Sushi", 10.99),
        ("Boiled Shrimp", "Sushi", 7.99),
        ("Jumbo Shrimp", "Sushi", 10.49),
        ("Scallop", "Sushi", 9.99),
        ("Squid", "Sushi", 7.49),
        ("Cooked Conger Eel", "Sushi", 11.99),
        ("Japanese Egg Omelet", "Sushi", 6.99),
        ("Chopped Tuna", "Gunkan/Roll", 8.99),
        ("Tuna with Yam", "Gunkan/Roll", 8.99),
        ("Salmon & Salmon Roe Roll", "Gunkan/Roll", 10.99),
        ("Cod Roe with Mayo", "Gunkan/Roll", 7.99),
        ("Corn Mayo Salad", "Gunkan/Roll", 6.99),
        ("Tuna Mayo Salad", "Gunkan/Roll", 6.99),
        ("Crab Mayo Salad", "Gunkan/Roll", 7.99),
        ("Natto", "Gunkan/Roll", 6.49),
        ("Cucumber Roll", "Gunkan/Roll", 6.99),
        ("Kitsune Udon Noodles", "Side Dishes", 5.99),
        ("Deep Fried Red Squid", "Side Dishes", 6.99),
        ("Pumpkin Tempura", "Side Dishes", 5.49),
        ("French Fries", "Side Dishes", 4.99),
        ("Ice Cake Catalana Brulee", "Desserts", 5.99),
        ("Rich Chocolate Cake", "Desserts", 5.99),
        ("Warabi & Candied Sweet Potato", "Desserts", 5.49),
        ("Japanese Sweet Potato", "Desserts", 4.99),
        ("Classic Pudding", "Desserts", 4.99)
    ]
    
    for item in menu_items:
        cursor.execute("SELECT * FROM menu_items WHERE item_name = ?", (item[0],))
        if cursor.fetchone():
            cursor.execute("UPDATE menu_items SET category = ?, price = ? WHERE item_name = ?", (item[1], item[2], item[0]))
        else:
            cursor.execute("INSERT INTO menu_items (item_name, category, price) VALUES (?, ?, ?)", item)
    
    conn.commit()
    conn.close()




class BaseScreen(Screen):
    def show_popup(self, message):
        box = BoxLayout(orientation='vertical', spacing=10, padding=10)
        label = Label(text=message)
        close_button = Button(text="Close", size_hint=(1, 0.3))
        close_button.bind(on_press=lambda x: self.popup.dismiss())
        box.add_widget(label)
        box.add_widget(close_button)
        self.popup = Popup(title="Alert", content=box, size_hint=(0.6, 0.3), auto_dismiss=False)
        self.popup.open()

class SplashScreen(BaseScreen):
    def on_enter(self):
        Clock.schedule_once(lambda dt: setattr(self.manager, "current", "login"), 2)

class LoginScreen(BaseScreen):
    def login_user(self):
        username = sanitize_input(self.ids.username.text)
        password = self.ids.password.text

        if username in failed_attempts:
            attempts, lock_time = failed_attempts[username]
            if attempts >= 5:
                if time.time() - lock_time < 300:
                    self.show_popup("Too many failed attempts. Try again in 5 minutes.")
                    return
                else:
                    failed_attempts[username] = [0, time.time()]

        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT password, role FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user:
            stored_hash, role = user
            if check_password(password, stored_hash):
                if username in failed_attempts:
                    del failed_attempts[username]

                if role == "customer":
                    self.manager.current = "dine_or_delivery"
                    self.manager.get_screen('CustomerHomeScreen').username = username
                elif role == "delivery_guy":
                    self.manager.current = "delivery_home"
                    self.manager.get_screen('delivery_home').username = username
                elif role == "employee":
                    self.manager.current = "EmployeeHomeScreen"
                    self.manager.get_screen('EmployeeHomeScreen').username = username
                elif role == "admin":
                    self.manager.current = "AdminScreen"
                    self.manager.get_screen('AdminScreen').username = username
                return

        if username in failed_attempts:
            failed_attempts[username][0] += 1
        else:
            failed_attempts[username] = [1, time.time()]

        remaining_attempts = 5 - failed_attempts[username][0]
        if remaining_attempts > 0:
            self.show_popup(f"Invalid credentials. {remaining_attempts} attempts remaining.")
        else:
            self.show_popup("Too many failed attempts. Try again in 5 minutes.")




class RegisterScreen(BaseScreen):
    def register_user(self):
        username = sanitize_input(self.ids.reg_username.text)
        password = self.ids.reg_password.text
        confirm_password = self.ids.confirm_password.text
        role = self.ids.role_spinner.text.lower()

        print(f"Debug: Registering user '{username}' with role '{role}'")

        if password != confirm_password:
            self.show_popup("Passwords do not match")
            return

        if role not in ["customer", "delivery_guy"]:
            self.show_popup("Invalid role selection.")
            return

        hashed_password = hash_password(password)
        print(f"Debug: Hashed password for user '{username}'")

        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password, role, points, last_transaction) VALUES (?, ?, ?, ?, ?)",
                           (username, hashed_password, role, 0, 0))  # Provide a default value for last_transaction
            conn.commit()
            print(f"Debug: User '{username}' registered successfully")
            self.show_popup("User registered successfully!")
        except sqlite3.IntegrityError as e:
            print(f"Debug: IntegrityError - {e}")
            self.show_popup("Username already exists")
        finally:
            conn.close()

class AdminScreen(Screen):
    pass

class AddEmployeeScreen(Screen):
    def add_employee(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        confirm_password = self.ids.confirm_password_input.text

        if password != confirm_password:
            self.show_popup("Passwords do not match!")
            return

        hashed_password = hash_password(password)  # Hash the password

        points = 0  # Default value for points
        last_transaction = ""  # Default value for last_transaction

        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, role, points, last_transaction) VALUES (?, ?, ?, ?, ?)", 
                       (username, hashed_password, "employee", points, last_transaction))
        conn.commit()
        conn.close()
        self.show_popup("Employee added successfully!")
        self.clear_inputs()

    def show_popup(self, message):
        popup = Popup(title='Info',
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 400))
        popup.open()

    def clear_inputs(self):
        self.ids.username_input.text = ""
        self.ids.password_input.text = ""
        self.ids.confirm_password_input.text = ""

class AddItemScreen(Screen):
    def add_menu_item(self):
        item_name = self.ids.new_item_name.text
        category = self.ids.new_category.text
        price = self.ids.new_price.text

        if not item_name or not category or not price:
            self.show_popup("Please fill all fields!")
            return

        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO menu_items (item_name, category, price) VALUES (?, ?, ?)", (item_name, category, float(price)))
        conn.commit()
        conn.close()
        self.show_popup("Item added successfully!")
        self.clear_inputs()

    def show_popup(self, message):
        popup = Popup(title='Info',
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 400))
        popup.open()

    def clear_inputs(self):
        self.ids.new_item_name.text = ""
        self.ids.new_category.text = ""
        self.ids.new_price.text = ""

class RemoveItemScreen(Screen):
    def on_enter(self):
        self.load_menu_items()
        self.selected_item = None  # Initialize selected item

    def load_menu_items(self):
        self.ids.menu_grid.clear_widgets()
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT item_name, category, price FROM menu_items")
        menu_items = cursor.fetchall()
        conn.close()

        for item_name, category, price in menu_items:
            item_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            item_label = Label(text=f"{item_name} - {category} - ${price:.2f}", size_hint_x=0.8, color=(0, 0, 0, 1))  # Black text
            remove_button = Button(text="X", size_hint_x=0.2, background_color=(1, 0, 0, 1))  # Small red button
            remove_button.bind(on_press=lambda btn, item_name=item_name: self.select_item(item_name))
            item_layout.add_widget(item_label)
            item_layout.add_widget(remove_button)
            self.ids.menu_grid.add_widget(item_layout)
        self.ids.menu_grid.height = self.ids.menu_grid.minimum_height

    def select_item(self, item_name):
        self.selected_item = item_name
        self.ids.remove_item_label.text = f"Selected item to remove: {item_name}"
        self.ids.confirm_remove_btn.disabled = False  # Enable the confirm remove button

    def confirm_remove_action(self):
        if self.selected_item:
            self.remove_item(self.selected_item)

    def remove_item(self, item_name):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM menu_items WHERE item_name = ?", (item_name,))
        conn.commit()
        conn.close()
        self.show_popup("Item removed successfully!")
        self.selected_item = None  # Clear the selected item
        self.ids.remove_item_label.text = "Selected item to remove: None"
        self.ids.confirm_remove_btn.disabled = True  # Disable the confirm remove button
        self.load_menu_items()

    def show_popup(self, message):
        popup = Popup(title='Info',
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 400))
        popup.open()

class DineOrDeliveryScreen(BaseScreen):
    def choose_eat_in(self):
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        label = Label(text="Enter your table number:")
        table_number_input = TextInput(hint_text="Table Number", multiline=False)
        submit_button = Button(text="Submit", size_hint=(1, 0.3))
        content.add_widget(label)
        content.add_widget(table_number_input)
        content.add_widget(submit_button)
        popup = Popup(title="Table Number", content=content, size_hint=(0.6, 0.4), auto_dismiss=False)
        submit_button.bind(on_press=lambda x: self.submit_table_number(table_number_input.text, popup))
        popup.open()

    def submit_table_number(self, table_number, popup):
        if table_number.isdigit():
            self.manager.get_screen('CustomerHomeScreen').table_number = int(table_number)
            self.manager.get_screen('CustomerHomeScreen').dining_option = "Eat In"
            popup.dismiss()
            self.manager.current = 'CustomerHomeScreen'
        else:
            self.show_popup("Please enter a valid table number.")

    def choose_delivery(self):
        self.manager.current = 'delivery_address'

class DeliveryAddressScreen(BaseScreen):
    def submit_address(self):
        address = self.ids.address_input.text
        city = self.ids.city_input.text
        postal_code = self.ids.postal_code_input.text
        home_or_work = self.ids.home_or_work_input.text
        name_in_bell = self.ids.name_in_bell_input.text

        if address and city and postal_code and home_or_work:
            self.manager.get_screen('CustomerHomeScreen').address = address
            self.manager.get_screen('CustomerHomeScreen').city = city
            self.manager.get_screen('CustomerHomeScreen').postal_code = postal_code
            self.manager.get_screen('CustomerHomeScreen').home_or_work = home_or_work
            self.manager.get_screen('CustomerHomeScreen').name_in_bell = name_in_bell
            self.manager.get_screen('CustomerHomeScreen').dining_option = "Delivery"

            # Store delivery information in the database
            conn = sqlite3.connect(database)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO delivery_orders (username, address, city, postal_code, home_or_work, name_in_bell)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (self.manager.get_screen('CustomerHomeScreen').username, address, city, postal_code, home_or_work, name_in_bell))
            conn.commit()
            conn.close()

            self.manager.current = 'CustomerHomeScreen'
        else:
            self.show_popup("Please fill in all required fields.")


class CustomerHomeScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(CustomerHomeScreen, self).__init__(**kwargs)
        self.username = ''
        self.cart = {}
        self.cart_items = {}
        self.total_price = 0
        self.menu_items = []
        self.current_page = 0
        self.items_per_page = 10
        self.session_order_count = 0  # Track the number of orders in the session
        self.dining_option = None
        self.table_number = None
        self.address = None
        self.city = None
        self.postal_code = None
        self.home_or_work = None
        self.name_in_bell = None

    def on_enter(self):
        self.start_mining()
        self.load_menu_items()
        self.display_points()
        self.logged_in_time = datetime.utcnow()  # Track when the user logs in

    def start_mining(self):
        # Schedule the mining function to run every minute
        Clock.schedule_interval(self.mine_points, 60)

    def mine_points(self, dt):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT points, visit_count, last_visit FROM users WHERE username = ?", (self.username,))
        user = cursor.fetchone()
        if user:
            points, visit_count, last_visit = user
            current_time = datetime.utcnow()
            last_visit_time = datetime.strptime(last_visit, "%Y-%m-%d").date() if last_visit else None

            # Determine the engagement factor
            engagement_factor = 1 + self.session_order_count  # Increase factor based on session order count

            # Calculate points earned over time with engagement factor
            elapsed_time = current_time - self.logged_in_time
            points_to_add = int((elapsed_time.total_seconds() // 60) * engagement_factor)
            new_points = points + points_to_add

            # Update the user's points and last visit
            cursor.execute("UPDATE users SET points = ?, last_visit = ? WHERE username = ?", 
                           (new_points, current_time.date(), self.username))
            conn.commit()
            self.logged_in_time = current_time  # Update logged_in_time
            self.ids.points_label.text = f"Points: {new_points}"
        conn.close()

    def load_menu_items(self):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT item_name, category, price FROM menu_items")
        self.menu_items = cursor.fetchall()
        conn.close()
        self.display_menu("All")

    def display_menu(self, category):
        self.ids.menu_grid.clear_widgets()
        items_to_display = [item for item in self.menu_items if category == "All" or item[1] == category]
        start_index = self.current_page * self.items_per_page
        end_index = start_index + self.items_per_page
        for item in items_to_display[start_index:end_index]:
            item_name, item_category, price = item
            item_button = Button(
                text=f"{item_name}\n{item_category}\n${price}",
                size_hint_y=None,
                height=150,  # Increased height for spaciousness
                background_normal='',
                background_color=(0, 0, 0, 0),  # Transparent background
                color=(0, 0, 0, 1)  # Dark font
            )
            item_button.bind(on_press=lambda btn, item=item: self.add_to_cart(item))
            self.ids.menu_grid.add_widget(item_button)
            item_button.bind(size=self.update_canvas, pos=self.update_canvas)

    def update_canvas(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(0, 0, 0.5, 1)  # Navy blue border
            Line(width=1.5, rounded_rectangle=(instance.x, instance.y, instance.width, instance.height, 20))

    def display_points(self):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT points FROM users WHERE username = ?", (self.username,))
        user = cursor.fetchone()
        conn.close()

        if user:
            self.ids.points_label.text = f"Points: {user[0]}"

    def add_to_cart(self, item):
        if len(self.cart) < 4:
            item_name, item_category, price = item
            if item_name in self.cart:
                self.cart[item_name] += 1
            else:
                self.cart[item_name] = 1
                self.cart_items[item_name] = price
            self.total_price += price
            self.show_popup(f"Added {item_name} to cart\nTotal Price: ${self.total_price:.2f}")
        else:
            self.show_popup("You can only order 4 items per order.")

    def logout(self):
        self.manager.current = 'login'

    def view_cart(self):
        cart_content = ""
        for item_name, quantity in self.cart.items():
            cart_content += f"{item_name} x{quantity}\n"
        self.manager.get_screen('ViewCart').cart = self.cart
        self.manager.get_screen('ViewCart').cart_items = self.cart_items
        self.manager.get_screen('ViewCart').update_cart_details()
        self.manager.current = 'ViewCart'

    def pay(self):
        # Calculate total price
        total_price = sum(quantity * self.cart_items[item_name] for item_name, quantity in self.cart.items())

        # Check if the user has enough points to pay
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT points FROM users WHERE username = ?", (self.username,))
        user = cursor.fetchone()
        conn.close()

        if user:
            user_points = user[0]
            if user_points >= total_price:
                # Ask user if they want to pay with points
                self.show_payment_popup(total_price, user_points)
            else:
                # User does not have enough points, proceed with normal payment
                self.process_payment(total_price, points_earned=int(total_price // 10))
        else:
            self.show_popup("User not found.")

    def process_payment(self, total_price, points_earned=0, pay_with_points=False):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        if pay_with_points:
            cursor.execute("SELECT points FROM users WHERE username = ?", (self.username,))
            user_points = cursor.fetchone()[0]
            if user_points >= total_price:
                cursor.execute("UPDATE users SET points = points - ? WHERE username = ?", (total_price, self.username))
                self.show_popup("Payment successful! You paid with points.")
            else:
                self.show_popup("Insufficient points for payment.")
                if self.payment_popup:
                    self.payment_popup.dismiss()
                return
        else:
            points_earned = int(total_price // 10)  # Example algorithm: 1 point for every $10 spent
            self.update_points(points_earned)
            self.show_popup(f"Payment successful! You earned {points_earned} points.")

        # Save order to orders table with status 'Ongoing'
        order_details = ", ".join(f"{item_name} x{quantity}" for item_name, quantity in self.cart.items())
        cursor.execute("""
            INSERT INTO orders (username, order_details, total_price, payment_method, status, table_number, address)
            VALUES (?, ?, ?, ?, 'Ongoing', ?, ?)
        """, (self.username, order_details, total_price, "Points" if pay_with_points else "Card", self.table_number, self.address))

        conn.commit()
        conn.close()

        # Update session order count
        self.session_order_count += 1

        # Increase mining rate after each order
        self.mining_rate = max(5, 10 - (self.session_order_count // 1))  # Decrease the mining rate

        # Update points label
        self.update_points_label()

        # Close the payment popup if it exists
        if self.payment_popup:
            self.payment_popup.dismiss()

        # Clear cart and update cart details
        self.cart.clear()
        self.update_cart_details()

class ViewCart(BaseScreen):
    def __init__(self, **kwargs):
        super(ViewCart, self).__init__(**kwargs)
        self.cart = {}  # Format: {item_name: quantity}
        self.cart_items = {}  # Format: {item_name: price}
        self.payment_popup = None  # Initialize the payment_popup attribute
        self.logged_in_time = datetime.utcnow()  # Track when the user logs in
        self.points = 0  # Track user points
        self.session_order_count = 0  # Track the number of orders in the session
        self.mining_rate = 10  # Minutes per point, default to 1 point per 10 minutes

        Clock.schedule_interval(self.mine_points, 60)  # Mine points every minute

    def on_pre_enter(self):
        self.update_cart_details()
        self.update_points_from_db()  # Fetch and update points from the database

    def mine_points(self, dt):
        current_time = datetime.utcnow()
        elapsed_time = (current_time - self.logged_in_time).total_seconds() // 60  # Elapsed time in minutes

        # Calculate points earned based on the mining rate
        points_to_add = int(elapsed_time // self.mining_rate)
        if points_to_add > 0:
            self.points += points_to_add
            self.logged_in_time = current_time  # Reset the logged in time

            # Update user points in the database
            conn = sqlite3.connect(database)
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET points = points + ? WHERE username = ?", (points_to_add, self.manager.get_screen('CustomerHomeScreen').username))
            conn.commit()
            conn.close()

            self.update_points_label()

    def update_points_from_db(self):
        # Fetch points from the database and update points_label
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT points FROM users WHERE username = ?", (self.manager.get_screen('CustomerHomeScreen').username,))
        user = cursor.fetchone()
        conn.close()

        if user:
            self.points = user[0]
            self.update_points_label()

    def update_points_label(self):
        self.ids.points_label.text = f"Points: {self.points}"

    def update_cart_details(self):
        self.ids.cart_items.clear_widgets()
        total_price = 0
        for item_name, quantity in self.cart.items():
            item_price = self.cart_items[item_name]
            item_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            with item_layout.canvas.before:
                Color(0, 0, 0.5, 1)  # Navy blue border
                Line(width=1.5, rounded_rectangle=(0, 0, item_layout.width, item_layout.height, 20))
            item_label = Label(text=f"{item_name}", font_size="20sp", color=(0, 0, 0, 1), size_hint_x=0.4)
            price_label = Label(text=f"${item_price:.2f}", font_size="20sp", color=(0, 0, 0, 1), size_hint_x=0.2)
            quantity_label = Label(text=f"x{quantity}", font_size="20sp", color=(0, 0, 0, 1), size_hint_x=0.1)
            plus_button = Button(text="+", size_hint=(None, None), size=(30, 30), background_color=(0, 1, 0, 1))  # Green background, smaller size
            plus_button.bind(on_press=self.make_add_item_callback(item_name))
            minus_button = Button(text="-", size_hint=(None, None), size=(30, 30), background_color=(1, 0, 0, 1))  # Red background, smaller size
            minus_button.bind(on_press=self.make_remove_item_callback(item_name))
            item_layout.add_widget(item_label)
            item_layout.add_widget(price_label)
            item_layout.add_widget(quantity_label)
            item_layout.add_widget(plus_button)
            item_layout.add_widget(minus_button)
            self.ids.cart_items.add_widget(item_layout)
            total_price += quantity * item_price
        self.ids.cart_items.height = self.ids.cart_items.minimum_height
        self.ids.cart_total.text = f"Total: ${total_price:.2f}"
        self.update_points_label()  # Update points display

    def make_add_item_callback(self, item_name):
        return lambda instance: self.add_item(item_name)

    def make_remove_item_callback(self, item_name):
        return lambda instance: self.remove_item(item_name)

    def add_item(self, item_name):
        if len(self.cart) < 4:
            if item_name in self.cart:
                self.cart[item_name] += 1
            else:
                self.cart[item_name] = 1
                self.cart_items[item_name] = self.cart_items.get(item_name, 0)  # Fetch the item price
            self.update_cart_details()
        else:
            self.show_popup("You can only order 4 items per order.")

    def remove_item(self, item_name):
        if self.cart[item_name] > 0:
            self.cart[item_name] -= 1
            if self.cart[item_name] == 0:
                del self.cart[item_name]
                del self.cart_items[item_name]
        self.update_cart_details()

    def pay(self):
        # Calculate total price
        total_price = sum(quantity * self.cart_items[item_name] for item_name, quantity in self.cart.items())


        # Check if the user has enough points to pay
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT points FROM users WHERE username = ?", (self.manager.get_screen('CustomerHomeScreen').username,))
        user = cursor.fetchone()
        conn.close()

        if user:
            user_points = user[0]
            if user_points >= total_price:
                # Ask user if they want to pay with points
                self.show_payment_popup(total_price, user_points)
            else:
                # User does not have enough points, proceed with normal payment
                self.process_payment(total_price, points_earned=int(total_price // 10))
        else:
            self.show_popup("User not found.")

    def show_payment_popup(self, total_price, user_points):
        box = BoxLayout(orientation='vertical', spacing=10, padding=10)
        label = Label(text=f"Do you want to pay with {total_price} points?\nYou have {user_points} points.")
        points_button = Button(text="Pay with Points", size_hint=(1, 0.3))
        card_button = Button(text="Pay with Card", size_hint=(1, 0.3))

        if user_points >= total_price:
            points_button.bind(on_press=lambda x: self.process_payment(total_price, pay_with_points=True))
        else:
            points_button.disabled = True  # Disable the button if the user doesn't have enough points

        card_button.bind(on_press=lambda x: self.process_payment(total_price, points_earned=int(total_price // 10)))

        box.add_widget(label)
        box.add_widget(points_button)
        box.add_widget(card_button)

        self.payment_popup = Popup(title="Payment Option", content=box, size_hint=(0.6, 0.3), auto_dismiss=False)
        self.payment_popup.open()

    def process_payment(self, total_price, points_earned=0, pay_with_points=False):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        if pay_with_points:
            cursor.execute("SELECT points FROM users WHERE username = ?", (self.manager.get_screen('CustomerHomeScreen').username,))
            user_points = cursor.fetchone()[0]
            if user_points >= total_price:
                cursor.execute("UPDATE users SET points = points - ? WHERE username = ?", (total_price, self.manager.get_screen('CustomerHomeScreen').username))
                self.show_popup("Payment successful! You paid with points.")
            else:
                self.show_popup("Insufficient points for payment.")
                if self.payment_popup:
                    self.payment_popup.dismiss()
                return
        else:
            points_earned = int(total_price // 10)  # Example algorithm: 1 point for every $10 spent
            self.update_points(points_earned)
            self.show_popup(f"Payment successful! You earned {points_earned} points.")

        # Save order to orders table with status 'Ongoing'
        order_details = ", ".join(f"{item_name} x{quantity}" for item_name, quantity in self.cart.items())
        cursor.execute("""
            INSERT INTO orders (username, order_details, total_price, payment_method, status, table_number)
            VALUES (?, ?, ?, ?, 'Ongoing', ?)
        """, (self.manager.get_screen('CustomerHomeScreen').username, order_details, total_price, "Points" if pay_with_points else "Card", 1))  # Assuming table_number = 1 for simplicity

        conn.commit()
        conn.close()

        # Update session order count
        self.session_order_count += 1

        # Increase mining rate after each order
        self.mining_rate = max(5, 10 - (self.session_order_count // 1))  # Decrease the mining rate

        # Update points label
        self.update_points_label()

        # Close the payment popup if it exists
        if self.payment_popup:
            self.payment_popup.dismiss()

        # Clear cart and update cart details
        self.cart.clear()
        self.update_cart_details()

    def update_points(self, points_earned):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET points = points + ? WHERE username = ?", (points_earned, self.manager.get_screen('CustomerHomeScreen').username))
        conn.commit()
        conn.close()
        self.update_points_from_db()  # Refresh points after updating

    def show_popup(self, message):
        box = BoxLayout(orientation='vertical', spacing=10, padding=10)
        label = Label(text=message)
        close_button = Button(text="Close", size_hint=(1, 0.3))
        close_button.bind(on_press=lambda x: self.popup.dismiss())
        box.add_widget(label)
        box.add_widget(close_button)
        self.popup = Popup(title="Alert", content=box, size_hint=(0.6, 0.3), auto_dismiss=False)
        self.popup.open()



class DeliveryHomeScreen(BaseScreen):
    def on_enter(self):
        self.load_ready_orders()

    def load_ready_orders(self):
        self.ids.orders_grid.clear_widgets()
        
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT order_id, username, order_details, total_price, address FROM orders WHERE status = 'Ready for Delivery' AND address != ''")
        ready_orders = cursor.fetchall()
        conn.close()
        
        for order_id, username, order_details, total_price, address in ready_orders:
            order_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100)
            with order_layout.canvas.before:
                Color(0, 0, 0.5, 1)  # Navy blue border
                Line(width=1.5, rounded_rectangle=(order_layout.x, order_layout.y, order_layout.width, order_layout.height, 20))
            order_label = Label(text=f"Order {order_id} | {username} | {order_details} | ${total_price:.2f} | {address}", size_hint_x=0.8, color=(0, 0, 0, 1))
            complete_button = Button(text="Complete", size_hint_x=0.2, height=60, background_color=(0, 1, 0, 1))  # Bigger height
            complete_button.bind(on_press=lambda btn, order_id=order_id: self.complete_order(order_id))
            order_layout.add_widget(order_label)
            order_layout.add_widget(complete_button)
            self.ids.orders_grid.add_widget(order_layout)
            with complete_button.canvas.before:
                Color(0, 1, 0, 1)  # Green color
                RoundedRectangle(pos=complete_button.pos, size=complete_button.size, radius=[20,])
        self.ids.orders_grid.height = self.ids.orders_grid.minimum_height

    def complete_order(self, order_id):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("UPDATE orders SET status = 'Completed' WHERE order_id = ?", (order_id,))
        conn.commit()
        conn.close()
        self.load_ready_orders()  # Refresh the list of ready orders
        self.show_popup("Order marked as completed!")

    def show_popup(self, message):
        box = BoxLayout(orientation='vertical', spacing=10, padding=10)
        label = Label(text=message)
        close_button = Button(text="Close", size_hint=(1, 0.3))
        close_button.bind(on_press=lambda x: self.popup.dismiss())
        box.add_widget(label)
        box.add_widget(close_button)
        self.popup = Popup(title="Alert", content=box, size_hint=(0.6, 0.3), auto_dismiss=False)
        self.popup.open()

    def logout(self):
        self.manager.current = 'login'  # Switch to the login screen

class EmployeeHomeScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(EmployeeHomeScreen, self).__init__(**kwargs)
        self.shift_start_time = datetime.now()  
        self.shift_duration = timedelta(hours=8) 
    
    def on_enter(self):
        self.load_ongoing_orders()
        self.update_shift_timer()

    def load_ongoing_orders(self):
        self.ids.orders_grid.clear_widgets()
        
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT order_id, username, order_details, table_number FROM orders WHERE status = 'Ongoing'")
        ongoing_orders = cursor.fetchall()
        conn.close()
        
        for order_id, username, order_details, table_number in ongoing_orders:
            order_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100)
            with order_layout.canvas.before:
                Color(0, 0, 0.5, 1)  # Navy blue border
                Line(width=1.5, rounded_rectangle=(order_layout.x, order_layout.y, order_layout.width, order_layout.height, 20))
            order_label = Label(text=f"Order {order_id} | Table {table_number} | {username} | {order_details}", size_hint_x=0.8, color=(0, 0, 0, 1))
            ready_button = Button(text="Ready for Delivery", size_hint_x=0.2, height=60, background_color=(0, 1, 0, 1))  # Bigger height
            ready_button.bind(on_press=lambda btn, order_id=order_id: self.mark_ready_for_delivery(order_id))
            order_layout.add_widget(order_label)
            order_layout.add_widget(ready_button)
            self.ids.orders_grid.add_widget(order_layout)
            with ready_button.canvas.before:
                Color(0, 1, 0, 1)  # Green color
                RoundedRectangle(pos=ready_button.pos, size=ready_button.size, radius=[20,])
        self.ids.orders_grid.height = self.ids.orders_grid.minimum_height

    def mark_ready_for_delivery(self, order_id):
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("UPDATE orders SET status = 'Ready for Delivery' WHERE order_id = ?", (order_id,))
        conn.commit()
        conn.close()
        self.load_ongoing_orders()  # Refresh the list of ongoing orders
        self.show_popup("Order marked as ready for delivery!")

    def update_shift_timer(self):
        remaining_time = self.shift_start_time + self.shift_duration - datetime.now()
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.ids.shift_timer.text = f"Time left: {hours}h {minutes}m"
        
        # Schedule the timer update every minute
        Clock.schedule_once(lambda dt: self.update_shift_timer(), 60)

    def logout(self):
        self.manager.current = 'login'  # Switch to the login screen

    def show_popup(self, message):
        box = BoxLayout(orientation='vertical', spacing=10, padding=10)
        label = Label(text=message)
        close_button = Button(text="Close", size_hint=(1, 0.3))
        close_button.bind(on_press=lambda x: self.popup.dismiss())
        box.add_widget(label)
        box.add_widget(close_button)
        self.popup = Popup(title="Alert", content=box, size_hint=(0.6, 0.3), auto_dismiss=False)
        self.popup.open()

class OrderHistoryScreen(BaseScreen):
    def on_enter(self):
        self.load_order_history()

    def load_order_history(self):
        self.ids.order_history_grid.clear_widgets()
        
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT order_id, order_details, total_price, status FROM orders WHERE username = ?", (self.manager.get_screen('CustomerHomeScreen').username,))
        orders = cursor.fetchall()
        conn.close()
        
        for order_id, order_details, total_price, status in orders:
            order_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=80)
            with order_layout.canvas.before:
                Color(0, 0, 0.5, 1)  # Navy blue border
                Line(width=1.5, rounded_rectangle=(order_layout.x, order_layout.y, order_layout.width, order_layout.height, 20))
            order_label = Label(text=f"Order {order_id} | {order_details} | ${total_price:.2f} | {status}", size_hint_x=0.8, color=(0, 0, 0, 1))
            order_layout.add_widget(order_label)
            self.ids.order_history_grid.add_widget(order_layout)
        self.ids.order_history_grid.height = self.ids.order_history_grid.minimum_height

class FeedbackScreen(BaseScreen):
    def submit_feedback(self):
        feedback = self.ids.feedback_input.text
        if feedback:
            conn = sqlite3.connect(database)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO feedback (username, feedback) VALUES (?, ?)", (self.manager.get_screen('CustomerHomeScreen').username, feedback))
            conn.commit()
            conn.close()
            self.show_popup("Feedback submitted successfully!")
            self.ids.feedback_input.text = ""
        else:
            self.show_popup("Please enter your feedback.")

class NotificationScreen(BaseScreen):
    def on_enter(self):
        self.load_notifications()

    def load_notifications(self):
        self.ids.notification_grid.clear_widgets()
        
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM notifications WHERE username = ?", (self.manager.get_screen('CustomerHomeScreen').username,))
        notifications = cursor.fetchall()
        conn.close()
        
        for message in notifications:
            notification_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=80)
            with notification_layout.canvas.before:
                Color(0, 0, 0.5, 1)  # Navy blue border
                Line(width=1.5, rounded_rectangle=(notification_layout.x, notification_layout.y, notification_layout.width, notification_layout.height, 20))
            notification_label = Label(text=message[0], size_hint_x=0.8, color=(0, 0, 0, 1))
            notification_layout.add_widget(notification_label)
            self.ids.notification_grid.add_widget(notification_layout)
        self.ids.notification_grid.height = self.ids.notification_grid.minimum_height

sm = ScreenManager(transition=FadeTransition())
sm.add_widget(SplashScreen(name="splash"))
sm.add_widget(LoginScreen(name="login"))
sm.add_widget(RegisterScreen(name="register"))
sm.add_widget(AdminScreen(name='AdminScreen'))
sm.add_widget(AddEmployeeScreen(name='AddEmployeeScreen'))
sm.add_widget(AddItemScreen(name='AddItemScreen'))
sm.add_widget(RemoveItemScreen(name='RemoveItemScreen'))
sm.add_widget(DineOrDeliveryScreen(name="dine_or_delivery"))
sm.add_widget(DeliveryAddressScreen(name="delivery_address"))
sm.add_widget(CustomerHomeScreen(name="CustomerHomeScreen"))
sm.add_widget(ViewCart(name="ViewCart"))
sm.add_widget(DeliveryHomeScreen(name="delivery_home"))
sm.add_widget(EmployeeHomeScreen(name="EmployeeHomeScreen"))
sm.add_widget(OrderHistoryScreen(name="order_history"))
sm.add_widget(FeedbackScreen(name="feedback"))
sm.add_widget(NotificationScreen(name="notifications"))

class LoginApp(App):
    has_logo = False  # Logo property
    has_sushi_icon = False  # Sushi icon property
    has_custom_font = False  # Custom font property
    
    def __init__(self, **kwargs):
        super(LoginApp, self).__init__(**kwargs)
        # Logo path
        self.logo_path = 'path/to/your/logo.png'
        self.has_logo = os.path.exists(self.logo_path) if hasattr(self, 'logo_path') else False
        
        # Sushi icon path
        self.sushi_icon_path = 'path/to/your/sushi_icon.png'
        self.has_sushi_icon = os.path.exists(self.sushi_icon_path) if hasattr(self, 'sushi_icon_path') else False
        
        # Custom font path
        self.font_path = os.path.join('fonts', 'Roboto-Bold.ttf')
        self.has_custom_font = os.path.exists(self.font_path)
        
        # Create fonts directory if it doesn't exist
        if not os.path.exists('fonts'):
            os.makedirs('fonts')
    
    def build(self):
        initialize_db()
        return Builder.load_file("upgraded_project3.kv")
    
    def gradient_texture(self, color1, color2, direction='horizontal'):
        """Create a gradient texture between two colors."""
        size = (2, 512) if direction == 'horizontal' else (512, 2)
        texture = Texture.create(size=size, colorfmt='rgba')
        
        # Create the gradient array
        buf = np.zeros((size[1], size[0], 4), dtype=np.uint8)
        
        # Calculate the gradient
        for i in range(size[1]):
            for j in range(size[0]):
                t = i / (size[1] - 1) if direction == 'vertical' else j / (size[0] - 1)
                for k in range(4):  # RGBA channels
                    buf[i, j, k] = int((1 - t) * color1[k] * 255 + t * color2[k] * 255)
        
        # Update the texture with the gradient
        texture.blit_buffer(buf.tobytes(), colorfmt='rgba', bufferfmt='ubyte')
        
        return texture

if __name__ == "__main__":
    LoginApp().run()


