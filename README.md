# Database Documentation

## 1. General

Library Package requirements:

1.  sudo apt install python3-pip
    
2.  pip3 install flask
    

## 2. Frontend

### Setting up: Initiating Flask for webserver. In Terminal,

1.  cd ./flaskproject
    
2.  export FLASK_APP=app.py
    
3.  export FLASK_ENV=development
    
4.  flask run
    
5.  Output:
    

![](https://lh4.googleusercontent.com/pc2SQ9ICydlDLhdpNKSKGjF0CdpfiJyOVikWMNmBpo_cE9GgFS6P9iK3q4Olf-VX7CDPVyc53SjgQ5S7_tJ2Q_OaWP5II1i9_fdUxUFPqohaym5Y1tQJAx9t1oOdfNskwQHg-Bd7)

  

### Webpages and Components:

Common Functions:

**1.  Navigation Bar:**
    The navigation bar in the top header of the webpage contains 3 links: one that leads to homepage, one to all categories page and lastly one that leads to creating a book page. The navigation bar is a common feature that is available on all pages to make accessibility to main pages easier.

![](https://lh3.googleusercontent.com/N3BJXtL2yCp9saMvU0BUqp3NA4SLpgG6uyH2BfKnEadgFrNmJSRX8n5CqHqZaihjQw58Yiornk_o12MPrw-Py-6y_MJ8aIgRFdW9O_o-D8uwDlh28gyUDe2lkMplMNq6kl5-2Us0)
**Figure 1: Navigation Bar**

**2.  Top Picks Column:**
 
There is a Top Picks Column on the right hand side of every page that returns a display of the top 9 books based on overall reviews. It is a clickable image that leads directly to the book and its reviews.

![](https://lh4.googleusercontent.com/w6nTaFnwc7W_v78-ITk2t8w4XzxMEQnsWZ-q9Q_D0mg3Ddu9zKczoT1CqkdBQAHLG9Ubgir5zYEqt92JLvcY4bvnVvRA7QtLy4udTQYEumqW2PCAY1LTg48uGK7mP9Teb-9NqxMa)  




  
  
  
Pages
1.  Homepage: ( / )
    

![](https://lh3.googleusercontent.com/RDS3EoUqfzS96nQC5VbSF-dbVlNDnsachwIN3rZ8YeBpuXcK_-00-VqU4E-08PK44CM6j4hBUmJ4hgT2lQiAWJAJ8kKJwcOEOQhsnMI-AdMi4Jc2rnuZK2f9LngcXSWXD_AlC7_U)

Figure 3: Home Page

**Search Book Function:**
The search book function on the main body of the homepage allows a user to search for a book based on its ASIN number. If an invalid ASIN number or no input is entered into the search function, a popup informs the user to enter a valid ASIN number. If the book ASIN number exists, the page redirects the user to the book and its reviews.

![](https://lh5.googleusercontent.com/F4YeF2kkzmqapjaADyl3vHv0tEMlwSEPf1lEcugNeYqiTcLeAnPeLbiZl7dAKOGdGqStwMbV7hpkDLA3RdNGKpUfdIXrOe46Q3TAeaJAYMiGz76I_zNm9Oul8cqnQjhtxPrVgPFJ)

Figure 4: Search Book Function (using ASIN ID)

  
  

**Top Categories Section:**
On the homepage main body, there is also a top categories section. This section allows the user to access the top categories of Great Reads. It redirects to the books classified in that category. Since the homepage can only access up to a number of categories, there is a redirect link to all the categories in Great Reads.

![](https://lh4.googleusercontent.com/9Gs3ok3V2P_C7NfufTjV52nWwS27ByAzVQnUcwYuffTz1OK-CB_JEV1fetkSm--IO03Pms_tmm9UbwOyEk4eLpzGjnADh-IM3OqeG6GkycL6_32XPWpGES063r_vNX1uJQq1pMXM)

Figure 5: Top Categories Section

  
  

**2.  All Categories Page** ( /allcategories)
  It is accessible from Categories in the navigation bar.

![](https://lh4.googleusercontent.com/u3RyqPjducTTbNa6hh-yoSzcxmS3DSqdtxNn4OX4i3urioXfD_Q2lcAtmcfmgrsW9OvdlWcRyz9CNG2Ydcpd-Tl7i9svm1lMxf13sFNa_q7dWLORCUrnrF5gr8mARG9O9GS1qN7k)

Figure 6: All Categories Page

  
**Categories:**( /categorypage/<categoryname> )
This page accesses all the available categories in the Great Reads database. Each category link redirects to the specific categories page that showcases all books in that particular category. 
  
![](https://lh6.googleusercontent.com/TvbqGYiqCoFzwrWF43HXiBjkALBSUA0m9EJvvOpAOLUpC_PHCg16_AkwHfFoplafZkB6yPnM2dwUF8eCBU_v6NUInElsQFt6pwc5vRpJfr-R6pY5VCrFeS1dm1w34VehKp0QaeWR)

Figure 7: (Specific) Categories Page

**3.  Book Reviews Page:**( /book/<asin> )
This page is accessible by clicking on a book from top picks, a book from the specific category or by searching up the exact ASIN number. It shows all the reviews of a particular book (identified by ASIN number), including the name of reviewer, review content and how many people have found the reviews helpful.

![](https://lh4.googleusercontent.com/f6eNxPlbY8KJb8J3hrZLG0s4YApqLHmXqyxyNxXjo5Ay0q4Ph7-l5ru68vFJrMH_oiidoUhaYd7bPzSA7xUK5ZaAnp5-XO6Ij5I6pGN86S3fze38OGUB5etG2xT03iWF6j-pJcd2)

Figure 10: Book Reviews Page


**Create a Review Popup:**

At the left hand side of the page, there is a create a review button that brings up a popup to create a new review (for that particular book). Certain fields are required and if are not properly filled in, will result in an alert to “fill in the required fields”.

![](https://lh6.googleusercontent.com/aUh9NzBx0kvCtAiFySnCQKWT3eTyA4hGQhzpVGX2jroll4uU0qDHdG2yp4xmP-LOcwf6zvNfiGnDM7UW6Hz7IZjA3KNUXzIjC5B7IWgEGxqcEPvE7zgON7KHJMav4Aw3pSGuWPTH)

Figure 11: Write a New Review Page


**3.  Create Book Page:**
    Once Add Book from Navigation bar is clicked, a pop-up for admin password pops up.
    
**Admin Login Page:**
A normal user of the webpage is not allowed to create a new book. Therefore, we have added an additional function that only allow admins to create new book in the system. The admin password to access the create a book page is: admin.

![](https://lh4.googleusercontent.com/BQjG9WeY64MrECH5MqwG7hRjKV76fpkJdRqi-NOExxqdexxnEEHkN-CvdnqqyO_uq48LzR-3C1F-lZuW7e8Cq4XqqGYXRP90oZgeNsC6asWUGfUr1XPkLDLObFivFok1DQBXsYgQ)

Figure 8: Admin Login for Creating a New Book

  

**Create a Book Page:**

This page is only allowed for admins and will only be accessible by those who have the admin password. It contains the form to create a new book that would be inputted into mongoDB.

![](https://lh6.googleusercontent.com/KC0v5v_3AjHkFAnX1U9XKR7i4A1v-CwfhU6H6hbBtqnWRYvcXo4p5-gizN3_onYg3nq2U14JlXQ68bSlmI7U4p5nsm5w3ju2KBCJNfZKO3eczqJEt7PFd7e7oNkCEGgwPDKqvx6h)

Figure 9: Create a Book Form
