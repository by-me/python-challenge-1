# Food Truck Ordering System

**Tabel of Contents:**
1. [Overview](#overview) 
2. [Features](#features)
3. [code tructure](#code-structure)
4. [Project Resouces and Acknowledgments](#project-resources-and-acknowledgments)
5. [Conclusion](#conclusion)

## 1. Overview

This project implements an interactive ordering system for a food truck. Customers can select items from a categorized menu, specify quantities, and receive a detailed receipt with the total cost of their order. The system is built using Python, demonstrating key programming concepts such as dictionaries, lists, input validation, loops, and formatted output.

## 2. Features

- **Categorized Menu**: The menu is organized into Snacks, Meals, Drinks, and Desserts.
- **User Interaction**: Customers can select items by number and specify the quantity.
- **Quantity Input Validation**: Ensures the quantity entered by the user is a positive integer. If an invalid quantity is entered, a default quantity of 1 is used.
- **User Confirmation for Quantity**: After an invalid quantity input, the system asks the user if they'd like to adjust the quantity before proceeding with the order.
- **Improved User Prompts**: Input prompts have been updated for better clarity, avoiding confusion with default values.
- **Robust Error Handling**: Prevents invalid menu selections and quantities, making the system more user-friendly.
- **Enhanced Code Readability**: The code is structured clearly for easy maintenance and scalability.
- **Order Summary**: Displays a formatted receipt, including item names, prices, quantities, and total cost.


## 3. Code Structure
- **Menu**: A nested dictionary that stores the categories, subcategories, and prices of the items available for order.
- **Order** List: The order is maintained in a list of dictionaries, each containing the item name, price, and quantity.
- **Receipt Display**: A well-structured receipt is generated that aligns the item names, prices, and quantities into neat columns.

## 4. Project Resources and Acknowledgments

- **Class Material**: This project builds on concepts learned in class, such as working with dictionaries, loops, and input validation.
- **Menu Data**: The menu dictionary was provided as part of the course materials and used as the dataset for this project.
- **ChatGPT Assistance**: While I developed the core logic and structure of the project, ChatGPT was instrumental in resolving syntax errors and optimizing code readability.


##  5. Conclusion
This Food Truck Ordering System project demonstrates practical applications of Python programming concepts like data structures, loops, and input validation. It satisfies all challenge requirements and delivers a functional, user-friendly ordering system.

---
> *Thank you for reviewing this project!*

