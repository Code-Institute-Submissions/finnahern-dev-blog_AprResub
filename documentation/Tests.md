# Testing

In order to manually test each function of the site I'm going to go through each page and document the expected result of various actions and compare this to the actual result.

# User log in
#### ACTION: 
Complete the login form with valid credentials.
#### EXPECTED RESULT:
The user is logged in to their account.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Complete the login form with a valid username but incorrect password.
#### EXPECTED RESULT:
The user is not logged in to their account.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Complete the login form with an invalid username and password.
#### EXPECTED RESULT:
The user is not logged in to their account.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Submit the login form with empty fields.
#### EXPECTED RESULT:
An error is displayed, the form is not submitted.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Try to access the login screen while already logged in via the url.
#### EXPECTED RESULT:
The form is not displayed and the user is prompted to logout or go back.
#### ACTUAL RESULT:
As expected.

<br>

# User registration
#### ACTION: 
Complete the registration form with a valid username, email and password.
#### EXPECTED RESULT:
A new user object is created and the user is prompted to login.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Complete the registration form with a username that already exists in the database.
#### EXPECTED RESULT:
An error is displayed, the form is not submitted.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Complete the registration form with a username containing disallowed characters.
#### EXPECTED RESULT:
An error is displayed, the form is not submitted.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Try to access the registration screen while already logged in via the url.
#### EXPECTED RESULT:
The form is not displayed and the user is prompted to logout or go back.
#### ACTUAL RESULT:
As expected.+


<br>

# Logout
#### ACTION: 
Click the logout button
#### EXPECTED RESULT:
An error is displayed, the form is not submitted.
#### ACTUAL RESULT:
As expected.

<br>

# Blog
#### ACTION: 
Create a new blog post with each form field populated.
#### EXPECTED RESULT:
A new Post object is added to the database.
#### ACTUAL RESULT:
As expected.

<br>

#### ACTION: 
Create a new blog post with non-alphanumeric symbols in the title.
#### EXPECTED RESULT:
A new Post object is added to the database.
#### ACTUAL RESULT:
The slug cannot handle symbols and the url is invalid. This breaks any page that features a link to the newly created Post, which is most of them. This is a critical error.

<br>

#### ACTION: 
Edit an existing blog post to add non-alphanumeric symbols in the title.
#### EXPECTED RESULT:
The same error as above.
#### ACTUAL RESULT:
This actually works fine as editing a post does not change the slug. This could potentially cause problems if there was an error in the title that the author doesn't want a visible record of.

<br>