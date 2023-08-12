<!DOCTYPE html>
<html>

<body>

<h1>Ecommerce Web Application</h1>

<h2>Project Screenshots</h2>

<img width="400" alt="Screenshot 1" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/ef2fb936-2b43-42d7-b85b-b73e3fdbe6b6">
<img width="600" alt="Screenshot 2" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/5371c728-8433-454d-b1af-98c2e0aedcdc">
<img width="877" alt="Screenshot 3" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/39c0978f-ef50-44cd-a340-2b24e5b11ad9">
<img width="863" alt="Screenshot 4" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/9569c1cb-b58d-4aa7-a799-a85314e4b1ce">
<img width="915" alt="Screenshot 5" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/68932236-ed07-4ac7-b07a-8ec34ca3e707">
<img width="864" alt="Screenshot 6" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/28a8fda6-bd40-477f-88b8-55d4b21729cb">
<img width="692" alt="Screenshot 7" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/536fb8cb-7042-4483-92b6-f9ebad98f343">
<img width="863" alt="Screenshot 8" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/efbb3b76-bb85-423c-8884-b6288c9b4624">


</body>
</html>

<h2>Project Overview</h2>

<p>This is an Ecommerce Web Application built using Django. It allows customers to view/search products, add/remove products to/from the cart, place orders, and make payments.</p>

<h3>Features</h3>

<ul>
    <li>Customer can view/search products without logging in.</li>
    <li>Customer can also add/remove products to/from the cart without logging in (if the customer tries to add the same product to the cart, it will add only one).</li>
    <li>When the customer tries to purchase a product, then he/she must log in to the system.</li>
    <li>After creating an account and logging in to the system, he/she can place an order.</li>
    <li>There is a payment page also (just for demo, DO NOT FILL YOUR CARD DETAILS THERE; the website does not save that information).</li>
    <li>If you want to try PayPal, sign up for developer PayPal and get demo Login ID Password for the demo.</li>
    <li>If the customer clicks on the pay button, then their payment will be successful and their order will be placed.</li>
    <li>Customer can check their ordered details by clicking on the orders button.</li>
    <li>Customer can see the order status (Pending, Confirmed, Delivered) for each order.</li>
</ul>

<h4>Admin</h4>
<ul>
    <li>First admin will log in (for username/password run the following command in cmd):<br>
        <code>py manage.py createsuperuser</code></li>
    <li>Give username, email, password, and your admin account will be created.</li>
    <li>After login, there is a dashboard (attached in screenshot) where admin can see how many customers are registered, how many products are there for sale, and how many orders have been placed.</li>
    <li>Admin can add/delete/view/edit products.</li>
    <li>Admin can view/edit/delete customer details.</li>
    <li>Admin can view/delete orders.</li>
    <li>Admin can change the status of orders (Pending, Confirmed, Out for Delivery, Delivered).</li>
</ul>

<h2>How to Run the Project</h2>

<ol>
    <li><strong>Install Python</strong>: Install Python 3.10.11. Make sure to select "Add to Path" during installation.</li>
    <li><strong>Install Dependencies</strong>: Open a terminal and run the following commands:<br>
        <code>pip install django==4.2<br>
        pip install django-widget-tweaks<br>
        pip install -r requirements.txt<br>
        pip install xhtml2pdf</code></li>
    <li><strong>Download and Extract Project</strong>: Download and extract the project zip folder.</li>
    <li><strong>Database Configuration</strong>: Open <code>Ecommerce/ecommerce/settings.py</code> and set the database name or create a database named 'ecommerce'.</li>
    <li><strong>Run Migrations</strong>: In the terminal, navigate to the project folder and run:<br>
        <code>py manage.py makemigrations<br>
        py manage.py migrate</code></li>
    <li><strong>Run the Server</strong>: Start the development server by running:<br>
        <code>py manage.py runserver</code></li>
    <li><strong>Access the Application</strong>: Open your browser and go to <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>.</li>
</ol>

<h3>Disclaimer</h3>
<p>This project was developed for educational purposes and should not be used in a real-world application.</p>

</body>
</html>
