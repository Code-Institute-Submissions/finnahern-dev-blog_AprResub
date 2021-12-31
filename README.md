# Developer Blog

[Link to deployed site.](https://ms4-django-blog.herokuapp.com/)

A project using Django to create an interactive blog website about being a new full stack developer. The Django app uses a Postgres database to store information on users and blog posts using a custom data model.

![Flowchart of the site navigation](screenshots/navigation.PNG)
Flowchart of the site navigation


## Features

- ### Custom data model for blog posts

![Post data model](screenshots/post_model.PNG)

- ### Functions for users to register for accounts, log in and out, and change their password

- ### Sidebar confirming login status to user on all pages

![Sidebar](screenshots/sidebar.PNG)

- ### Homepage listing all blog posts

All posts are listed newest first. The page features pagination so if there are more than 4 posts in the database it will create secondary pages with navigation links. Each post on the list features the title of the post, which is a link to individual post's view page, the publish date and time, the author and a truncated preview of the first 30 words.

![Home](screenshots/home.PNG)

- ### User dashboard

The user's dashboard can be reached from any page of the site by clicking on the username in the sidebar. It's a lot like the homepage except it can only be accessed once the user has logged in. It's list only features posts belonging to the currently signed in user. From here the user can change their password, create a new post, and they can view, edit or delete one of their existing posts. Like the home page, the dashboard also features pagination for more than 4 posts.

![User dashboard](screenshots/dashboard.PNG)

## User stories

## Testing
Bugs identified and fixed

Unresolved issues

Validator testing

Improvements to make

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