# ajay_habotconnect

# Employee Management API
This API provides CRUD functionality to manage employees within a company. It follows RESTful principles and includes token-based authentication to secure endpoints.
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ajay7605/ajay_habotconnect
   cd employee_management
## Setup Instructions
pip install -r requirements.txt
2. python manage.py migrate
3.python manage.py createsuperuser

## Authentication
1. Obtain a token by sending a POST request with your credentials:
   ex:
POST /api/auth/
{
  "username": "testuser",
  "password": "testpassword"
}

## Endpoints Documentation


## Endpoints

### 1. Create Employee
- **URL**: `/api/employees/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "Ajay",
    "email": "ajay@gmail.com",
    "department": "HR",
    "role": "Manager"
  }
  
##  List Employees

URL: /api/employees/
Method: GET
Query Parameters:
department (optional): Filter by department.
role (optional): Filter by role.
page (optional): Pagination page number

## Filtering and Pagination

- Use `?department=<department_name>` or `?role=<role_name>` for filtering.
- Add `?page=<page_number>` to navigate through pages of results (10 items per page).

## Testing

To run all tests:

```bash
python manage.py test


---

### **Step 2: Prepare Authentication Demo**

#### 2.1 **Token Generation**:
- Using Postman or a command-line tool like `curl`, demonstrate getting a token:
  ```bash
  POST http://localhost:8000/api/auth/
  Content-Type: application/json

  {
    "username": "testuser",
    "password": "testpassword"
  }
  ```
- This will return a token that looks like:
  ```json
  {
    "token": "your_generated_token_here"
  }
  ```

#### 2.2 **Use Token in Requests**:
- To access endpoints securely, add `Authorization: Token <your_token>` to each request’s header. In Postman, go to the Authorization tab, select "Token" as the type, and paste the token.

---
