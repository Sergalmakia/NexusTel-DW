CREATE DATABASE nexustel_dw;
USE nexustel_dw;
CREATE TABLE staging_crm (
    customer_id VARCHAR(20),
    full_name VARCHAR(100),
    gender VARCHAR(10),
    age INT,
    region VARCHAR(50),
    subscription_type VARCHAR(50),
    registration_date DATE,
    customer_status VARCHAR(20),
    customer_segment VARCHAR(50)
);
CREATE TABLE staging_billing (
    invoice_id VARCHAR(20),
    customer_id VARCHAR(20),
    billing_date DATE,
    payment_date DATE,
    amount_paid DECIMAL(10,2),
    payment_method VARCHAR(50),
    service_type VARCHAR(50),
    invoice_status VARCHAR(20)
);
CREATE TABLE staging_usage (
    usage_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id VARCHAR(20),
    usage_date DATE,
    data_usage_mb DECIMAL(10,2),
    call_duration_minutes DECIMAL(10,2),
    sms_count INT,
    internet_sessions INT,
    dropped_calls INT,
    network_region VARCHAR(50),
    connection_type VARCHAR(50)
);
CREATE TABLE Dim_Customer (
    customer_key INT AUTO_INCREMENT PRIMARY KEY,
    customer_id VARCHAR(20),
    full_name VARCHAR(100),
    gender VARCHAR(10),
    age INT,
    region VARCHAR(50),
    subscription_type VARCHAR(50),
    customer_status VARCHAR(20),
    customer_segment VARCHAR(50),

    start_date DATE,
    end_date DATE,
    is_current BOOLEAN
);
CREATE TABLE Dim_Time (
    time_key INT AUTO_INCREMENT PRIMARY KEY,
    full_date DATE,
    day INT,
    month INT,
    quarter_num INT,
    year INT,
    month_name VARCHAR(20)
);
CREATE TABLE Dim_Service (
    service_key INT AUTO_INCREMENT PRIMARY KEY,
    service_type VARCHAR(50)
);
CREATE TABLE Dim_Region (
    region_key INT AUTO_INCREMENT PRIMARY KEY,
    region_name VARCHAR(50)
);
CREATE TABLE Dim_Subscription (
    subscription_key INT AUTO_INCREMENT PRIMARY KEY,
    subscription_type VARCHAR(50)
);
CREATE TABLE Dim_Payment_Method (
    payment_method_key INT AUTO_INCREMENT PRIMARY KEY,
    payment_method VARCHAR(50)
);
CREATE TABLE Fact_Billing (
    billing_key INT AUTO_INCREMENT PRIMARY KEY,

    customer_key INT,
    time_key INT,
    payment_method_key INT,
    service_key INT,

    amount_paid DECIMAL(10,2),

    FOREIGN KEY (customer_key)
        REFERENCES Dim_Customer(customer_key),

    FOREIGN KEY (time_key)
        REFERENCES Dim_Time(time_key),

    FOREIGN KEY (payment_method_key)
        REFERENCES Dim_Payment_Method(payment_method_key),

    FOREIGN KEY (service_key)
        REFERENCES Dim_Service(service_key)
);
CREATE TABLE Fact_Usage (
    usage_key INT AUTO_INCREMENT PRIMARY KEY,

    customer_key INT,
    time_key INT,
    region_key INT,

    data_usage_mb DECIMAL(10,2),
    call_duration_minutes DECIMAL(10,2),
    sms_count INT,
    internet_sessions INT,
    dropped_calls INT,

    FOREIGN KEY (customer_key)
        REFERENCES Dim_Customer(customer_key),

    FOREIGN KEY (time_key)
        REFERENCES Dim_Time(time_key),

    FOREIGN KEY (region_key)
        REFERENCES Dim_Region(region_key)
);
CREATE TABLE Fact_Payments (
    payment_key INT AUTO_INCREMENT PRIMARY KEY,

    customer_key INT,
    time_key INT,
    payment_method_key INT,

    amount_paid DECIMAL(10,2),

    FOREIGN KEY (customer_key)
        REFERENCES Dim_Customer(customer_key),

    FOREIGN KEY (time_key)
        REFERENCES Dim_Time(time_key),

    FOREIGN KEY (payment_method_key)
        REFERENCES Dim_Payment_Method(payment_method_key)
);
CREATE TABLE error_crm (
    error_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id VARCHAR(20),
    error_reason VARCHAR(255)
);
CREATE TABLE error_billing (
    error_id INT AUTO_INCREMENT PRIMARY KEY,
    invoice_id VARCHAR(20),
    error_reason VARCHAR(255)
);
CREATE TABLE error_usage (
    error_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id VARCHAR(20),
    error_reason VARCHAR(255)
);