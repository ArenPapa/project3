![Pixel Art Kitchen GIF - Pixel Art Kitchen Cafe - Discover   Share GIFs](https://github.com/user-attachments/assets/74afb5a2-73d5-4ae9-bef4-b8ab650b91f8)


# Unit 3: A restaurant manager application

## Criteria A: Planning

## Problem definition

``` I propose developing a cutting-edge digital platform to transform operations at my bustling sushi restaurant by replacing traditional waitstaff with a seamless, app-based ordering system. This innovative solution will allow customers to place dine-in and delivery orders directly from their mobile devices, supporting various payment methods, including credit cards and mobile payments. A unique loyalty program will introduce a restaurant-specific currency, rewarding customers based on past orders and allowing them to redeem points for discounts or exclusive menu items.Additionally, the platform will feature a dedicated section for delivery drivers, enabling them to sign up, accept nearby orders, and track their earnings in real time. A built-in rating system will maintain service quality, while an instant payout feature will help attract and retain delivery partners. Restaurant staff will also benefit from the platform, as they will be able to monitor their remaining shift time and mark orders as completed, ensuring efficient service and streamlined workflow. ```

## Proposed Solution
To meet the client’s requirements, an optimal solution involves developing a digital platform using Python and Kivy to handle both customer interactions and restaurant management. This platform will replace traditional waitstaff with an intuitive mobile ordering system, allowing customers to place dine-in and delivery orders directly from their devices. Additionally, it will include features such as a loyalty program, a driver management system, and staff shift tracking.

For data storage and management, SQLite will be used as the primary database solution. SQLite is a lightweight, serverless database engine that integrates seamlessly with Python, making it an excellent choice for this application. Unlike heavier database management systems such as MySQL or PostgreSQL, SQLite requires no dedicated server, reducing deployment complexity and maintenance costs. Given that this platform is intended for a single restaurant rather than a large-scale enterprise with high concurrent transactions, SQLite provides the right balance between efficiency and simplicity. Additionally, its ability to store data locally ensures fast read/write speeds, making it ideal for tracking orders, managing loyalty points, and storing shift schedules without significant overhead.

Given the need for cross-platform compatibility, a visually rich user interface, and efficient real-time updates, Python and Kivy are the most suitable choices for development. Python’s open-source nature, extensive library support, and platform independence make it ideal for long-term scalability and future enhancements. Kivy, a Python framework designed for multi-touch applications, provides a highly flexible UI that runs seamlessly on both mobile and desktop devices without requiring separate codebases. Compared to alternatives like Java or Swift, Kivy allows for rapid development with fewer lines of code, making it more efficient for a small development team.

Additionally, Kivy’s built-in event-driven architecture simplifies user interactions, ensuring a smooth ordering experience. Its GPU-accelerated rendering engine enhances performance, allowing for fluid animations and real-time updates, crucial for tracking order status and shift times. Unlike web-based alternatives that rely heavily on internet connectivity, a Kivy-based application can function locally with offline capabilities, reducing dependency on external servers and improving reliability.

By leveraging Python, Kivy, and SQLite, this solution ensures a cost-effective, scalable, and user-friendly application that optimizes restaurant operations, enhances customer satisfaction, and improves delivery logistics.

## Success Criteria

1. **The solution provides a secure and efficient user authentication system for customers, employees, and delivery drivers.**  
   **[Issue Tackled]**: Prevents unauthorized access and ensures that each user has appropriate access to platform functionalities.  

2. **The platform allows customers to place dine-in and delivery orders through a user-friendly interface.**  
   **[Issue Tackled]**: Eliminates reliance on traditional waitstaff, reducing human error and improving ordering efficiency.  

3. **Multiple payment methods, including card payments and a points-based loyalty system, are supported.**  
   **[Issue Tackled]**: Provides flexibility in payment options, enhancing customer convenience and engagement.  

4. **A loyalty program is implemented, where customers earn points based on past orders and can redeem them for discounts or exclusive menu items.**  
   **[Issue Tackled]**: Encourages repeat customers and increases brand loyalty.  

5. **The system includes an order-tracking feature, allowing customers to view their order status in real time.**  
   **[Issue Tackled]**: Enhances transparency and reduces customer inquiries about order progress.  

6. **Delivery drivers can register, accept nearby orders, and track their earnings through a dedicated interface.**  
   **[Issue Tackled]**: Improves efficiency and ensures that deliveries are completed in a timely manner.  

7. **A rating system is included to allow customers to provide feedback on orders and delivery experiences.**  
   **[Issue Tackled]**: Helps maintain high service quality by identifying areas for improvement.  

8. **Restaurant employees can track their remaining shift time and mark orders as completed.**  
   **[Issue Tackled]**: Enhances workflow efficiency and ensures accurate order fulfillment.  

9. **Orders and customer data are securely stored and managed using an SQLite database.**  
   **[Issue Tackled]**: Provides a lightweight, serverless storage solution that is easy to maintain and efficient for restaurant operations.  

10. **The platform includes an admin dashboard where managers can monitor orders, employees, and delivery performance.**  
   **[Issue Tackled]**: Allows for better oversight and decision-making to optimize restaurant operations.  

11. **A menu management system is available, enabling administrators to add, update, or remove menu items.**  
   **[Issue Tackled]**: Provides flexibility in menu updates, ensuring accurate pricing and availability.  

12. **The application is built using Python and Kivy, ensuring cross-platform compatibility for mobile and desktop devices.**  
   **[Issue Tackled]**: Reduces development overhead and allows for a single codebase across different platforms.  

13. **The system includes offline functionality for essential features, such as order tracking and staff shift monitoring.**  
   **[Issue Tackled]**: Ensures continued usability even in cases of internet disruptions.  

14. **A notification system is implemented to send real-time updates about order status, promotions, and loyalty rewards.**  
   **[Issue Tackled]**: Keeps customers and staff informed about important updates.  

15. **A reporting feature generates summaries of order trends, peak business hours, and customer preferences.**  
   **[Issue Tackled]**: Provides valuable insights for restaurant management to optimize service and marketing strategies.  

16. **The system includes a feedback collection feature for customers to provide suggestions and complaints.**  
   **[Issue Tackled]**: Enables continuous improvement by gathering direct input from users.  

17. **A security mechanism is in place to prevent multiple failed login attempts and unauthorized access.**  
   **[Issue Tackled]**: Protects user data and maintains system integrity.  

18. **The final project documentation includes an overview of the features, implementation details, and impact assessment.**  
   **[Issue Tackled]**: Ensures maintainability and provides a reference for future enhancements.  


### **TOK Connection: Ethics of Data Collection and Privacy in Digital Platforms**  

Your digital restaurant platform collects and stores various forms of user data, including personal login credentials, order history, loyalty points, and delivery driver performance metrics. This raises significant ethical concerns about privacy, security, and consent, which are central issues in both the **Human Sciences** and **Technology** as Areas of Knowledge. The ethical dilemma revolves around **how much control users should have over their own data and to what extent businesses should be allowed to collect and use that data for operational efficiency.**  

One of the primary concerns is the issue of **informed consent in data collection**. Users interact with digital systems daily, often without fully understanding how their data is being stored and processed. Your platform, like many modern applications, automatically tracks customer behavior, order frequency, and staff work hours. However, if the platform does not provide clear policies or explicit user consent agreements, it becomes ethically questionable whether users are truly aware of how their data is being used. This reflects a broader **epistemological question**: *To what extent does a lack of transparency in data collection affect ethical responsibility in digital platforms?* Many users do not read privacy policies before signing up for services, which raises the question of whether businesses should take extra steps to ensure their customers fully understand the implications of using the platform.  

Another key ethical dilemma is the **trade-off between security and convenience** in digital platforms. Your system encrypts passwords using bcrypt, which adds a layer of security, but it does not incorporate more advanced protection mechanisms, such as two-factor authentication. This presents a conflict between making security strict enough to protect user data and keeping it simple enough for customers and employees to log in quickly. A system that prioritizes convenience over security may lead to vulnerabilities, making it easier for hackers to exploit user data. On the other hand, if security measures are too complex, they may discourage users from engaging with the platform. This dilemma raises the question: *How do we determine the ethical responsibility of protecting user data in digital systems?* Should businesses prioritize their own efficiency, or do they have a duty to implement security protocols that go beyond basic encryption?  

Beyond security, your platform also tracks user interactions to enhance business operations, such as monitoring customer visits for the loyalty program and tracking driver performance through ratings and earnings. While this data can help optimize service quality, it raises concerns about **digital surveillance and behavioral tracking**. If a delivery driver receives a few poor ratings, their ability to receive future orders could be affected, creating a system where algorithms, rather than human judgment, determine economic opportunities. Similarly, customers may receive targeted promotions based on their past spending habits, raising the question of whether businesses are subtly influencing consumer behavior in ways that limit their autonomy. This brings up an essential ethical issue: *At what point does data collection become digital surveillance, and how does this impact human freedom?* While tracking data is beneficial for business, excessive monitoring could create an environment where users are unknowingly manipulated by algorithms, much like the concerns raised with tech giants such as Amazon, Uber, or Google.  

Ultimately, your project highlights a broader debate about **data ethics, digital privacy, and the power dynamics between businesses and consumers**. In the age of information, knowledge is often collected through invisible processes, leaving users with little awareness of how their personal information is being used. This leads to larger epistemological questions: *Can a system truly "know" a customer’s preferences just by tracking their purchases? How much control should individuals have over their own digital footprint?* By examining the ethical implications of your platform, you engage with fundamental **TOK concepts related to the nature of knowledge, ethics in technology, and the limits of digital surveillance in modern society**.

# Criteria B: Design

## System Diagram

![Untitled presentation (1)](https://github.com/user-attachments/assets/ea85e1ea-e5ba-42df-af85-15c82b7740cc)


**Fig.1** System diagram for the proposed Digital Restaurant Platform, designed to streamline order management, payment processing, and delivery coordination. Customers interact with the platform via a user-friendly interface, placing dine-in and delivery orders. The system securely stores user data and order history using an SQLite database. A Raspberry Pi server hosts the application, facilitating real-time communication between customers, employees, and delivery drivers. The platform implements an API to manage authentication, order tracking, and loyalty rewards, ensuring seamless integration across all user roles.

## Wireframe

![Untitled design](https://github.com/user-attachments/assets/ffa97312-cd5b-47f1-9ed7-97d72c561f5f)

## flowchart

![image](https://github.com/user-attachments/assets/56c9e0ca-addd-464a-be32-5c587e3057ea)

## UML diagram of Proposed Solution

![image](https://github.com/user-attachments/assets/1d019c96-68c5-4bbf-a06f-14ec032c1036)

## ER diagram of database

![image](https://github.com/user-attachments/assets/bd19f5a9-66b6-4ad6-a07b-ec0270749b8c)

## flow diagram login function

![image](https://github.com/user-attachments/assets/1ea0871b-0db6-4e97-9c5a-8813e6ca100e)

## flow diagram Register function 

![image](https://github.com/user-attachments/assets/dddb5425-db92-40c2-bb6b-e8b702c921cb)

## flow diagram Update points function

![image](https://github.com/user-attachments/assets/75f03f3e-111d-4b99-8ae1-0c798cb8f362)


## Record of Tasks

| **Task Number** | **Task Description**                                           | **Start Date** | **End Date**   | **Status**     | **Comments/Notes**                           |
|-----------------|---------------------------------------------------------------|----------------|----------------|----------------|----------------------------------------------|
| 1               | Define the user roles and authentication requirements.         | Feb 10, 2025   | Feb 11, 2025    | Completed      | Set up user roles (customer, employee, driver) and security requirements. |
| 2               | Implement secure authentication system for all user roles.     | Feb 12, 2025   | Feb 14, 2025    | Completed      | Integrated login system with password hashing and role-based access. |
| 3               | Design the user interface for customer ordering (dine-in & delivery). | Feb 15, 2025   | Feb 17, 2025    | Completed      | Used Kivy to design a responsive UI for placing orders. |
| 4               | Integrate multiple payment methods (card and loyalty points).  | Feb 18, 2025   | Feb 21, 2025    | Completed      | Set up payment gateways and implemented points system. |
| 5               | Develop loyalty program (earning points & redeeming rewards).  | Feb 22, 2025   | Feb 24, 2025    | Completed      | Created system for customers to earn and redeem points. |
| 6               | Implement order tracking system for customers.                 | Feb 25, 2025   | Feb 26, 2025    | Completed      | Real-time order tracking developed and integrated. |
| 7               | Design and implement a driver interface for order acceptance and earnings tracking. | Feb 27, 2025   | Mar 1, 2025     | Completed      | Developed driver dashboard with order management and earnings tracker. |
| 8               | Add rating system for customers to give feedback.              | Mar 2, 2025    | Mar 3, 2025     | Completed      | Enabled customer feedback system for orders and delivery. |
| 9               | Implement employee shift tracking and order completion marking. | Mar 4, 2025    | Mar 5, 2025     | Completed      | Employees can track shifts and mark orders as completed. |
| 10              | Set up SQLite database for secure storage of order and customer data. | Mar 6, 2025    | Mar 7, 2025     | Completed      | SQLite database configured for data management. |
| 11              | Create admin dashboard for monitoring orders, employees, and delivery performance. | Mar 7, 2025    | Mar 8, 2025     | Completed      | Admin dashboard allows real-time monitoring and management. |
| 12              | Develop menu management system for administrators.             | Mar 8, 2025    | Mar 9, 2025     | Completed      | Menu items can be added, updated, or removed easily. |
| 13              | Implement offline functionality for critical features.        | Mar 9, 2025    | Mar 9, 2025     | Completed      | Offline mode ensures continued functionality during internet downtime. |
| 14              | Set up notification system for order updates, promotions, and rewards. | Mar 9, 2025    | Mar 9, 2025     | Completed      | Notifications for order status, loyalty rewards, and promotions. |
| 15              | Implement reporting features for order trends and customer insights. | Mar 9, 2025    | Mar 9, 2025     | Completed      | Reports generated on peak times, trends, and preferences. |
| 16              | Integrate feedback collection system for customers.            | Mar 9, 2025    | Mar 9, 2025     | Completed      | Enabled feedback collection for continuous improvement. |
| 17              | Implement security measures for login attempts and user data protection. | Mar 9, 2025    | Mar 9, 2025     | Completed      | Security protocols in place for multiple failed login attempts. |
| 18              | Finalize project documentation and impact assessment.         | Mar 9, 2025    | Mar 9, 2025     | Completed      | Documentation created, covering features, impact, and future improvements. |

## Test Plan

| **Test Number** | **Test Scenario**                                              | **Expected Outcome**                                      | **Actual Outcome** | **Status (Pass/Fail)** | **Comments/Notes** |
|---------------|----------------------------------------------------------------|--------------------------------------------------|----------------|-----------------|----------------|
| 1             | Register as a customer                                        | Customer account is successfully created.       |                |                 |                |
| 2             | Register as a driver                                          | Driver account is successfully created.         |                |                 |                |
| 3             | Log in as a customer                                          | Customer can log in with valid credentials.     |                |                 |                |
| 4             | Make a dine-in order                                          | Order is placed successfully.                   |                |                 |                |
| 5             | Make a delivery order                                         | Delivery order is placed successfully.          |                |                 |                |
| 6             | Try to pay with points                                        | Points are deducted correctly, and order is completed. |                |                 |                |
| 7             | Wait for loyalty points to refresh                            | Points increase based on time spent.            |                |                 |                |
| 8             | Make more orders to see if point frequency increases          | Points are awarded at an increasing rate.       |                |                 |                |
| 9             | Give feedback to the restaurant                              | Feedback is submitted and stored.               |                |                 |                |
| 10            | Log out as customer                                          | User is logged out successfully.                |                |                 |                |
| 11            | Log in as admin (Username: admin, Password: adminpassword)    | Admin successfully logs in.                     |                |                 |                |
| 12            | Try to add things to the menu                                | New items appear on the menu.                   |                |                 |                |
| 13            | Try to remove things from the menu                           | Selected menu items are removed.                |                |                 |                |
| 14            | Assign new employees                                         | Employees are added successfully.               |                |                 |                |
| 15            | Look at customer feedback                                   | Feedback is visible in the admin dashboard.     |                |                 |                |
| 16            | Log out as admin                                            | Admin logs out successfully.                    |                |                 |                |
| 17            | Log in as an employee                                       | Employee successfully logs in.                  |                |                 |                |
| 18            | Check if shift timer works properly                         | Timer runs correctly, tracking work duration.   |                |                 |                |
| 19            | Try to mark orders as complete                             | Orders are updated to "Completed" status.      |                |                 |                |
| 20            | Log out as employee                                        | Employee logs out successfully.                 |                |                 |                |
| 21            | Log in as a driver                                         | Driver successfully logs in.                    |                |                 |                |
| 22            | Try to accept orders                                       | Driver can see and accept available orders.    |                |                 |                |
| 23            | Look at payment and earnings wallet                        | Driver earnings are displayed correctly.        |                |                 |                |
| 24            | Mark orders as delivered                                   | Order status updates to "Delivered."           |                |                 |                |
| 25            | Log out as driver                                          | Driver logs out successfully.                   |                |                 |                |




# Criteria C: Development (around 1000 word max)

## List of techniques used

1. API communication with remote server
2. Filtering using moving average
3. 

---

### **1 Login Process**
### **Code:**
```python
def login_user(self):
    username = sanitize_input(self.ids.username.text)  # Prevent SQL injection
    password = self.ids.password.text  # Get password input

    # Check if the user is temporarily locked out
    if username in failed_attempts:
        attempts, lock_time = failed_attempts[username]
        if attempts >= 5:
            if time.time() - lock_time < 300:  # 5 minutes lockout
                self.show_popup("Too many failed attempts. Try again in 5 minutes.")
                return
            else:
                failed_attempts[username] = [0, time.time()]  # Reset lockout timer

    # Connect to database and fetch stored password hash
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT password, role FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    # If user exists and password is correct
    if user:
        stored_hash, role = user
        if check_password(password, stored_hash):
            if username in failed_attempts:
                del failed_attempts[username]  # Reset failed attempts

            # Redirect user based on role
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

    # Handle incorrect credentials
    if username in failed_attempts:
        failed_attempts[username][0] += 1
    else:
        failed_attempts[username] = [1, time.time()]

    remaining_attempts = 5 - failed_attempts[username][0]
    if remaining_attempts > 0:
        self.show_popup(f"Invalid credentials. {remaining_attempts} attempts remaining.")
    else:
        self.show_popup("Too many failed attempts. Try again in 5 minutes.")
```
### **Detailed Explanation:**
## Detailed Analysis of `login_user` Method

```python
def login_user(self):
    username = sanitize_input(self.ids.username.text)  # Prevent SQL injection
    password = self.ids.password.text  # Get password input
```

**Lines 1-3: Method Declaration and Input Collection**
- This is a method of a class (indicated by the `self` parameter)
- Line 2 calls a function named `sanitize_input()` on the username input:
  - `self.ids.username.text` retrieves the text value from a UI element with ID "username"
  - The sanitization function likely removes/escapes special characters to prevent SQL injection attacks
  - The sanitized username is stored in the variable `username`
- Line 3 retrieves the password input directly from a UI element with ID "password"
  - Note that the password is not sanitized since it will be hashed, not directly inserted into SQL

```python
    # Check if the user is temporarily locked out
    if username in failed_attempts:
        attempts, lock_time = failed_attempts[username]
        if attempts >= 5:
            if time.time() - lock_time < 300:  # 5 minutes lockout
                self.show_popup("Too many failed attempts. Try again in 5 minutes.")
                return
            else:
                failed_attempts[username] = [0, time.time()]  # Reset lockout timer
```

**Lines 4-12: Account Lockout Mechanism**
- Line 5 checks if the username exists in a dictionary called `failed_attempts`
- Line 6 unpacks the value stored for this username, which is a list containing:
  - `attempts`: The number of failed login attempts
  - `lock_time`: The timestamp when counting started
- Line 7 checks if the user has reached or exceeded 5 failed attempts
- Line 8 calculates the time difference between now and when the lockout started:
  - `time.time()` returns the current time in seconds since the epoch
  - If less than 300 seconds (5 minutes) have passed, the account is still locked
- Lines 9-10 show an error message and exit the function with `return` if the account is locked
- Lines 11-12 reset the failed attempts counter if the lockout period has passed:
  - Sets attempts back to 0
  - Updates the timestamp to the current time

```python
    # Connect to database and fetch stored password hash
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT password, role FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
```

**Lines 13-18: Database Connection and Query**
- Line 14 establishes a connection to an SQLite database:
  - `database` is a variable containing the database path/name
- Line 15 creates a cursor object for executing SQL commands
- Line 16 executes a parameterized SQL query:
  - The `?` is a placeholder that gets replaced with the value in the tuple `(username,)`
  - This is a security best practice that prevents SQL injection
  - The query selects the password hash and role for the specified username
- Line 17 fetches the first matching record (or None if no match is found)
- Line 18 closes the database connection to free up resources

```python
    # If user exists and password is correct
    if user:
        stored_hash, role = user
        if check_password(password, stored_hash):
            if username in failed_attempts:
                del failed_attempts[username]  # Reset failed attempts
```

**Lines 19-24: User Verification**
- Line 20 checks if `user` contains data (i.e., if a matching username was found)
- Line 21 unpacks the database result into variables:
  - `stored_hash`: The bcrypt hash stored in the database
  - `role`: The user's role in the system
- Line 22 calls the `check_password` function explained earlier:
  - Passes the entered password and stored hash
  - Returns True only if the password matches the hash
- Lines 23-24 remove the user from the failed attempts dictionary if login is successful

```python
            # Redirect user based on role
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
```

**Lines 25-36: Role-Based Redirection**
- This code block implements role-based access control
- The system has four different user roles with different interfaces:
  - Customer (lines 26-28)
  - Delivery person (lines 29-31)
  - Employee (lines 32-34)
  - Admin (lines 35-37)
- For each role, the function:
  1. Sets the current screen using `self.manager.current = "screen_name"`
  2. Passes the username to the destination screen
- Line 38 exits the function with `return` after successful login and redirection

```python
    # Handle incorrect credentials
    if username in failed_attempts:
        failed_attempts[username][0] += 1
    else:
        failed_attempts[username] = [1, time.time()]
    remaining_attempts = 5 - failed_attempts[username][0]
    if remaining_attempts > 0:
        self.show_popup(f"Invalid credentials. {remaining_attempts} attempts remaining.")
    else:
        self.show_popup("Too many failed attempts. Try again in 5 minutes.")
```

**Lines 39-48: Failed Login Handling**
- This code executes only if the login failed (invalid username or wrong password)
- Lines 40-43 update the failed attempts counter:
  - If the username already has failed attempts, increment the counter (line 41)
  - Otherwise, create a new entry with 1 attempt and current timestamp (line 43)
- Line 44 calculates remaining attempts before lockout
- Lines 45-48 display appropriate error messages:
  - If attempts remain, show how many are left (line 46)
  - If no attempts remain, show the lockout message (line 48)

## Security Features Implemented

1. **Input Sanitization**: Prevents SQL injection attacks by sanitizing user input
2. **Parameterized Queries**: Adds additional SQL injection protection
3. **Rate Limiting**: Prevents brute force attacks by limiting login attempts
4. **Account Lockout**: Temporarily locks accounts after multiple failed attempts
5. **Secure Password Verification**: Uses bcrypt to safely verify passwords without storing them in plaintext
6. **Role-Based Access Control**: Directs users to appropriate interfaces based on their permission level
7. **Proper Database Handling**: Opens and closes connections appropriately
---

# **2. Point Mining System**
### **Code:**
```python
def mine_points(self, dt):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT points, visit_count, last_visit FROM users WHERE username = ?", (self.username,))
    user = cursor.fetchone()
    conn.close()

    if user:
        points, visit_count, last_visit = user
        current_time = datetime.utcnow()
        elapsed_time = current_time - self.logged_in_time
        points_to_add = int((elapsed_time.total_seconds() // 60) * (1 + self.session_order_count))

        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET points = points + ? WHERE username = ?", (points_to_add, self.username))
        conn.commit()
        conn.close()

        self.logged_in_time = current_time
```
### **Detailed Explanation:**
I'll provide a confident and definitive explanation of the `mine_points` method for your computer science project.

## Detailed Analysis of `mine_points` Method

```python
def mine_points(self, dt):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT points, visit_count, last_visit FROM users WHERE username = ?", (self.username,))
    user = cursor.fetchone()
    conn.close()
```

**Lines 1-6: Method Declaration and Database Query**
- This is a method of a class as indicated by the `self` parameter
- The `dt` parameter represents delta time (time elapsed since last call)
- This method is called periodically by a scheduler or timer system
- Lines 2-3 establish a connection to an SQLite database and create a cursor
- Line 4 executes a parameterized SQL query to retrieve user data:
  - Selects three columns: points, visit_count, and last_visit
  - Uses the username stored in `self.username` as the query parameter
  - The `?` placeholder prevents SQL injection by safely inserting the username value
- Line 5 fetches the first matching record into the `user` variable
- Line 6 closes the database connection to free up resources

```python
    if user:
        points, visit_count, last_visit = user
        current_time = datetime.utcnow()
        elapsed_time = current_time - self.logged_in_time
        points_to_add = int((elapsed_time.total_seconds() // 60) * (1 + self.session_order_count))
```

**Lines 7-11: Points Calculation Logic**
- Line 7 checks if a user record was found in the database
- Line 8 unpacks the database result into variables:
  - `points`: Current point balance
  - `visit_count`: Number of times the user has visited
  - `last_visit`: Timestamp of the user's last visit
- Line 9 gets the current UTC time using `datetime.utcnow()`
- Line 10 calculates the time elapsed since the user logged in:
  - `self.logged_in_time` is set when the user logs in or when points were last mined
  - The result is a timedelta object representing the exact time difference
- Line 11 calculates the points to award based on a formula:
  - `elapsed_time.total_seconds() // 60` converts the elapsed time to whole minutes
  - Multiplies by `(1 + self.session_order_count)`, creating a bonus for users who place orders
  - The `int()` function ensures the final result is an integer

```python
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET points = points + ? WHERE username = ?", (points_to_add, self.username))
        conn.commit()
        conn.close()
        self.logged_in_time = current_time
```

**Lines 12-17: Database Update and Time Reset**
- Lines 12-13 establish a new connection to the database and create a cursor
- Line 14 executes an UPDATE query to add the calculated points to the user's account:
  - `points = points + ?` increments the current points value
  - Uses a parameterized query with two parameters: points_to_add and username
- Line 15 commits the transaction to save changes to the database
- Line 16 closes the database connection
- Line 17 updates `self.logged_in_time` to the current time, resetting the timer for the next calculation cycle

## Functional Analysis

This method implements a loyalty/reward system that grants points based on time spent in the application:

1. **Reward Mechanism**: Users earn points for time spent on the platform, encouraging longer engagement.

2. **Time-Based Calculation**: Points are awarded per minute of activity.

3. **Order Bonus**: The formula `(1 + self.session_order_count)` provides a multiplier effect - users who place more orders during their session earn points faster.

4. **Periodic Execution**: The `dt` parameter is the time delta passed by the scheduling system that calls this method at regular intervals.

5. **Session Tracking**: The system tracks login time and resets it after each point award, ensuring continuous but segmented point accumulation.

## Technical Implementation Details

1. **Database Operations**: The method performs two separate database operations:
   - First retrieves the user's current data
   - Then updates the points value

2. **UTC Time Usage**: Using `datetime.utcnow()` ensures consistent time calculations regardless of the server's timezone.

3. **Integer Division**: The `//` operator ensures that only whole minutes are counted for points, preventing fractional point awards.

4. **Parameterized Queries**: SQL injection protection is maintained through parameterized queries.

5. **Transaction Management**: The `commit()` call ensures that changes are saved to the database.

# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration
