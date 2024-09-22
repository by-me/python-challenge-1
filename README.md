# Food Truck Ordering System

**Tabel of Contents:**
1. [Overview](#overview) 
2. [Features](#features)
3. [code tructure](#code-structure)
4. [Project Resouces and Acknowledgments](#project-resources-and-acknowledgments)
5. [Conclusion](#conclusion)

1. ## Overview

This project implements an interactive ordering system for a food truck. Customers can select items from a categorized menu, specify quantities, and receive a detailed receipt with the total cost of their order. The system is built using Python, demonstrating key programming concepts such as dictionaries, lists, input validation, loops, and formatted output.

2. ## Features
- **Categorized Menu**: Items are organized into Snacks, Meals, Drinks, and Desserts.
- **User Interaction**: Customers can select items by number and specify quantities.
- **Quantity Input Validation**: Implemented checks to ensure that the quantity entered by the user is a positive integer. If the user enters an invalid quantity (like zero or a negative number), they are prompted to confirm if they want to proceed with a default quantity of 1.
User Confirmation for Quantity:
> After entering an invalid quantity, the program now asks the user if they would like to change their quantity before proceeding with the order.
- **Improved User Prompts**: Updated input prompts for clarity, removing references to default quantities in the prompt messages to enhance user experience.
- **Robust Error Handling:** Added checks for invalid selections and quantities, ensuring the program can handle user input more gracefully and avoid unexpected behavior.
- **Enhanced Code Readability:** Improved code structure and organization to enhance maintainability and readability.
- **Testing:** Verified that the program handles various edge cases correctly, such as invalid menu selections and quantity inputs.
- **Order Summary**: Receives a formatted receipt displaying item names, prices, quantities, and total cost.

3. ## Code Structure
- **Menu**: A nested dictionary that stores the categories, subcategories, and prices of the items available for order.
- **Order** List: The order is maintained in a list of dictionaries, each containing the item name, price, and quantity.
- **Receipt Display**: A well-structured receipt is generated that aligns the item names, prices, and quantities into neat columns.

4. ## Project Resources and Acknowledgments
* **Class Material** : All concepts and techniques used to build the ordering system were studied in the course, including how to work with -
dictionaries, loops, and input validation.
* **Menu Support File:** The menu dictionary, provided as a support file during the course, was used as the primary dataset for the project.
* **ChatGPT Assistance:** As an experienced data scientist, I used ChatGPT for help with syntax corrections and general optimizations. While the logic and structure of the project were independently developed, ChatGPT provided additional support to ensure clean and efficient code.

5. ## Conclusion
This Food Truck Ordering System project demonstrates practical applications of Python programming concepts like data structures, loops, and input validation. It satisfies all challenge requirements and delivers a functional, user-friendly ordering system.

---
> *Thank you for reviewing this project!*






