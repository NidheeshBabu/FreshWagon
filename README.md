# FreshWagon
Online Supermarket Website

<h1>Software Specification</h1>
<h5>Front End:	HTML, JS, CSS, jQuery</h5>
<h5>Server Software:	Python</h5>
<h5>Framework:	Django</h5>
<h5>Back End:	MySQL</h5>

<h1>Modules<h1>
<ul>
<li>admin</li>
<li>staff</li>
<li>customer</li>
<li>public</li>
</ul>
<h3>ADMIN</h3>
<p>
Administrator or admin has total control over the application. Admin login by his username and password.Admin has the following responsibilities:
</p>
<ul>
<li>Staff Management</li>
<li>Product Category Mangement</li>
<li>Product Management</li>
<li>Sales & stock reports</li>
<li>View Complaints</li>
</ul>
<p>
Admin can appoint staffs by entering staff details and also can remove or change existing staffs. Admin can manage product categories; product category management includes adding product categories and removing product categories. Admin can also add products under each category that is previously added. Product management includes adding new products, removing and editing existing products. Admin has the access to sales and stock reports. Sales reports are concentrated on the total sales revenue in a specified period. Admin can filter the sales by monthly daily or by specifying specific date intervals. Stock reports are concentrated on the current inventory information. Stock reports makes the inventory management process easy and efficient. Stocks can be filtered among specific categories. Only Admin has the access to view the complaints raised by customers. Admin can resolve these issues which in turn increase the customer satisfaction.
</p>
<br><br>
<h3>STAFF</h3>
<p>
Staff is appointed by admin. Staff can login with the provided username and password.
	Staff has following responsibilities:

</p>
<ul>
<li>Stock Management</li>
<ul>
<li>Add Stock</li>
<li>Update Stock</li>
<li>Generate Purchase Order</li>
</ul>
<li>Order Proccessing</li>
<ul>
<li>View Orders</li>
<li>Check Payment</li>
<li>Deliver Products</li>
</ul>
</ul>
<p>
Staff has two main responsibilities, Stock Management and Order Processing. Stock management includes adding stock details of the products, updating the stock details of the existing products and generating purchase orders of the products which has current stock less than re-order level.

Order processing includes viewing the latest orders submitted by customers, checking the payment done by the customers as part of ordering, and finally delivering products to the specified customer using the provided details.
</p>
<br><br>
<h3>CUSTOMER</h3>
<ul>
<li>Search Products</li>
<li>Select Products</li>
<li>Check Bill</li>
<li>Make Payment</li>
<li>Order Products</li>
<li>View Order Status</li>
<li>Generate Complaints</li>
<li>Give Review</li>
</ul>

<p>
Customers have large range of functionalities. First one is searching products using the search bar. Instead of searching customer can also select products by viewing product categories. Customer can add products to cart by selecting the required quantity. After adding the required products in cart customer can check the bill details and make payment for the bill amount. After the payment order is placed.
Customers can review every product, also customers can generate complaints about the service or product quality.

</p>

<br><br>
<h3>PUBLIC</h3>

<ul>
<li>Search Product</li>
<li>View Review</li>
<li>Customer Registration</li>
</ul>
<p>
Public can search products and view products through the category list. Public can register for a new account and can continue as a customer.
</p>

