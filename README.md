# **Django Backend Services**

This repository contains a Django-based backend for three key services: **Ride Booking**, **Room Booking**, and **Online Ordering**. Each service has its own set of APIs to support respective functionality. This README will guide you through setting up the project, running it, and interacting with the APIs.

## **Table of Contents**
1. [Project Setup](#project-setup)
2. [Running the Project](#running-the-project)
3. [API Documentation](#api-documentation)
   - [Ride Booking Service](#ride-booking-service)
   - [Room Booking Service](#room-booking-service)
   - [Online Ordering Service](#online-ordering-service)
4. [Testing the APIs](#testing-the-apis)
5. [Technologies Used](#technologies-used)
6. [Contributors](#contributors)

---

## **Project Setup**

### **Requirements:**
- Python 3.x
- Django 5.x (or as specified in `requirements.txt`)
- Virtual environment (recommended)
- API testing tool (Postman, Insomnia, etc.)

### **Installation Steps:**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/<your-username>/django-backend-services.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd django-backend-services
   ```

3. **Create a virtual environment:**

   ```bash
   python -m venv env
   ```

4. **Activate the virtual environment:**

   - For macOS/Linux:
     ```bash
     source env/bin/activate
     ```
   - For Windows:
     ```bash
     env\Scripts\activate
     ```

5. **Install project dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Run migrations to set up the database schema:**

   ```bash
   python manage.py migrate
   ```

---

## **Running the Project**

1. **Start the Django development server:**

   ```bash
   python manage.py runserver
   ```

2. The project will now be running at `http://127.0.0.1:8000/`.

---

## **API Documentation**

### **Ride Booking Service**

- **GET /ride_booking/rides/**: Retrieve a list of all available rides.
- **GET /ride_booking/bookings/**: Retrieve a list of all ride bookings.
- **POST /ride_booking/bookings/create/**: Create a new ride booking.
  - **Request Body (JSON):**
    ```json
    {
      "user_id": 1,
      "ride_id": 1
    }
    ```
- **POST /ride_booking/bookings/cancel/<booking_id>/**: Cancel an existing ride booking.

**Models:**
- **Ride:** Contains fields such as `pickup_location`, `destination`, `vehicle_type`, and `is_available`.
- **Booking:** Contains fields like `user_id`, `ride`, and `status` (booked/cancelled).

### **Room Booking Service**

- **GET /room_booking/rooms/**: Retrieve a list of all available rooms.
- **GET /room_booking/bookings/**: Retrieve a list of all room bookings.
- **POST /room_booking/bookings/create/**: Create a new room booking.
  - **Request Body (JSON):**
    ```json
    {
      "user_id": 1,
      "room_id": 1
    }
    ```
- **POST /room_booking/bookings/cancel/<booking_id>/**: Cancel an existing room booking.

**Models:**
- **Room:** Contains fields like `room_number`, `room_type`, and `is_available`.
- **RoomBooking:** Contains fields like `user_id`, `room`, and `status` (booked/cancelled).

### **Online Ordering Service**

- **GET /online_ordering/orders/**: Retrieve a list of all orders.
- **POST /online_ordering/orders/create/**: Create a new order.
  - **Request Body (JSON):**
    ```json
    {
      "user_id": 1,
      "total_price": 100.00
    }
    ```
- **POST /online_ordering/orders/cancel/<order_id>/**: Cancel an existing order.

**Models:**
- **Order:** Contains fields like `user_id`, `total_price`, and `status` (ordered/cancelled).

---

## **Testing the APIs**

### **Using Postman:**

1. **Start the Django server:**

   Ensure that the server is running at `http://127.0.0.1:8000/`.

2. **Testing the Ride Booking APIs:**
   - **GET Rides:**
     - URL: `http://127.0.0.1:8000/ride_booking/rides/`
   - **POST Create Booking:**
     - URL: `http://127.0.0.1:8000/ride_booking/bookings/create/`
     - Method: POST
     - Body (JSON):
       ```json
       {
         "user_id": 1,
         "ride_id": 1
       }
       ```

3. **Testing the Room Booking APIs:**
   - **GET Rooms:**
     - URL: `http://127.0.0.1:8000/room_booking/rooms/`
   - **POST Create Room Booking:**
     - URL: `http://127.0.0.1:8000/room_booking/bookings/create/`
     - Method: POST
     - Body (JSON):
       ```json
       {
         "user_id": 1,
         "room_id": 1
       }
       ```

4. **Testing the Online Ordering APIs:**
   - **GET Orders:**
     - URL: `http://127.0.0.1:8000/online_ordering/orders/`
   - **POST Create Order:**
     - URL: `http://127.0.0.1:8000/online_ordering/orders/create/`
     - Method: POST
     - Body (JSON):
       ```json
       {
         "user_id": 1,
         "total_price": 100.00
       }
       ```

---

## **Technologies Used**

- **Django**: A high-level Python web framework for rapid development.
- **SQLite**: The default database used for development.
- **Postman**: For API testing and validation.

---

## **Contributors**

- Backend Developer: Arsh Tandon

