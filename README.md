# Developer Blog

[Link to deployed site.](https://ms4-django-blog.herokuapp.com/)

A project using Django to create an interactive blog website about being a new full stack developer. The Django app uses a Postgres database to store information on users and blog posts using a custom data model.

![Flowchart of the site navigation](screenshots/navigation.PNG)
Flowchart of the site navigation


## Features

- ### Custom data model for blog posts

The main purpose of the site is to view and create blog posts and for this I needed a data model to use in the database. Below is the Post model used in the project. Each post instance features a title, slug, which is used to create the post's unique url, author, body, dates for when it's published, created and updated, and it's status, either "draft" or "published".

![Post data model](screenshots/post_model.PNG)

- ### Functions for users to register for accounts, log in and out, and change their password

The site invites the user to register for an account and begin creating posts. This can be done quickly and easily using the site's registration, login and password change forms.

- ### Sidebar

The sidebar is visible on all pages of the site, confirming login status to user and allowing them to logout, or access their dashboard by clicking their username.

![Sidebar](screenshots/sidebar.PNG)

- ### Homepage/Blog post list

All posts are listed newest first. The page features pagination so if there are more than 4 posts in the database it will create secondary pages with navigation links. Each post on the list features the title of the post, which is a link to individual post's view page, the publish date and time, the author and a truncated preview of the first 30 words.

![Home](screenshots/home.PNG)

- ### User dashboard

The user's dashboard can be reached from any page of the site by clicking on the username in the sidebar. If the user is not signed in and try to go straight to the dashboard url they will be redirected to the login page. 

The dashboard is a lot like the homepage except it can only be accessed once the user has logged in. It's list only features posts belonging to the currently signed in user. From here the user can change their password, create a new post, and they can view, edit or delete one of their existing posts. Like the home page, the dashboard also features pagination for more than 4 posts.

![User dashboard](screenshots/dashboard.PNG)

- ### Post view

When the user clicks on the title of a post, either from the home page or from their dashboard where they are brought to the post view screen. Each post has a unique url generated using its created date and slug properties where this page is hosted. From here the user can read the full body of the post.

![Post view](screenshots/post_view.PNG)

- ### Full CRUD functionality for posts

As mentioned above the dashboard completes the CRUD functionality for the user's own posts. From there they can create a new post or edit an existing one using a simple form, as well as delete

![Post create form](screenshots/post_create.PNG)

## User stories

## Testing
Bugs identified and fixed
Password links/redirects not working - Changed urls from "login"/"logout" to "blog:login"/"blog/logout", 
Password change going to django error instead of redirect. added success_url="/password_change/done") to PasswordChangeView

Unresolved issues
-Slugs
-No defensive programming when deleting

- ### Validator testing
The Pythin code was validated using the [Pep8](http://pep8online.com/) validator. The only errors returned were a number of "line too long" and "continuation line under-indented for visual indent" errors, that don't interfere with the program logic.

Improvements to make

-Custom stlying, Bootstrap or MAterlalize
-Drafts
-Plugins like summernote or crispy forms to improve UX for forms.

## Deployment

## Credits

### Acknowledgements

Spencer Barriball for his feedback and advice and recommending invaluable resources

Anton Shmatov for letting me bounce questions off him and providing helpful support and advice.

### Technology used
- [Django 4.0](https://docs.djangoproject.com/en/4.0/)
- [Python](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/) - Database used to store data models
- [Git](https://git-scm.com/) - Version control.
- [Github](https://github.com/) - Used to host repository and live site.
- [Gitpod IDE](https://gitpod.io/) - Development enviornment used to build site.
- [Pep8 validator](http://pep8online.com/) - Used to validate code and check for errors.

### Resources

- [Django 3 By Example - Third Edition by Antonio Melé](https://www.packtpub.com/product/django-3-by-example-third-edition/9781838981952)
- [W3Schools](https://www.w3schools.com/)
- [Stackoverflow.com](https://stackoverflow.com/)