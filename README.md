# Services_API
# **Django Backend Services**

This project contains a Django-based backend with three key services: **Ride Booking**, **Room Booking**, and **Online Ordering**. Each service has been developed with multiple APIs to support the corresponding functionality. This guide will help you set up, run, and interact with the APIs.

## **Table of Contents**
1. [Project Setup](#project-setup)
2. [Running the Project](#running-the-project)
3. [API Documentation](#api-documentation)
   - [Ride Booking Service](#ride-booking-service)
   - [Room Booking Service](#room-booking-service)
   - [Online Ordering Service](#online-ordering-service)
4. [Testing the APIs](#testing-the-apis)
5. [Technologies Used](#technologies-used)

---

## **Project Setup**

### **Requirements:**
- Python 3.x
- Django 5.x (or version as specified in `requirements.txt`)
- Virtual environment (recommended)
- Postman or any API testing tool

### **Installation Steps:**
1. **Clone or copy the project folder** from the pen drive onto your system.

2. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

3. **Create a virtual environment** (recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # For Mac/Linux
   env\Scripts\activate  # For Windows
   ```

4. **Install project dependencies**:
   Ensure that you have `requirements.txt` in the root directory, and then run:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**:
   Apply the migrations to set up the database schema:
   ```bash
   python manage.py migrate
   ```

---

## **Running the Project**

1. **Start the Django development server**:
   ```bash
   python manage.py runserver
   ```

2. The server will run on `http://127.0.0.1:8000/` by default.

---

## **API Documentation**

### **Ride Booking Service**

**Endpoints:**
- **GET /ride_booking/rides/**: Retrieve a list of all available rides.
- **GET /ride_booking/bookings/**: Retrieve a list of all ride bookings.
- **POST /ride_booking/bookings/create/**: Create a new ride booking.
  - **Request Body (JSON)**:
    ```json
    {
      "user_id": 1,
      "ride_id": 1
    }
    ```
- **POST /ride_booking/bookings/cancel/<booking_id>/**: Cancel an existing booking.

**Models:**
- **Ride**: Contains fields like `pickup_location`, `destination`, `vehicle_type`, and `is_available`.
- **Booking**: Contains fields like `user_id`, `ride_id`, and `status` (booked/cancelled).

### **Room Booking Service**

**Endpoints:**
- **GET /room_booking/rooms/**: Retrieve a list of all available rooms.
- **GET /room_booking/bookings/**: Retrieve a list of all room bookings.
- **POST /room_booking/bookings/create/**: Create a new room booking.
  - **Request Body (JSON)**:
    ```json
    {
      "user_id": 1,
      "room_id": 1
    }
    ```
- **POST /room_booking/bookings/cancel/<booking_id>/**: Cancel an existing booking.

**Models:**
- **Room**: Contains fields like `room_number`, `room_type`, and `is_available`.
- **RoomBooking**: Contains fields like `user_id`, `room_id`, and `status` (booked/cancelled).

### **Online Ordering Service**

**Endpoints:**
- **GET /online_ordering/orders/**: Retrieve a list of all orders.
- **POST /online_ordering/orders/create/**: Create a new order.
  - **Request Body (JSON)**:
    ```json
    {
      "user_id": 1,
      "total_price": 100.00
    }
    ```
- **POST /online_ordering/orders/cancel/<order_id>/**: Cancel an existing order.

**Models:**
- **Order**: Contains fields like `user_id`, `total_price`, and `status` (ordered/cancelled).

---

## **Testing the APIs**

### **Using Postman**:
1. **Start the Django server**: 
   Make sure the server is running on `http://127.0.0.1:8000/`.

2. **Ride Booking APIs**:
   - **GET Rides**:
     - URL: `http://127.0.0.1:8000/ride_booking/rides/`
   - **POST Create Booking**:
     - URL: `http://127.0.0.1:8000/ride_booking/bookings/create/`
     - Method: POST
     - Body (JSON):
       ```json
       {
         "user_id": 1,
         "ride_id": 1
       }
       ```

3. **Room Booking APIs**:
   - **GET Rooms**:
     - URL: `http://127.0.0.1:8000/room_booking/rooms/`
   - **POST Create Room Booking**:
     - URL: `http://127.0.0.1:8000/room_booking/bookings/create/`
     - Method: POST
     - Body (JSON):
       ```json
       {
         "user_id": 1,
         "room_id": 1
       }
       ```

4. **Online Ordering APIs**:
   - **GET Orders**:
     - URL: `http://127.0.0.1:8000/online_ordering/orders/`
   - **POST Create Order**:
     - URL: `http://127.0.0.1:8000/online_ordering/orders/create/`
     - Method: POST
     - Body (JSON):
       ```json
       {
         "user_id": 1,
         "total_price": 100.00
       }
       ```

### **Responses:**
- Success response: `200 OK`
- Error responses (like `404 Not Found` or `400 Bad Request`) will return relevant error messages.

---

## **Technologies Used**
- **Django**: A high-level Python Web framework that encourages rapid development.
- **SQLite**: The default database used for development (can be switched to PostgreSQL or MySQL for production).
- **Postman**: For API testing and validation.

---

### **Contributors**
- Backend Developer: Arsh Tandon

---

### **Notes**
- Feel free to adjust the models and views if more specific functionality is needed.
- For more advanced features, consider adding pagination to list views or implementing JWT authentication for secure endpoints.

---
