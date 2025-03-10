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

## System Diagram **SL**

![System Diagrams unit 2](https://github.com/user-attachments/assets/719228e9-3e4b-4e92-89a1-4a5887e0c73d)

**Fig.1** System diagram for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with the sensor DHT11 locally on an Arduino and remotely with a raspberry Pi. The latter implements an API (192.162.4.61/readings) providing access to remotely sensed data via ISAK-S network.


![System Diagrams unit 2 (1)](https://github.com/user-attachments/assets/7ec53d20-7afa-4279-8ac2-b5798e38f4db)

**Fig.2** System diagram (HL) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with a network of DHT11/BMP280 sensors locally. A remote server provides and API for remote monitoring and storage via the ISAK-S network. 

![System Diagrams unit 2 (2)](https://github.com/user-attachments/assets/36775cba-6730-45d3-bccb-57b4d8a8179d)

**Fig.3** Fig. 3 System diagram (HL+) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with a network of DHT11/BMP280 sensors locally on a Raspberry Pi. A remote server provides and API for remote monitoring and storage (192.162.6.142) via the ISAK-S network. A laptop for remote work is included.

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

### 1. Filtering using moving average

Things to explain: a) what problem are you trying to solve (what success criteria), b) demonstrate your technical
understanding, c) algorithmic thinking.

Ex: To solve SC#1 I encounter the problem that the values from teh sensors are noisy due to the changes in the
temperature and other variables. I thougt about using an algorithm to filter the data and smooth it. After some reseach
I decided to use the moving average. To make things more sustainable and organized I decided to use a function to
implemented the moving average and placed it in a library.
```.py
def moving_average(windowSize:int, x:list)->list:
    # this function  has a purpose XXXX
    #The inputs are XXXXX
    # the output is xxxx
    x_smoothed = []
    for i in range(0, len(x)-windowSize):
        x_section = x[i:i+windowSize]
        x_average = sum(x_section)/windowSize
        x_smoothed += [x_average]

    return x_smoothed
```
In the code above, we can see that the function signature includes two inputs, ```windowSize:int ``` is the size used for filtering which is of
data type integer.....


# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration
