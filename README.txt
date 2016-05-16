
Shopify Coupon Generator

To Run App:

-cd into ApiProject directory (that includes api, ApiProject, env, db.sqlite3, manage.py)
-launch virtual environment: “source env/bin/activate”
-run app: “./manage.py runserver"

To Test Coupon Generation:
-go to http://127.0.0.1:8000/coupon/ in browser
-enter coupon information and submit (will return page with coupon name)
-login to shopify account at https://www.shopify.com/login :
	Store address: austin123
	Email address: au.smith7@gmail.com
	Password: password
-Navigate to Discounts, and the coupon you just generated should be there.
