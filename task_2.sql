CREATE TABLE Books
(
    book_id INT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id (Foreign Key referencing Authors table) NOT NULL,
    price DOUBLE NOT NULL,
    publication_date DATE
);
CREATE TABLE Authors
(
    author_id PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);
CREATE TABLE Customers
(
    customer_id (Primary Key),
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT NOT NULL
);
CREATE TABLE Orders
(
    order_id (Primary Key),
    customer_id INT,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
CREATE TABLE Order_Details
(
    orderdetailid (Primary Key),
    order_id INT,
    book_id INT,
    quantity DOUBLE,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
)