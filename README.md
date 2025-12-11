 Inventory & Order Fulfillment API (Backend Capstone Project)

Project Overview

This repository contains the backend implementation for a comprehensive **Inventory and Order Fulfillment API. The system is designed to manage product stock, handle user authentication, and process secure sales orders, ensuring transactional integrity.

 Core Features

User Management:Secure registration and login for users.
Role-Based Access Control (RBAC): Restrict inventory creation and updates to Admin users only.
Inventory Management: CRUD operations for products, including tracking `stock_quantity`.
Order Processing: Transactional creation of orders that automatically decrement product stock.
Reporting:Admin access to view all historical orders.

Technology Stack

Backend Framework Django [e.g., 5.0.x] 
API Framework Django REST Framework (DRF) [e.g., Latest]
Language  Python [e.g., 3.10+] 
Database SQLite (Development)  PostgreSQL (Production target)

 Getting Started

 Prerequisites

1.  Python installed (3.8 or higher)
2.  pip and venv installed.


 Project Structure

The project uses a clear separation of concerns with three Django apps:
users Handles the custom User model and authentication (login/register).
inventory Manages the Product model and inventory-specific endpoints.
orders Manages the Order and OrderItem models and transactional fulfillment logic.
backend The main project configuration (settings, main URLs).
