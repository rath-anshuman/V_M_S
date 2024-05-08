# Vendor Management System with Performance Metrics

## Installation

To run this system locally, follow these steps:

1. Clone the repository:
   git clone [https://github.com/rath-anshuman/V_M_S](https://github.com/rath-anshuman/V_M_S)
2. Navigate to the project directory : cd V_M_S
3. Install dependencies : pip install -r requirements.txt
4. Start the development server in root cmd : python manage.py runserver
5. Access the API at `http://localhost:8000/`.
6. To access the admin panel, go to `http://localhost:8000/admin`.

- **Username:** a
- **Password:** a

## API Endpoints

### Vendor Profile Management

**API Endpoints**:

- **POST /api/vendors/**: Create a new vendor.
- **GET /api/vendors/**: List all vendors.
- **GET /api/vendors/{vendor_id}/**: Retrieve a specific vendor's details.
- **PUT /api/vendors/{vendor_id}/**: Update a vendor's details.
- **DELETE /api/vendors/{vendor_id}/**: Delete a vendor.
- **GET /api/vendors/{vendor_id}/performance/:** calculated performance metrics

### Purchase Order Tracking

**API Endpoints**:

- **POST /api/purchase_orders/**: Create a purchase order.
- **GET /api/purchase_orders/**: List all purchase orders with an option to filter by vendor.
- **GET /api/purchase_orders/{po_id}/**: Retrieve details of a specific purchase order.
- **PUT /api/purchase_orders/{po_id}/**: Update a purchase order.
- **DELETE /api/purchase_orders/{po_id}/**: Delete a purchase order.
- **POST /api/purchase_orders/{po_id}/acknowledge/:** vendors to acknowledge
  POs.

### Vendor Performance Evaluation

**Metrics**:

- **On-Time Delivery Rate**: Percentage of orders delivered by the promised date.
- **Quality Rating**: Average of quality ratings given to a vendor’s purchase orders.
- **Response Time**: Average time taken by a vendor to acknowledge or respond to purchase orders.
- **Fulfilment Rate**: Percentage of purchase orders fulfilled without issues.

**Model Design**: Fields are added to the vendor model to store these performance metrics.

**API Endpoints**:

- **GET /api/vendors/{vendor_id}/performance**: Retrieve a vendor's performance metrics.

## Usage

- Use the provided API endpoints with appropriate HTTP methods (POST, GET, PUT, DELETE) to interact with the system.
- Utilize filters and query parameters where necessary for efficient data retrieval.

## API Testing with Postman and Thunder Client

### Postman:

1. **Install Postman**: Download and install Postman from the [official website](https://www.postman.com/downloads/).
2. **Create a Request**:

   - Open Postman and click on the "New" button to create a new request.
   - Choose the HTTP method (GET, POST, PUT, DELETE, etc.) from the dropdown menu.
   - Enter the request URL in the address bar.
   - Add headers, parameters, request body (if applicable), and any other required information.
3. **Send the Request**:

   - Click on the "Send" button to send the request.
   - Postman will display the response, including status code, headers, and body.
4. **Test Different Scenarios**:

   - Utilize Postman's features like environments, variables, and collections to organize and streamline your testing process.
   - Test different scenarios by modifying request parameters, headers, or body.

### Thunder Client (VS Code Extension):

1. **Install Thunder Client**: If you're using Visual Studio Code, you can install the Thunder Client extension from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client).
2. **Create a Request**:

   - Open Thunder Client from the sidebar.
   - Click on the "New Request" button.
   - Enter the request URL and choose the HTTP method.
3. **Send the Request**:

   - Click on the "Send Request" button to send the request.
   - Thunder Client will display the response in a separate pane.
4. **View Response**:

   - Thunder Client provides options to view the response in different formats (Raw, Pretty, Parsed).
5. **Test Different Scenarios**:

   - Similar to Postman, you can test different scenarios by modifying request parameters, headers, or body directly in Thunder Client.

## Additional Information

- The system comes preloaded with10 vendors and40 purchase orders data for testing purposes.

## Contributors

- [Anshuman Rath](https://github.com/anish-anshuman)
