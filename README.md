![11e470e9022f4fc5b367429bcbb285bc](https://github.com/comsci-uwc-isak/unit2_2023/assets/53995212/1d14b1d3-ae39-4ef3-8ec9-3329630eacae)

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

The solution provides a secure and efficient user authentication system for customers, employees, and delivery drivers.
[Issue Tackled]: Prevents unauthorized access and ensures that each user has appropriate access to platform functionalities.

The platform allows customers to place dine-in and delivery orders through a user-friendly interface.
[Issue Tackled]: Eliminates reliance on traditional waitstaff, reducing human error and improving ordering efficiency.

Multiple payment methods, including card payments and a points-based loyalty system, are supported.
[Issue Tackled]: Provides flexibility in payment options, enhancing customer convenience and engagement.

A loyalty program is implemented, where customers earn points based on past orders and can redeem them for discounts or exclusive menu items.
[Issue Tackled]: Encourages repeat customers and increases brand loyalty.

The system includes an order-tracking feature, allowing customers to view their order status in real time.
[Issue Tackled]: Enhances transparency and reduces customer inquiries about order progress.

Delivery drivers can register, accept nearby orders, and track their earnings through a dedicated interface.
[Issue Tackled]: Improves efficiency and ensures that deliveries are completed in a timely manner.

A rating system is included to allow customers to provide feedback on orders and delivery experiences.
[Issue Tackled]: Helps maintain high service quality by identifying areas for improvement.

Restaurant employees can track their remaining shift time and mark orders as completed.
[Issue Tackled]: Enhances workflow efficiency and ensures accurate order fulfillment.

Orders and customer data are securely stored and managed using an SQLite database.
[Issue Tackled]: Provides a lightweight, serverless storage solution that is easy to maintain and efficient for restaurant operations.

The platform includes an admin dashboard where managers can monitor orders, employees, and delivery performance.
[Issue Tackled]: Allows for better oversight and decision-making to optimize restaurant operations.

A menu management system is available, enabling administrators to add, update, or remove menu items.
[Issue Tackled]: Provides flexibility in menu updates, ensuring accurate pricing and availability.

The application is built using Python and Kivy, ensuring cross-platform compatibility for mobile and desktop devices.
[Issue Tackled]: Reduces development overhead and allows for a single codebase across different platforms.

The system includes offline functionality for essential features, such as order tracking and staff shift monitoring.
[Issue Tackled]: Ensures continued usability even in cases of internet disruptions.

A notification system is implemented to send real-time updates about order status, promotions, and loyalty rewards.
[Issue Tackled]: Keeps customers and staff informed about important updates.

A reporting feature generates summaries of order trends, peak business hours, and customer preferences.
[Issue Tackled]: Provides valuable insights for restaurant management to optimize service and marketing strategies.

The system includes a feedback collection feature for customers to provide suggestions and complaints.
[Issue Tackled]: Enables continuous improvement by gathering direct input from users.

A security mechanism is in place to prevent multiple failed login attempts and unauthorized access.
[Issue Tackled]: Protects user data and maintains system integrity.
_TOK Connection: To what extent does ```the use of data science``` in climate research influence our understanding of environmental issues, and what knowledge questions arise regarding the ```reliability, interpretation, and ethical implications``` of data-driven approaches in addressing climate change_

1. How does our use of technology shape our understanding of the environment
2. What responsibilities do we have as technologists when it comes to handling personal data related to our living spaces?
3. What cultural and contextual factors might impact our interpretation of the results, especially when comparing our local readings with those from the campus? 

# Criteria B: Design

## System Diagram **SL**

![System Diagrams unit 2](https://github.com/user-attachments/assets/719228e9-3e4b-4e92-89a1-4a5887e0c73d)

**Fig.1** System diagram for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with the sensor DHT11 locally on an Arduino and remotely with a raspberry Pi. The latter implements an API (192.162.4.61/readings) providing access to remotely sensed data via ISAK-S network.


![System Diagrams unit 2 (1)](https://github.com/user-attachments/assets/7ec53d20-7afa-4279-8ac2-b5798e38f4db)

**Fig.2** System diagram (HL) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with a network of DHT11/BMP280 sensors locally. A remote server provides and API for remote monitoring and storage via the ISAK-S network. 

![System Diagrams unit 2 (2)](https://github.com/user-attachments/assets/36775cba-6730-45d3-bccb-57b4d8a8179d)

**Fig.3** Fig. 3 System diagram (HL+) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with a network of DHT11/BMP280 sensors locally on a Raspberry Pi. A remote server provides and API for remote monitoring and storage (192.162.6.142) via the ISAK-S network. A laptop for remote work is included.

## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Write the Problem context                        | 10min         | Nov 22                 | A         |

## Test Plan

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
