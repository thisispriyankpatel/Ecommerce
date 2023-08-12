screenshots:- 
—----------------------------------------------------------------------------------------------------------------------------
<img width="400" alt="image" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/ef2fb936-2b43-42d7-b85b-b73e3fdbe6b6"><img width="600" alt="image" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/5371c728-8433-454d-b1af-98c2e0aedcdc">

<img width="877" alt="image" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/39c0978f-ef50-44cd-a340-2b24e5b11ad9">
<img width="863" alt="image" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/9569c1cb-b58d-4aa7-a799-a85314e4b1ce"><img width="915" alt="image" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/68932236-ed07-4ac7-b07a-8ec34ca3e707">
<img width="864" alt="image" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/28a8fda6-bd40-477f-88b8-55d4b21729cb"><img width="692" alt="image" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/536fb8cb-7042-4483-92b6-f9ebad98f343">
<img width="863" alt="image" src="https://github.com/thisispriyankpatel/Ecommerce/assets/124012521/efbb3b76-bb85-423c-8884-b6288c9b4624">

FUNCTIONS:- 
—----------------------------------------------------------------------------------------------------------------------------
Customer:- 
—----------------------------------------------------------------------------------------------------------------------------
Customer can view/search products without login.
Customer can also add/remove product to cart without login (if customer try to add same product in cart. It will add only one)
When customer try to purchase product, then he/she must login to system.
After creating account and login to system, he/she can place order.
There is a payment page also (just for demo, DONT FILL YOUR CARD DETAILS THERE ,By the way, website do not save that details)
If you want to try Paypal signup for developer Paypal and will get demo Login ID Password for demo.
If customer click on pay button, then their payment will be successful and their order will be placed.
Customer can check their ordered details by clicking on orders button.
Customer can see the order status (Pending, Confirmed, Delivered) for each order



Admin:-
—-------------------------------------------------------------------------------------------------------------------------
First admin will login ( for username/password run following command in cmd )
py manage.py createsuperuser


Give username, email, password and your admin account will be created.
After run python manage.py runserver and go to http://127.0.0.1:8000/admin
After login, there is a dashboard where admin can see how many products are there for sale, how many orders placed.
Admin can add/delete/view/edit the products.
Admin can view/edit/delete customer details.
Admin can view/delete orders.
Admin can change status of order (order is pending, confirmed, out for delivery, delivered)



HOW TO RUN THIS PROJECT:- 
—----------------------------------------------------------------------------------------------------------------------------
Install Python (3.10.11) (Dont Forget to Tick Add to Path while installing Python)
Open Terminal and Execute Following Commands :
pip install django==4.2
pip install django-widget-tweaks
pip install -r requirements.txt
pip install xhtml2pdf




Download This Project Zip Folder and Extract it
Now go to Ecommerce\ecommerce\settings.py file and set Database name to your data base or create same as ‘ecommerce’ database to you mysql databases
Move to project folder in Terminal. Then run following Commands :
py manage.py makemigrations
py manage.py migrate
   py manage.py runserver


Now enter following URL in Your Browser Installed On Your Pc
http://127.0.0.1:8000/


Disclaimer
This project is developed for collage assignment purpose and it's not supposed to be used in real application.

