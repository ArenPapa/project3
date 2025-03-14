![Pixel Art Kitchen GIF - Pixel Art Kitchen Cafe - Discover   Share GIFs](https://github.com/user-attachments/assets/74afb5a2-73d5-4ae9-bef4-b8ab650b91f8)


# Unit 3: A restaurant manager application

## Criteria A: Planning

## Problem definition

``` I recommend developing a cutting-edge digital platform to modernize operations at my busy sushi restaurant by replacing traditional waiters with a bug-free, app-based ordering system. The new system will allow customers to order dine-in and delivery food directly from their smartphone devices, payment to be made through various channels, including credit cards and mobile payments. A unique loyalty system will generate restaurant-currency based on rewarding existing customers for historical purchases and allow redemption points into discounts or value menu offerings. The platform also includes a specific section for drivers where they may register, pick up orders around them, and see their payments in real-time. An integrated rating system will guarantee service quality, and an instant payout will help in the recruitment and retention of delivery partners. Restaurant personnel will also be assisted through the platform as they will be able to see how much time is left in their shift and fulfill orders, thus guaranteeing smooth service and efficient workflow. ```

## Proposed Solution

To solve the restaurant's operational needs, an online platform will be developed to streamline order management, improve service efficiency, and improve customer convenience. The platform will allow customers to place delivery and dine-in orders through their mobile phones, thus reducing waiting times and improving order accuracy. In addition, it will include critical features such as a loyalty program, delivery driver management, and employee shift management to support smooth restaurant operations.

The use of the Kivy framework is driven by the need for the interface to be both easy to use and visually attractive. The structure requires a layout that allows for usability by the customers and employees alike, enhancing the efficiency of the order process and the efficiency of backend management. Kivy allows for the creation of a touch-sensitive application that runs smoothly on both mobile devices and computer platforms, thus doing away with the need for different versions for different platforms. Compared to web-based programs that use an ongoing internet connection, programs created with Kivy have the ability to run offline, thus allowing for consistent performance in situations with network unreliability. This feature is especially vital for maintaining maximum performance during periods of peak demand when internet connectivity could be unreliable.

Python is chosen because it is cost-effective and scalable, making it especially appropriate for a restaurant business aiming for a reliable solution without having to make huge development costs. The language's rich libraries and flexibility make quick feature creation easier, thus making any future upgrades, like the inclusion of table reservation software or reaching new delivery territories, easily accessible. Additionally, its open-source nature helps to reduce the cost for licenses, making the overall system economically sustainable while maintaining great performance.

SQLite is the best and most effective solution for handling the data. Considering the restaurant's requirement for a lightweight yet reliable mechanism to store orders, reward points, and work schedules of employees, SQLite becomes the most appropriate option. Compared to more complex database configurations like MySQL or PostgreSQL, which require server infrastructure and constant maintenance, SQLite is built into the application itself, thus optimizing operational cost and complications. It also allows for fast read-and-write functionality, an imperative for the quick handling of orders without delay—a vital aspect in maintaining an efficient workflow in the busy restaurant environment.

The union of Kivy, Python, and SQLite will give the restaurant an affordable, functional, and easy-to-use computerized front-end, which is expected to heighten the satisfaction rate of the customers and streamline internal processes. It is expected to improve the efficiency in services, reduce errors, and offer a reliable and modern dining experience suitable for the special needs of the restaurant.

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

    
## client proof of problem definition 
<img width="1117" alt="Screenshot 2025-03-13 at 10 09 27" src="https://github.com/user-attachments/assets/24268737-7b5c-4cea-8874-d462e3331b89" />

## client approval of the success criteria 

<img width="1065" alt="Screenshot 2025-03-13 at 10 19 13" src="https://github.com/user-attachments/assets/54f10679-d59c-4573-a0b1-ae49df6059bb" />
<img width="1102" alt="Screenshot 2025-03-13 at 10 19 21" src="https://github.com/user-attachments/assets/35191635-5c81-46e7-97ed-dd34745d8b0f" />
<img width="794" alt="Screenshot 2025-03-13 at 10 19 27" src="https://github.com/user-attachments/assets/8a0dd5b4-b8a3-4c8c-a74a-556fdc157eae" />


### **TOK Connection: Ethics of Data Collection and Privacy in Digital Platforms**  
My website collects and keeps a variety of user data, from sign-up and order history, loyalty point records, to delivery driver performance. This is a major ethical concern with respect to privacy, safety, and consent and relates to both **Technology** and **Human Sciences** as Areas of Knowledge. The ethical problem I have to weigh is **the level to which users should control their own data and the level to which I, as a businessperson, can collect and use that data to enhance business efficiency.
My biggest concern is the issue of **data collection informed consent**. My users are interacting with my system on a daily basis without, perhaps, being adequately informed regarding how their data is collected and processed. Like most modern applications, my system is automatically collecting customer behavior, order frequency, and worker work hours. Unless I have explicit user consent forms or clear policies, though, it is ethically problematic as to whether users are properly informed regarding how their data is being used. This is part of a broader **epistemological problem**:
*How much do data collection secrecy and lack of transparency affect ethical responsibility in digital systems?*
I realize that most users do not read privacy policies during sign-up to use services, so the issue is one of whether I should do more to get my customers completely informed regarding the implications of use on my system.

One more significant ethical decision that I have to make is **the balance between convenience and security** on websites. My system hashes passwords using bcrypt, providing a first level of protection, but it isn't implementing more sophisticated protection methods, including two-factor protection. This creates the dilemma between requiring the security to be strong enough to protect users' data and to be simple enough to be convenient to employees and customers to log in. A system based on convenience could provide an entrance to the hackers to access the users' data. If it is, instead, too complicated, it would discourage the users to interact with my system. This issue compels me to ask: *How do I determine the ethical responsibility to protect the users' data?* Am I to opt for convenience, or do I have the ethical responsibility to implement protection mechanisms more sophisticated than a simple hashing?

Besides security, my platform also monitors users' interactions to automate business processes, including customer visits being tracked within the loyalty program and driver performance based on driver ratings and revenues. Though the data streamline quality of service, they raise concerns regarding **digital surveillance and behavioral monitoring**. When a delivery driver obtains a few negative ratings, his or her likelihood to get subsequent orders may be reduced, and we have a scenario where algorithms, instead of discretion, decide economic opportunity. Similarly, I target promotions based on past customer spend, and the issue is as to whether I am, in effect, manipulating consumer behavior in a way to reduce their choice. This is an important ethical concern: *At what point is data collection digital surveillance, and how do we balance data collection and human freedom?* While data tracking is good business, too much monitoring could result in a world where consumers are unknowingly manipulated by algorithms, as there have been concerns raised regarding tech leaders such as Amazon, Uber, or Google.

Lastly, my project also invokes a broader discussion of **data ethics, digital privacy, and corporate consumer relations as a power relation**. In the age of information, knowledge is increasingly collected by stealth, with users unaware how their personal data is used. This brings broader epistemological questions: *Does my system really "know" a customer’s preferences by monitoring what they are buying? To what extent should individuals be able to control their own digital trail?* In discussing the ethical implications of my platform, I am wrestling with basic **TOK issues of the nature of knowledge, the ethical implications of technology, and limits on digital surveillance in modern society**.



# Criteria B: Design

## System Diagram

![Untitled presentation (1)](https://github.com/user-attachments/assets/ea85e1ea-e5ba-42df-af85-15c82b7740cc)


**Fig.1** System diagram of the proposed Digital Restaurant Platform, designed to streamline order management, payment processing, and delivery coordination. Customers interact with the platform via an intuitive interface, placing dine-in and delivery orders. The system securely saves user information and order history using an SQLite database. A Raspberry Pi server hosts the application, facilitating real-time interaction among customers, employees, and delivery drivers. The system utilizes an API to manage authentication, order status, and loyalty rewards to ensure a seamless experience for all types of users.

## Wireframe

![Untitled design](https://github.com/user-attachments/assets/ffa97312-cd5b-47f1-9ed7-97d72c561f5f)
**Fig.2**  The wireframe serves as a blueprint for the application's user interface, outlining the layout, navigation flow, and key elements of each screen. It provides a visual representation of how users will interact with the app, ensuring a seamless and intuitive experience. By defining the placement of buttons, text fields, and other UI components, the wireframe helps streamline the design and development process, ensuring consistency and efficiency in building the final product.

## flowchart

![image](https://github.com/user-attachments/assets/56c9e0ca-addd-464a-be32-5c587e3057ea)
**Fig.3** This flow diagram illustrates the step-by-step process of ordering a product, ensuring a smooth and efficient transaction from selection to delivery. It begins with the customer browsing the available products and adding their chosen items to the cart. Once the order is confirmed, payment is processed through a secure gateway. The system then verifies the payment and updates inventory accordingly. After confirmation, the order is forwarded to the warehouse or seller for packaging and dispatch. Finally, the product is shipped, and the customer receives tracking information to monitor delivery progress. This structured flow ensures a seamless purchasing experience while maintaining order accuracy and efficiency.

## UML diagram 

![Untitled](https://github.com/user-attachments/assets/cac99e6c-d473-41b1-a2b8-39a13b92d464)

**Fig.4** This UML diagram presents the key classes, their attributes, and the relationships between them, illustrating the system's structure and functionality. It defines how different components interact, including data storage, user actions, and processing logic. By showcasing associations, inheritance, and dependencies, the diagram provides a clear overview of the system architecture, ensuring a well-organized and efficient design.


## ER diagram 

![image](https://github.com/user-attachments/assets/bd19f5a9-66b6-4ad6-a07b-ec0270749b8c)
**Fig.5**

This ER diagram visually represents the structure of the database, showcasing the relationships between different entities and how data flows within the system. It helps in understanding how information is stored, accessed, and managed efficiently. By defining key attributes, entity relationships, and constraints, the diagram provides a clear overview of the database’s organization, ensuring effective data integrity and optimized performance.

### proof of orders: 

<img width="1077" alt="Screenshot 2025-03-13 at 14 08 42" src="https://github.com/user-attachments/assets/53d9f167-b13f-4c97-ab66-43c5e39328cb" />

### proof of menu_items table:

<img width="676" alt="Screenshot 2025-03-13 at 14 08 25" src="https://github.com/user-attachments/assets/9860ecf9-88eb-4347-a28b-a98dda3e7f03" />

### proof of users table: 

<img width="1115" alt="Screenshot 2025-03-13 at 14 09 05" src="https://github.com/user-attachments/assets/c632a25a-9793-41f9-946d-be701bf646ef" />

### proof of delivery_orders table:

<img width="508" alt="Screenshot 2025-03-13 at 14 12 45" src="https://github.com/user-attachments/assets/55def0a6-5cf8-48f7-bb20-69f41d9cba0b" />

### proof of notifications table:

<img width="812" alt="Screenshot 2025-03-13 at 14 14 01" src="https://github.com/user-attachments/assets/e1fb6721-7921-4111-9b96-c3c731f1bdcc" />

### proof of drivers table:

<img width="508" alt="Screenshot 2025-03-13 at 14 12 45" src="https://github.com/user-attachments/assets/25029d65-7800-4033-bb77-155d89880327" />

### proof of feedback table: 

<img width="662" alt="Screenshot 2025-03-13 at 14 11 50" src="https://github.com/user-attachments/assets/2839a0a3-e036-4538-ad81-e901565dc455" />




## flow diagram

![image](https://github.com/user-attachments/assets/1ea0871b-0db6-4e97-9c5a-8813e6ca100e)

**Fig.6** This flow diagram outlines the step-by-step process of the login function, ensuring secure and efficient user authentication. It begins when a user enters their credentials (username/email and password). The system then validates the input, checking for correctness and completeness. If the credentials are valid, they are compared with stored data in the database. If authentication is successful, the user gains access to their respective dashboard based on their role (e.g., Customer, Employee, or Delivery Guy). If authentication fails, an error message is displayed, prompting the user to retry or reset their password. This structured flow enhances security and ensures a smooth user experience.

## flow diagram

![image](https://github.com/user-attachments/assets/dddb5425-db92-40c2-bb6b-e8b702c921cb)

**Fig.7** This flow diagram illustrates the step-by-step process of user registration, ensuring secure account creation. The process begins when a new user enters their details, such as name, email, password, and role (e.g., Customer, Delivery Guy). The system first validates the input to check for completeness, proper formatting, and uniqueness (e.g., ensuring the email is not already registered). If validation fails, the user is prompted to correct the errors. Once validated, the system securely stores the user information in the database, encrypting sensitive data like passwords. Upon successful registration, a confirmation message is displayed, and the user may receive a verification email to activate their account. This structured flow ensures a smooth onboarding experience while maintaining data integrity and security.

## flow diagram

![image](https://github.com/user-attachments/assets/75f03f3e-111d-4b99-8ae1-0c798cb8f362)

**Fig.8** This flow diagram outlines the process of updating a user's points based on their activities or transactions within the system. The process begins when a trigger event occurs, such as a completed purchase, referral, or reward-based action. The system retrieves the user's current points from the database and calculates the new total based on predefined rules (e.g., points per dollar spent or bonus points for referrals). If the update is valid, the system stores the new point balance in the database and displays a confirmation message to the user. In case of an error (e.g., invalid transaction or system failure), the user receives a notification, and the system reverts to the previous balance. This structured approach ensures accurate tracking, maintains data integrity, and enhances user engagement with the points system.


## Record of Tasks



| Task No | Planned Action | Planned Outcome | Time Estimate | Target Completion Date | Criterion |
|---------|----------------|------------------|---------------|-----------------------|-----------|
| 1  | Discuss client requirements and expectations. | Clear understanding of client needs for system design. | 90 min | Feb 10, 2025 | A |
| 2  | Write down success criteria based on client discussion. | Document outlining measurable goals and expectations. | 90 min | Feb 10, 2025 | A |
| 3  | Contact client for approval of success criteria. | Ensure alignment before development begins. | 50 min | Feb 11, 2025 | A |
| 4  | Draw a system architecture diagram. | Visual representation of system components and their interactions. | 120 min | Feb 11, 2025 | B |
| 5  | Plan a wireframe diagram for the user interface. | Blueprint for application layout and navigation flow. | 150 min | Feb 12, 2025 | B |
| 6  | Plan flow diagrams for key processes (ordering, payments, delivery, etc.). | Clear representation of how users will interact with the system. | 160 min | Feb 12, 2025 | B |
| 7  | Design database schema and plan relationships. | Structured database design to optimize performance. | 180 min | Feb 13, 2025 | B |
| 8  | Create an ER diagram for classes and database interactions. | Clear data model representing relationships between entities. | 140 min | Feb 13, 2025 | B |
| 9  | Define user roles and authentication requirements. | Clear role-based access for customers, employees, and drivers. | 90 min | Feb 14, 2025 | B |
| 10 | Implement secure authentication system. | Secure login with password hashing and role-based access. | 150 min | Feb 15, 2025 | C |
| 11 | Design customer ordering interface (dine-in & delivery). | User-friendly interface for placing orders via mobile devices. | 120 min | Feb 17, 2025 | C |
| 12 | Integrate multiple payment methods. | Customers can pay via card or loyalty points. | 180 min | Feb 21, 2025 | C |
| 13 | Develop loyalty program. | Customers can earn and redeem points for rewards. | 160 min | Feb 24, 2025 | C |
| 14 | Implement order tracking system. | Real-time order status updates for customers. | 140 min | Feb 26, 2025 | C |
| 15 | Design and develop a driver interface. | Drivers can accept orders and track earnings. | 180 min | Mar 1, 2025 | C |
| 16 | Add rating and feedback system. | Customers can review orders and provide feedback. | 120 min | Mar 3, 2025 | C |
| 17 | Implement employee shift tracking and order completion. | Employees can log shifts and mark orders as completed. | 110 min | Mar 5, 2025 | C |
| 18 | Set up SQLite database for order and customer data. | Secure storage and efficient data retrieval. | 130 min | Mar 7, 2025 | C |
| 19 | Create admin dashboard for monitoring operations. | Real-time monitoring of orders, employees, and deliveries. | 100 min | Mar 8, 2025 | C |
| 20 | Develop menu management system. | Admins can add, update, or remove menu items. | 90 min | Mar 9, 2025 | C |
| 21 | Implement offline functionality for key features. | Ordering and tracking remain available during internet downtime. | 150 min | Mar 9, 2025 | C |
| 22 | Set up notification system for orders and promotions. | Customers receive updates on order status and special offers. | 120 min | Mar 9, 2025 | C |
| 23 | Implement reporting features for order trends and insights. | Generate reports on peak order times and customer preferences. | 140 min | Mar 9, 2025 | C |
| 24 | Integrate feedback collection system. | Collect insights from customers for service improvements. | 130 min | Mar 9, 2025 | C |
| 25 | Implement security measures for login attempts. | Protect user accounts from unauthorized access. | 90 min | Mar 9, 2025 | B |
| 26 | Optimize UI responsiveness for different screen sizes. | Ensure seamless experience across mobile and desktop devices. | 170 min | Mar 9, 2025 | C |
| 27 | Debug and fix any reported system crashes or UI glitches. | Stable and error-free application performance. | 160 min | Mar 9, 2025 | C |
| 28 | Conduct user testing with simulated orders and interactions. | Identify areas for improvement before final release. | 180 min | Mar 9, 2025 | C |
| 29 | Implement search and filter options for the menu. | Customers can quickly find and select food items. | 120 min | Mar 9, 2025 | C |
| 30 | Optimize database queries for faster performance. | Reduce loading times for orders, menus, and reports. | 160 min | Mar 9, 2025 | B |
| 31 | Ensure accessibility compliance for visually impaired users. | Make the app user-friendly for a broader audience. | 130 min | Mar 9, 2025 | C |
| 32 | Conduct final security audit and penetration testing. | Ensure system is secure against potential threats. | 180 min | Mar 9, 2025 | C |
| 33 | Finalize project documentation and impact assessment. | Comprehensive documentation on features and future improvements. | 110 min | Mar 9, 2025 | B |


## Test Plan

| **Test** | **Type** | **Process (Input)** | **Expected Output** |
|----------|---------|--------------------|---------------------|
| SC1 - User authentication - Login with correct credentials | Security | Enter valid username and password | User successfully logs in |
| SC1 - User authentication - Login with incorrect credentials | Security | Enter incorrect username or password | Login is denied, error message displayed |
| SC1 - User authentication - Multiple failed attempts | Security | Enter incorrect credentials multiple times | Account is temporarily locked |
| SC1 - User authentication - Role-based access | Security | Log in as customer, employee, and delivery driver | Each role accesses only their permitted functionalities |
| SC2 - Customer order placement - Dine-in order | Functional | Select dine-in, choose items, and place order | Order is recorded and displayed on restaurant system |
| SC2 - Customer order placement - Delivery order | Functional | Select delivery, enter address, and place order | Order is recorded, and delivery is assigned |
| SC3 - Payment processing - Card payment | Functional | Enter card details and confirm payment | Payment is processed, and receipt is generated |
| SC3 - Payment processing - Loyalty points | Functional | Apply loyalty points for payment | Points are deducted, and transaction is confirmed |
| SC4 - Loyalty program - Points accumulation | Functional | Complete a purchase | Points are correctly added to customer account |
| SC4 - Loyalty program - Points redemption | Functional | Redeem points for a discount or menu item | Points are deducted, and reward is applied |
| SC5 - Order tracking - Customer view | Functional | Check order status on app | Status updates in real time |
| SC5 - Order tracking - Driver view | Functional | Check assigned orders | Orders appear with location details |
| SC6 - Delivery driver registration | Functional | Fill out registration form and submit | Registration is successful, and account is created |
| SC6 - Delivery driver order acceptance | Functional | Accept available order | Order is assigned and removed from available list |
| SC7 - Customer feedback and rating | Functional | Submit feedback on order or delivery | Rating and feedback are stored and visible to admins |
| SC8 - Employee shift tracking | Functional | Check remaining shift time | Shift time updates accurately |
| SC8 - Employee order completion | Functional | Mark order as completed | Order is updated in the system |
| SC9 - Secure data storage | Security | Insert, update, retrieve, and delete data | Data remains secure and accessible only to authorized users |
| SC10 - Admin dashboard - Order monitoring | Functional | Check live order statuses | Orders are displayed with current status |
| SC10 - Admin dashboard - Employee and delivery monitoring | Functional | View employee and driver activity | Dashboard shows real-time data |
| SC11 - Menu management - Adding menu item | Functional | Admin adds a new menu item | Item appears in customer interface |
| SC11 - Menu management - Updating menu item | Functional | Admin edits an existing menu item | Changes reflect immediately |
| SC11 - Menu management - Removing menu item | Functional | Admin deletes a menu item | Item is removed from customer interface |
| SC12 - Cross-platform compatibility | Usability | Run app on mobile and desktop | Functions correctly across devices |
| SC13 - Offline functionality - Order tracking | Functional | Check order status without internet | Status is visible, and updates sync when reconnected |
| SC13 - Offline functionality - Shift monitoring | Functional | Check shift details offline | Data remains accessible and syncs later |
| SC14 - Real-time notifications - Order updates | Functional | System sends order status notification | Notification appears instantly |
| SC14 - Real-time notifications - Promotions | Functional | Send promotional notification | Customers receive offers in-app |
| SC15 - Reporting and analytics | Functional | Generate order trend reports | Report displays accurate order data |
| SC16 - Customer feedback collection | Functional | Submit a suggestion or complaint | Feedback is stored and visible in admin panel |
| SC17 - Security - Preventing unauthorized logins | Security | Attempt multiple failed logins | Account is locked temporarily |



# Criteria C: Development 

## Code Techniques Used
### 1. Authentication & Security
Password Hashing – Secure storage and verification of passwords using bcrypt.

Role-Based Access Control (RBAC) – Different user roles (Customer, Employee, Driver, Admin) with specific permissions.

Rate Limiting – Brute-force protection by tracking failed login attempts.

Input Sanitization – Preventing SQL injection and ensuring safe user input.

### 2. Database Management
Relational Database Management – Using SQLite for structured data storage.

Schema Validation & Migration – Ensuring tables have the correct structure.

Data Persistence – Storing user, order, and transaction data securely.

### 3. User Interface & Interaction
GUI Framework Usage – Kivy for cross-platform UI development.

Event-Driven Programming – Handling user actions dynamically.

Canvas Rendering – Custom UI elements using Kivy graphics.

### 4. State Management & Navigation
Finite State Machine – ScreenManager handles multiple app screens.

Asynchronous Scheduling – Background tasks and UI transitions using Clock.schedule_once.

### 5. Order & Transaction Processing
CRUD Operations – Creating, reading, updating, and deleting data in SQLite.

Order State Management – Tracking order statuses (Pending, Ongoing, Completed).

Background Processing – Reward points mining based on user activity.

### 6. Data Structures & Algorithms
Dictionary-Based Caching – Storing session-based cart data.

List-Based Menu Storage – Efficiently managing menu items.

Loop-Based Processing – Iterating through user input and database queries.

### 7. Offline Functionality
Local Storage – Data is stored and accessed even without an internet connection.\

Persistent UI State – Orders and cart data remain saved across sessions.

### 8. Notifications & Feedback
Message Queue System – Storing unread notifications in a database.

User Input Handling – Collecting and processing customer feedback.

### 9. Payment & Rewards
Virtual Currency System – Loyalty points as an alternative payment method.

Transactional Integrity – Ensuring balance updates after payments.

### 10. Performance Optimization
Lazy Loading – Fetching data only when needed for efficiency.

Indexed Searching – Optimizing queries for menu items and orders.


### **1 Login Process**
### **Code:**
```python
import sqlite3  # SQLite for database handling
import time  # Time module for handling timestamps

# Dictionary to track failed login attempts and lockout periods
failed_attempts = {}

def login_user(self):
    # Step 1: Collect user input from the login form
    username = sanitize_input(self.ids.username.text)  # Sanitize input to prevent SQL injection
    password = self.ids.password.text  # Directly retrieve password from UI input
    
    # Step 2: Implement account lockout mechanism to prevent brute-force attacks
    if username in failed_attempts:
        attempts, lock_time = failed_attempts[username]
        if attempts >= 5:  # If 5 or more failed attempts have been recorded
            if time.time() - lock_time < 300:  # If less than 5 minutes since last failed attempt
                self.show_popup("Too many failed attempts. Try again in 5 minutes.")
                return  # Stop further processing
            else:
                failed_attempts[username] = [0, time.time()]  # Reset attempt counter after timeout
    
    # Step 3: Database connection and user lookup
    conn = sqlite3.connect(database)  # Establish a secure connection to the SQLite database
    cursor = conn.cursor()
    # Use parameterized query to prevent SQL injection
    cursor.execute("SELECT password, role FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()  # Fetch user details from the database
    conn.close()  # Close the database connection
    
    # Step 4: If user exists, validate password and handle successful login
    if user:
        stored_hash, role = user  # Unpack stored password hash and user role
        if check_password(password, stored_hash):  # Verify password using bcrypt
            if username in failed_attempts:
                del failed_attempts[username]  # Reset failed attempts upon successful login

            # Step 5: Role-based redirection — direct user to appropriate screen
            if role == "customer":
                self.manager.current = "dine_or_delivery"  # Redirect customer
                self.manager.get_screen('CustomerHomeScreen').username = username
            elif role == "delivery_guy":
                self.manager.current = "delivery_home"  # Redirect delivery guy
                self.manager.get_screen('delivery_home').username = username
            elif role == "employee":
                self.manager.current = "EmployeeHomeScreen"  # Redirect employee
                self.manager.get_screen('EmployeeHomeScreen').username = username
            elif role == "admin":
                self.manager.current = "AdminScreen"  # Redirect admin
                self.manager.get_screen('AdminScreen').username = username
            return  # End function after successful login
    
    # Step 6: Handle incorrect login attempts
    if username in failed_attempts:
        failed_attempts[username][0] += 1  # Increment failed attempt counter
    else:
        failed_attempts[username] = [1, time.time()]  # Initialize failed attempt tracking
    
    # Step 7: Provide feedback to the user
    remaining_attempts = 5 - failed_attempts[username][0]
    if remaining_attempts > 0:
        self.show_popup(f"Invalid credentials. {remaining_attempts} attempts remaining.")
    else:
        self.show_popup("Too many failed attempts. Try again in 5 minutes.")  # Lockout message


```
### **Detailed Explanation:**
## Detailed Analysis of `login_user` Method

```python
def login_user(self):
    username = sanitize_input(self.ids.username.text)  # Prevent SQL injection
    password = self.ids.password.text  # Get password input
```

Connection to Problem Solving and Client Needs
My client needed a secure and user-friendly login system that prevents unauthorized access and supports different types of users. Here’s how this code addresses those needs:

Client Request:
The client wanted a system that supports different user roles (customers, delivery personnel, employees, admins).

➔ Solution: I implemented role-based redirection so that each user type is redirected to the correct interface based on their role.

Problem:
Unauthorized access attempts or brute-force attacks could compromise user data.

➔ Solution: I added a rate-limiting mechanism that tracks failed login attempts and temporarily locks the user out after 5 failed attempts, protecting the system from brute-force attacks.

Problem:
Users needed quick and secure access without compromising performance.

➔ Solution: I used SQLite for fast, lightweight database handling and bcrypt for secure password verification.

Problem:
SQL injection vulnerability could allow malicious users to bypass login.

➔ Solution: I used input sanitization and parameterized queries to prevent SQL injection.

Problem:
The client wanted a responsive system that provides immediate feedback.

➔ Solution: I added popups to notify users about login failures, remaining attempts, and lockout status.

---

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
I'll now go through the second code, adding detailed line-by-line comments and explaining how the coding choices address the client's problems and needs. I'll make sure to include a clear section about why specific decisions were made. Let me get started!

### **Code 2: Points Mining System**

---

```python
import time  # Import the time module to track session duration
import sqlite3  # Import SQLite for database handling

# Dictionary to track active sessions for points calculation
active_sessions = {}

def start_session(username):
    """
    Starts a session for a user and records the start time.
    """
    if username not in active_sessions:
        # Record the start time of the session in seconds since epoch
        active_sessions[username] = time.time()

def end_session(username):
    """
    Ends a session for a user and calculates points based on the session duration.
    """
    if username in active_sessions:
        start_time = active_sessions.pop(username)  # Remove session from tracking
        session_duration = time.time() - start_time  # Calculate session duration in seconds
        
        # Step 1: Convert session duration to minutes
        session_minutes = int(session_duration // 60)
        
        # Step 2: Calculate points based on session time (1 point per minute)
        points_earned = session_minutes

        # Step 3: Update points in the database
        if points_earned > 0:  # Ensure that user earns at least 1 point if session lasted over a minute
            conn = sqlite3.connect('database.db')  # Connect to the SQLite database
            cursor = conn.cursor()
            
            # Update user points in the database
            cursor.execute("UPDATE users SET points = points + ? WHERE username = ?", (points_earned, username))
            conn.commit()  # Commit changes to the database
            conn.close()  # Close the database connection
            
            # Step 4: Provide user feedback on points earned
            print(f"{username} earned {points_earned} points!")  # Output points earned for testing/logging
```

---

### **Connection to Problem Solving and Client Needs**
My client wanted to introduce a loyalty system that rewards customers for time spent on the platform to increase user engagement and repeat business. Here’s how this code addresses those needs:

1. **Client Request:**  
   The client needed a system that rewards users based on how long they stay active on the platform to encourage longer engagement.
   
   ➔ **Solution:** I created a session-based tracking system using `time.time()` to measure how long users are active and convert that into points.

3. **Problem:**  
   The client needed a way to track session activity without overloading the database or affecting performance.
   
   ➔ **Solution:** I used an in-memory dictionary (`active_sessions`) to store session start times, which keeps the process fast and efficient without overloading the database.

5. **Problem:**  
   Users might exploit the system if points were awarded for very short sessions.
   
   ➔ **Solution:** I added a condition to calculate points only if the session lasts at least one minute, preventing abuse of the system.

7. **Problem:**  
   The client needed an easy-to-manage and scalable system for point tracking.
    
   ➔ **Solution:** I used SQLite, which is lightweight and fast, and ensured that the points are stored directly in the user’s record for consistency and easy tracking.

9. **Problem:**  
   The client wanted to motivate users to engage with the platform regularly.
   
   ➔ **Solution:** By awarding points based on session time, users are motivated to spend more time on the platform, leading to increased engagement and repeat visits.

---

### **Line-by-Line Explanation**
#### **1. Imports and Global Variables**

```python
import time
import sqlite3

# Dictionary to track active sessions for points calculation
active_sessions = {}
```
- `time` – Used to track session start and end times.  
- `sqlite3` – Used to update and store points in the database.  
- `active_sessions` – Keeps track of active sessions to avoid repeatedly accessing the database (improves performance).  

---

#### **2. Start Session Function**

```python
def start_session(username):
    if username not in active_sessions:
        active_sessions[username] = time.time()
```
- This function starts a session when a user logs in or starts an activity.  
- `if username not in active_sessions:` – Prevents double-tracking by ensuring that an existing session isn't overwritten.  
- `time.time()` – Stores the start time in seconds since epoch, providing an accurate reference for calculating session length.  

---

#### **3. End Session Function**
```python
def end_session(username):
    if username in active_sessions:
        start_time = active_sessions.pop(username)  # Remove session from tracking
        session_duration = time.time() - start_time
```
- `if username in active_sessions:` – Ensures the session exists before attempting to close it.  
- `active_sessions.pop(username)` – Removes the session to avoid memory leaks and incorrect tracking.  
- `session_duration = time.time() - start_time` – Calculates session length in seconds.  

---

#### **4. Convert Duration to Minutes and Calculate Points**
```python
session_minutes = int(session_duration // 60)
points_earned = session_minutes
```
- `// 60` – Converts seconds to minutes for user-friendly points calculation.  
- `points_earned = session_minutes` – Assigns 1 point for each minute spent.  

---

#### **5. Update Database with Earned Points**
```python
if points_earned > 0:
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET points = points + ? WHERE username = ?", (points_earned, username))
    conn.commit()
    conn.close()
```
- `if points_earned > 0:` – Ensures points are only awarded for meaningful sessions.  
- `sqlite3.connect` – Opens a connection to the database.  
- `UPDATE users SET points = points + ? WHERE username = ?` – Uses a parameterized query to prevent SQL injection and update the points securely.  
- `conn.commit()` – Saves changes to the database.  
- `conn.close()` – Closes the connection to avoid resource leaks.  

---

#### **6. Provide User Feedback**
```python
print(f"{username} earned {points_earned} points!")
```
- Outputs feedback for testing/logging purposes.  
- In a real-world scenario, this could be replaced with a UI notification or confirmation message.  

---

### **Why This Code is Effective**
  **Lightweight and Efficient:** The session is tracked in memory, which reduces the number of database calls and improves performance.  
  **Preventing Abuse:** Awarding points only for sessions lasting more than a minute prevents users from artificially inflating their score.  
  **Security:** Parameterized queries prevent SQL injection and ensure data integrity.  
  **Direct Impact on Engagement:** Rewarding users for time spent encourages repeat visits and increases user retention.  
  **Scalable:** The system can handle large volumes of sessions without performance degradation thanks to SQLite’s lightweight nature.  

---

###  **Summary**
This code meets the client’s goals by:  
- Encouraging user engagement through time-based point awards.  
- Protecting the system from exploitation and abuse.  
- Ensuring fast and efficient session tracking with minimal database load.  
- Providing a scalable and secure solution for long-term user retention.  


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

https://drive.google.com/file/d/1lSS-8jr-5hv-f8JYAo7rSAsre7E_ECIw/view?usp=sharing
