# NGO Data Visualization Landing Page and Donations Service
#### Description:
Final project for CS50
## Project description
The project is a landing page for the NGO that I work for which helps provide education for underprivileged children (it's been anonymized as "MyNGO"). The goal is to visualize the impact the NGO has as well as the potential impact an individual donor could have by dynamically showcasing its impact data. A slider on the landing page can be dragged to change the donation amount, and the impact the donation has will be dynamically displayed below. Additionally, the KPs hero image will change based on the donation to vizualize the impact further and emotionalize donors.

The project also provides the possibility of donating money through a form as well as showcasing past donations in a table.

The project was created using python and flask while also utilizing client-side JavaScript. The pages were designed using HTML and bootstrap as well as some custom CSS.

## index.html
The homepage consists first of a hero section with a large image, a donation slider and a donation-button. Below are four bootstrap-card-elements containing a KPI for the NGO (beneficiaries, teachers, projects). Below that is an FAQ designed using bootsrtap's accordion element.

The slider's slider-value is listened to live via JavaScript and displayed as the current donation amount in the hero section. It is also passed on via the donation button to the donation-form.

The slider-value is also used to calculate the dynamic KPI in the card-elements using variables passed onto index.html via app.py. The function updateStats gets the midpoint between min and max values of the scale and uses it and the current value to calculate a scale value. This scale value is then used to manipulate the KPI according to slider position. The mid-point of the slider displays the KPI at a factor of 1, the max-point at a factor of 2, and the min-point at a factor of 5% as to still show non-zero values for the minimum, non-zero donation.

The second function updateImg is used to change the hero-section's image-path according to slider-value, changing at 20, 45 and 70%. It is set to go through 4 comic-style images of a classroom with varying degrees of student count, equipment and overall condition depending on how much money is being donated.

## donate.html
This bootstrap-styled form collects first and last name, email and donation amount. It requires a TOS-tick and a "valid" email address. The amount-field is autopopulated server-side when the user has come via the main page through a POST request (the donate button) and a valid amount had been selected.

## donations.html
This page shows donations.csv which is created upon the first donation in app.py. It's shown using jinja and a pandas-dataframe.

## thanks.html
The thank-you-page appears upon submission of the donation-form and is populated with the first name of the donor through app.py for a personalized thank you.

## impress.html and privacy.html
These pages are fillers to populate the footer of the pageg and flash out the design.

## layout.html
The layout consists of the head which calls bootstrap as well as a custom styles.css file.
Also there's a navbar element in the body taken from bootstrap. The navbar is resposive and switches from text-links in the navbar to a dropdown-menu in mobile-format.
Lastly, a custom #footer-class has been created.

## styles.css
Various custom changes have been made to existing tags and new classes have been created as well. The goal was to enable enhanced functionality while integrating the new elements into the look and feel of the bootstrap elements.
The body has been changed so it spans the entire screen and so the footer is always at the bottom of the screen, even if the page content's don't fill it.

## numbers.csv & donations.csv
Numbers.csv is expected from the page admin upon initial setup. It is a simple 2-row csv.file and is used to provide a dynamic experience during data-visualization, meaning the data can be swapped for another NGO's data.
Donations.csv is created upon first donation and keeps track of all donations.

## app.py
App.py requires Flask, Flask-session, pandas, os and csv.
First, it opens numbers.csv, sets up variables for the values and calculates an average donation value. It also sets up a session to keep track of theactual donation value set with the slider on the main page.
It routes all html-pages. For simplicity I will focus on the more complicated ones:

### donate()
the donate-button on the main page triggers the post-method of donate(), getting the slider value in a variable first, the in a session value. If the method was not post, donate() tries to get the existing session-value and upon failure sets 0 as default. The donation value is the passed as an argument of render_template to donate.html where it is set as the default value in the form.

### thanks()
thanks() is called when the donation-form is submitted. It gets all data from the form, stores it in variables, creates a list of lists containing the names of the columns as well as a list of the varialbes (to account for both cases where donations.csv has and hasn't yet been created). Then an if-conditional checks for the existence of donations.csv and either creates it and writes both the column names and new line or opens it and appends the new line using "a" instead of "w". Then the render_template function takes the person's first name as an argument to personalize the thank you note.

### donations()
Donations() checks for the existence of donations.csv. If it doesn't exist, nothing is being displayed. If it exists, a dataframe is created using pandas and given as an argument for donations.html.
