-- Câu 2: Viết lệnh và thực thi việc thống kê tổng doanh số bán hàng của các mặt hàng do khách hàng mua
SELECT 
    c.CustomerID,
    c.FirstName,
    c.LastName,
    SUM(od.OrderQty * od.UnitPrice) AS TotalSales
FROM orders o
JOIN orderdetails od ON o.OrderID = od.OrderID
JOIN customer c ON o.CustomerID = c.CustomerID
GROUP BY c.CustomerID, c.FirstName, c.LastName
ORDER BY TotalSales DESC;

-- Câu 3: Thống kê tổng doanh thu theo từng danh mục
SELECT 
    c.Name AS CategoryName,
    SUM(od.OrderQty * od.UnitPrice) AS TotalRevenue
FROM orderdetails od
JOIN product p ON od.ProductID = p.ProductID
JOIN subcategory sc ON p.ProductSubcategoryID = sc.SubcategoryID
JOIN category c ON sc.CategoryID = c.CategoryID
GROUP BY c.Name
ORDER BY TotalRevenue DESC;

-- Câu 4: Thống kê tổng doanh thu theo danh mục, phân theo Tháng + Năm
SELECT 
    c.Name AS CategoryName, 
    DATE_FORMAT(STR_TO_DATE(o.OrderDate, '%d/%m/%Y'), '%Y') AS Year, 
    DATE_FORMAT(STR_TO_DATE(o.OrderDate, '%d/%m/%Y'), '%m') AS Month, 
    SUM(od.OrderQty * od.UnitPrice) AS TotalRevenue
FROM orderdetails od
JOIN orders o ON od.OrderID = o.OrderID
JOIN product p ON od.ProductID = p.ProductID
JOIN subcategory s ON p.ProductSubcategoryID = s.SubcategoryID
JOIN category c ON s.CategoryID = c.CategoryID
GROUP BY c.Name, Year, Month
ORDER BY Year, Month;

-- Câu 5: Thống kê các đơn hàng được giao nhanh trước hạn từ 3 ngày trở lên
SELECT 
    OrderID, 
    STR_TO_DATE(OrderDate, '%d/%m/%Y') AS OrderDate, 
    STR_TO_DATE(DueDate, '%d/%m/%Y') AS DueDate, 
    STR_TO_DATE(ShipDate, '%d/%m/%Y') AS ShipDate,
    DATEDIFF(STR_TO_DATE(DueDate, '%d/%m/%Y'), STR_TO_DATE(ShipDate, '%d/%m/%Y')) AS DaysEarly
FROM orders
WHERE 
    ShipDate IS NOT NULL AND ShipDate <> ''
    AND DueDate IS NOT NULL AND DueDate <> ''
    AND DATEDIFF(STR_TO_DATE(DueDate, '%d/%m/%Y'), STR_TO_DATE(ShipDate, '%d/%m/%Y')) >= 3
ORDER BY DaysEarly DESC;










