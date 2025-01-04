This GitHub project is a Library Registration App. It allows users to register for the library and borrow books. It is focused on the backend only. The project design is set to Clean Architecture.

## **Key Features:**
- User registration for the library
- Book borrowing functionality
- Management of book borrowing processes

## **Technology Stack:**
- Flask: Web application framework
- SQLAlchemy: Database management
- ORM: Object-Relational Mapping
- PostgreSQL: Database system

# **API Endpoints:**

**Users:**
- Get All: GET /user
- Get By Id: GET /user/id
- Update: PATCH /user/update

**Loans:**
- Get All: GET /loan
- Get By Id: GET /loan/id
- Get By User Id: GET /loan/user-id
- Get By Book Id: GET /loan/book-id
- Add: POST /loan/add
- Delete: DELETE /loan/delete
- Update: PATCH /loan/update

**Categories:**
- Get All: GET /category
- Get By Id: GET /category/id
- Search: GET /category/search
- Add: POST /category/add
- Delete: DELETE /category/delete

**Books:**
- Get All: GET /book
- Get By Id: GET /book/id
- Search: GET /book/search
- Add: POST /book/add
- Delete: DELETE /book/delete

**Authors:**
- Get All: GET /author
- Get By Id: GET /author/id
- Search: GET /author/search
- Add: POST /author/add
- Delete: DELETE /author/delete

**Auth:**
- Register: POST /auth/register
- Login: POST /auth/login


# **Database:**

![libraryapperd](https://github.com/user-attachments/assets/d3a3d399-2204-4cd8-a0e2-84e417c70b47)

