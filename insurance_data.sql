CREATE TABLE customers (
    CustomerID varchar(10) NOT NULL,
    FirstName varchar(100) NOT NULL,
    LastName varchar(100) NOT NULL,
    DOB date NOT NULL,
    Sex varchar(20),
    MaritalStatus varchar(50),
    EmailID varchar(255),
    PhoneNumber int,
    PRIMARY KEY (CustomerID)
);

INSERT INTO customers (CustomerID, FirstName, LastName, DOB, Sex, MaritalStatus, EmailID, PhoneNumber) 
VALUES ('001', 'James', 'McBrien', '1991-10-25', 'Male', 'Single', 'mcbrienjimmy25@gmail.com', 5326030085), 
       ('002', 'Mary', 'Bowes', '1983-01-17', 'Female', 'Married', 'mary_bowes83@gmail.com', 7392061752), 
       ('003', 'Brady', 'Andrew', '1996-03-03', 'Male', 'Married', 'iambradyandrew@gmail.com', 8094375617), 
       ('004', 'Monank', 'Yadav', '1977-04-30', 'Male', 'Married', 'monankjyadav@yahoo.com', 4069052853), 
       ('005', 'Lakshmi', 'Mohan', '1994-07-12', 'Female', 'Single', 'lakshmi.mohan_21@hotmail.com', 7395720561), 
       ('006', 'Destiny', 'Moh', '2001-06-08', 'Female', 'Single', 'tinydesmoh6801@gmail.com', 50568391064), 
       ('007', 'Jonathan', 'Davids', '1996-12-28', 'Male', 'Single', 'jodavids17@yahoo.com', 8409472610), 
       ('008', 'Lupita', 'Diaz', '1987-10-25', 'Female', 'Married', '.lupita.diaz@hotmail.com', 9018471505), 
       ('009', 'Syed', 'Zabiullah', '1991-08-15', 'Male', 'Single', 'zabiullah_syed@gmail.com', 9023861592), 
       ('010', 'Emmanuel', 'Kapoor', '2000-02-24', 'Male', 'Single', 'emmanuellll@gmail.com', 5400481739),  
       ('011', 'Max', 'Johnson', '2001-11-30', 'Male', 'Single', 'max_johnson@gmail.com', 5049538207), 
       ('012', 'Leandre', 'Davies', '1977-05-05', 'Male', 'Married', 'leandrefdavies@yahoo.com', 9904582169), 
       ('013', 'Rebecca', 'Thomas', '1984-05-25', 'Female', 'Single', 'rebsythomas321@yahoo.com', 6749302841), 
       ('014', 'Alan', 'Chen', '2004-06-18', 'Male', 'Single', 'thealanchen0618@hotmail.com', 7335693321), 
       ('015', 'Hope', 'Nguyen', '2000-12-02', 'Female', 'Single', 'hopeistheway2@gmail.com', 7074488142), 
       ('016', 'Diana', 'White', '1966-10-13', 'Female', 'Divorced', 'dwhite12345@yahoo.com', 6063994152), 
       ('017', 'Grace', 'Mitchell', '1968-09-20', 'Female', 'Widowed', 'gracykolfman@hotmail.com', 2110509637), 
       ('018', 'Abdullah', 'Shafique', '1996-04-21', 'Male', 'Single', 'abdullahpshafique@gmail.com', 8543122228), 
       ('019', 'Daniel', 'Abrams', '2004-02-29', 'Male', 'Single', 'iamdannyabes@gmail.com', 9007427741), 
       ('020', 'Laura', 'Johnson', '1944-01-15', 'Female', 'Married', 'donna.johnson@gmail.com', 7668481210);
ALTER TABLE customers
     MODIFY COLUMN PhoneNumber BIGINT;


CREATE TABLE PolicyDetail (
    PolicyNumber VARCHAR(10) PRIMARY KEY,
    CustomerID VARCHAR(10) REFERENCES customers(CustomerID),
    PolicyStatus VARCHAR(20) REFERENCES PolicyStatus(StatusName),
    Type VARCHAR(20),
    Number INT,
    CarrierName VARCHAR(50)
);

INSERT INTO PolicyDetail (PolicyNumber, CustomerID, Type, CarrierName, PolicyStatus)
VALUES 
    ('001', '001', 'auto', 'Safeco', 'Active'),
    ('0001', '002', 'home', 'Nationwide', 'Active'),
    ('00001', '003', 'umbrella', 'Farmers', 'Active'),
    ('002', '004', 'auto', 'National General', 'Active'),
    ('0002', '005', 'home', 'CSE', 'Active'),
    ('00002', '006', 'umbrella', 'Safeco', 'Active'),
    ('003', '007', 'auto', 'Nationwide', 'Active'),
    ('0003', '008', 'home', 'Farmers', 'Active'),
    ('00003', '009', 'umbrella', 'National General', 'Active'),
    ('004', '010', 'auto', 'CSE', 'Active'),
    ('0004', '011', 'home', 'Safeco', 'Active'),
    ('00004', '012', 'umbrella', 'Nationwide', 'Active'),
    ('005', '013', 'auto', 'Farmers', 'Active'),
    ('0005', '014', 'home', 'National General', 'Active'),
    ('00005', '015', 'umbrella', 'CSE', 'Active'),
    ('006', '016', 'auto', 'Safeco', 'Active'),
    ('0006', '017', 'home', 'Nationwide', 'Active'),
    ('00006', '018', 'umbrella', 'Farmers', 'Active'),
    ('007', '019', 'auto', 'National General', 'Active'),
    ('0007', '020', 'home', 'CSE', 'Active');

CREATE TABLE Carrier (
    CarrierID VARCHAR(9) PRIMARY KEY,
    CarrierName VARCHAR(50),
    Logo VARCHAR(500), 
    MailingLocation VARCHAR(100)
);

INSERT INTO Carrier (CarrierID, CarrierName, Logo, MailingLocation)
VALUES 
    ('123456789', 'Safeco', 'https://www.creativefabrica.com/wp-content/uploads/2023/02/07/Car-under-umbrella-Automobile-insurance-Graphics-60331247-1-1-580x387.png', '123 Main St, Seattle, WA'),
    ('234567890', 'Nationwide', 'https://www.eliteinsuranceservicesinc.com/wp-content/uploads/2017/10/um-1.png', '456 Elm St, Columbus, OH'),
    ('345678901', 'CSE', 'https://www.hsip.com/sites/default/files/2023-06/umbrella-insurance-hero.jpg', '789 Oak St, San Diego, CA'),
    ('456789012', 'Farmers', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVOYxR_yGtNzwlhrngbHXE1DgvhekSNxgRQLc4IvyuZA&s', '567 Pine St, Los Angeles, CA'),
    ('567890123', 'National General', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTF1AqmbHe7VrcY4GK51EkRVKHn0uG7jfHZKf3FL0E7nw&s', '890 Maple St, New York, NY');

CREATE TABLE PolicyStatus (
    StatusID INT PRIMARY KEY,
    StatusName VARCHAR(20)
);

INSERT INTO PolicyStatus (StatusID, StatusName)
VALUES
    (1, 'Active'),
    (2, 'Inactive'),
    (3, 'Cancelled');

ALTER TABLE PolicyStatus
    ADD INDEX StatusName_index (StatusName);


CREATE TABLE Premiums (
     PremiumID INT PRIMARY KEY,
     PolicyNumber VARCHAR(50),
     CustomerID VARCHAR(10),
     PremiumAmount DECIMAL(10, 2),
     PremiumDueDate DATE,
     PaymentStatus VARCHAR(20),
     PolicyType VARCHAR(50),
     StatusName VARCHAR(20),
     FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID),
     FOREIGN KEY (PolicyNumber) REFERENCES PolicyDetail(PolicyNumber),
     FOREIGN KEY (StatusName) REFERENCES PolicyStatus(StatusName)
     );


INSERT INTO Premiums (PremiumID, PolicyNumber, CustomerID, PremiumAmount, PremiumDueDate, PaymentStatus, PolicyType, StatusName)
    VALUES
    (1, '001', '001', 500.00, '2024-04-30', 'Paid', 'auto', 'Active'),
    (2, '0001', '002', 700.00, '2024-05-15', 'Unpaid', 'home', 'Active'),
    (3, '00001', '003', 300.00, '2024-05-20', 'Paid', 'umbrella', 'Active'),
    (4, '002', '004', 550.00, '2024-04-25', 'Paid', 'auto', 'Active'),
    (5, '0002', '005', 800.00, '2024-05-10', 'Unpaid', 'home', 'Active'),
    (6, '00002', '006', 400.00, '2024-05-05', 'Paid', 'umbrella', 'Active'),
    (7, '003', '007', 600.00, '2024-04-28', 'Paid', 'auto', 'Active'),
    (8, '0003', '008', 750.00, '2024-05-12', 'Unpaid', 'home', 'Active'),
    (9, '00003', '009', 350.00, '2024-05-18', 'Paid', 'umbrella', 'Active'),
    (10, '004', '010', 600.00, '2024-04-27', 'Paid', 'auto', 'Active'),
    (11, '0004', '011', 850.00, '2024-05-08', 'Unpaid', 'home', 'Active'),
    (12, '00004', '012', 450.00, '2024-05-22', 'Paid', 'umbrella', 'Active'),
    (13, '005', '013', 700.00, '2024-04-29', 'Paid', 'auto', 'Active'),
    (14, '0005', '014', 900.00, '2024-05-18', 'Unpaid', 'home', 'Active'),
    (15, '00005', '015', 500.00, '2024-05-25', 'Paid', 'umbrella', 'Active'),
    (16, '006', '016', 550.00, '2024-04-26', 'Paid', 'auto', 'Active'),
    (17, '0006', '017', 750.00, '2024-05-14', 'Unpaid', 'home', 'Active'),
    (18, '00006', '018', 350.00, '2024-05-16', 'Paid', 'umbrella', 'Active'),
    (19, '007', '019', 600.00, '2024-04-28', 'Paid', 'auto', 'Active'),
    (20, '0007', '020', 800.00, '2024-05-11', 'Unpaid', 'home', 'Active');
