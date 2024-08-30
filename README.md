# Linktic Bookstore Module

Manage books, authors, and customers in a bookstore.

Configuration
=============
No additional configurations needed.


Credits
-------

* Developer : (V17) Jhon Garcia
  Contact: ggja23@gmail.com

## Overview

The **Linktic Bookstore** module is a custom Odoo solution for managing bookstores. It allows the management of authors,
books, customers, and sales orders.

## Installation

### Prerequisites

- Odoo 17 installed.
- Administrator access to an Odoo environment (development).

### Installation Steps

1. **Download the Module**:
    - Clone or download the module into the Odoo addons folder.

2. **Update Module List**:
    - Switch to developer mode in Odoo.
    - Go to **Apps** and click on **Update Apps List**.

3. **Install the Module**:
    - Search for "Linktic Bookstore" in the available apps list.
    - Click on **Install**.

## Initial Setup

1. **Sequences**:
    - The module automatically generates unique sequences for Sale Orders.

2. **Security Groups**:
    - Three security groups are created:
        - **Linktic Internal User**: Basic access to all module functionalities.
        - **Linktic Sales Manager**: Sales management and access to sales reports.
        - **Linktic Inventory Manager**: Management of inventory and products.

3. **Initial Data Configuration**:
    - Create authors, books, and customers from the respective menus under the **Linktic Bookstore** tab.

## Usage

### Managing Books and Authors

- **Create Authors**: Navigate to **Linktic Bookstore > Authors** to create new authors, specifying their names and
  biographies.
- **Create Books**: Navigate to **Linktic Bookstore > Books** to create books, associating them with authors, setting
  prices, and managing available stock.

### Managing Customers and Sales Orders

- **Create Customers**: Navigate to **Linktic Bookstore > Customers** to register new customers and their contact
  details.
- **Create Sales Orders**: Navigate to **Linktic Bookstore > Sales Orders** to record new customer orders, selecting
  books and the requested quantities.

### CRM Functionalities

- The module automatically logs each customer's purchases, allowing you to track their buying habits.

### Dashboard

- Access the **Dashboard** from the main **Linktic Bookstore** menu to view a summary of stock levels, recent sales, and
  other key metrics.

