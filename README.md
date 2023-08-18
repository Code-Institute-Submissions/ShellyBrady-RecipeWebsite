
# NICE AND EASY RECIPES

Introduction

Nice and Easy Recipes is a full-stack website using Django, Python, Bootstrap, HTML and CSS.
It is built for educational purposes only and the members are fictional.

[Click to go to Nice And Easy Recipes](https://recipesite.herokuapp.com/)

![Am I Responsive Image](<Documentation/Testing Documentation/Responsivemess/Screenshot amiresponsive.png>)

## Contents

- [About](#about)

- [UX](#ux)

- [Agile Methodology](#agile-methodology)

- [Features](#features)

- [Bugs](#bugs)

- [Wireframes](#wireframes)

- [Technologies Used](#technologies-used)

- [Testing](#testing)

- [Deployment](#deployment)
  - [Deployment to Heroku](#deployment-to-heroku)
  - [Forking](#forking)
  - [Creating a Clone](#creating-a-clone)

- [Credits and Acknowledgements](#creating-a-clone)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

#

## [About](#about)

- Nice and Easy Recipes is a website where people can read recipes. Users that sign up and become members can submit their own recipes to be included on the Members Recipes Page.
- Members' submitted recipes are listed on their profile page, making it a convenient way of storing their own recipes.
- Members can also 'like' and comment on all recipes as long as they're signed in.

[Back to Contents](#contents)

## UX

### Target Audience and Site Goals

-Nice and Easy Recipes is targetted at anyone who enjoys simple recipes such as busy parents, beginner cooks and people who are intimidated by more complex tastes and methods.

-These users will be looking for easy recipes with common ingredients in a simple format which is easy to navigate.

-They may want to share their own recipes with like-minded people.

-They would find keeping all their own recipes in one place online convenient.

-They may enjoy being able to like and comment on other members' recipes.

### User Stories

#### As a user

-I want to be able to see recipes available on the website

-I want to be able to click in to a recipe and read it

-I want to be able to access the website from any device

-I want to be able to register as a member

-I want to be able to sign in and out as a member

-I want to be able to comment on recipes as a member

-I want to be able to like recipes as a member

-I want to be able to share my own recipes as a member

-I want to be able to see a list of the recipes I have submitted

-I want to be able to click into my recipes in the list and read them

#### As an administrator

-I want to be able access the site from any device

-I want to be able to log in to my account

-I want to be able to access the admin screen

-I want to be able to check member's submitted recipes before they are published.

-I want to check others' comments before approving them for publishing.

-I want to be able to manage recipes included on the site

-I want to be able to add recipes to the homepage

-I want to be able to add suitable images to recipes

-I want to be able to edit recipes

-I want to be able to designate staff status to another user if needed

### Structure

#### Masthead and Navigation

- On all pages, this area contains the website name which is a clickable link to the homepage. It also contains a clear and uncluttered navigation menu.

#### Body

- The body holds recipe cards on the homescreen and Members' Recipes Page. On the Submit Recipe Page, which is available to signed in members only, the body contains a form to submit ingredients and instructions for their recipe. Profile information will be shown here on the Edit Profile Page. This area also is where any messages will be displayed and where registration, sign in or out screens will show.

#### Footer

- The footer of all site webpages contains the site name which is again a clickable link bringing the user back to the homescreen. It also contains the social media buttons.

### Surface

#### Fonts

- Libre Baskerville: logo, welcome message, recipe titles, submission form title
- Georgia: submit button, recipe headings, nav menu, author details
- Helvetica Neue: recipe details, sign out form, edit profile page, comments, footer social media prompt

As I wanted to site to look simple I used a combination of these three fonts to create subtle contrast between sections and to add interest without distracting the user.

#### Colours

Again, wishing to keep the site clean and uncluttered I stayed with a slight change in background colours, allowing the content of words and vivid photographs of food to stand out.

![Colour Palette Used](Documentation/App%20Screenshots/Colour%20Scheme%20RGB%20Canva.png)

Dark Green (#006400) Used for site logo and main headings for attention against a pale background and drawing the user's eye.

Dark Slate Grey (#2f4f4f) Body text on recipe pages and recipe list pages are dark slate grey, making the black of the navigation menu stand out further.

Light Grey (#d3d3d3) The background of the bottom of the recipe cards is light grey to highlight the important details contrasting against the food pic and pale container background.

White Smoke (#f5f5f5) I used this off-white to take away from the starkness of a white background.

White (#ffffff) White is used as a background to the navigation menu and footer.

#### Images

Images are used on the recipe cards and at the top of each recipe.
Vibrant photos of the food is important on a recipe website. They and the recipes used are taken from various websites which will be fully credited [here](#credits)

[Back to Contents](#contents)

## Agile Methodology

Issues and Project

While developing this app I incorporated agile methodology by using Github's project to create issues according to my user stories and moving them through my kanban as I worked on them. My Issues can be seen by clicking [here](https://github.com/ShellyBrady/RecipeWebsite/issues?q=is%3Aissue+is%3Aclosed). My project can be viewed [here](https://github.com/users/ShellyBrady/projects/3).

[Back to Contents](#contents)

## Features

### Navigation Menu

![Navigation](Documentation/App%20Screenshots/Screenshot%20Home%20Screen%20Menu%20and%20Upper.png)

The navigation area changes dynamically depending on whether the user is a signed-in member or a guest. A guest sees a different set of options-there is no 'Edit Profile' or 'Submit a Recipe' choices. Instead they are replaced with a 'Sign Up' link.

### Recipe Cards

![Recipe Cards](Documentation/App%20Screenshots/Screenshot%20recipe%20cards.png)

The recipe cards tile across the page and are responsive to changes in screen size. The recipe title is a clickable link that brings the user into the recipe chosen. Underneath the image and recipe title are all the details that tell the user who wrote it, when and if it has any likes.

### Footer Area

![Footer](Documentation/App%20Screenshots/Screenshot%20Home%20Screen%20Footer%20and%20Lower.png)

The footer contains the website logo which is a clickable link back to the landing page. Below this are the common social media buttons and the name of the site creator.

### Recipe

![Recipe](Documentation/App%20Screenshots/Screenshot%20Recipe%20Read%20Screen.png)

The recipe is formatted with the image to the right of the recipe title and the details of the recipe in clear sections beneath. When the recipe is viewed on a small screen, the nav bar becomes a vertical menu and the image is displayed beneath the recipe title.

### Recipe Submission Form

![Submission-Form](Documentation/App%20Screenshots/recipesubmission%20screenshot.png)

The submission form is only available to signed in members. It is a simple form with clearly labelled sections for the member to fill in with the relevant details. Once submitted, the recipe goes to admin to be checked and published to the Members' Recipes page. The member sees a message highlighted in green telling them their recipe was submitted successfully.

### Comment and Like Feature

![member-comment-area](Documentation/App%20Screenshots/Screenshot%20Member%20Comment%20Area.png)

![guest-leave-no-comment](Documentation/App%20Screenshots/Screenshot%20Guest%20No%20Comment%20Form.png)

The comments, once approved by admin, are visable to all users including guests. However the comment form area is blank for guests which means they must register or sign in to like or leave a comment.

### Edit Profile Page

![edit-profile](Documentation/App%20Screenshots/Screenshot%20Member%20Edit%20Profile.png)

The Edit Profile page is very simple and is an area I would develop in future. It contains the member's name, allows them to enter their email address and will show a clickable list of all the recipes they previously submitted to the site which admin has approved and published. This page is only veiwable by the member themselves and is not an available page to guests.

### Admin Menu

From this menu, admin can manage members and content. They can read, delete or approve comments submitted, delete members, read, delete or publish submitted recipes or submit their own recipes.

#### Admin Recipe Submission

![admin-add-recipe](Documentation/App%20Screenshots/Screenshot%20Admin%20Add%20Recipe%20To%20Recipe%20Page.png)

Admin can add recipes to the main Recipes page by filling in this form.

#### Admin Profile Edit

![admin-profile](Documentation/App%20Screenshots/Screenshot%20Admin%20%20Profile%20Change.png)

Admin can edit their profile from this page.

### Future Features

To develop the site further i would:

- add more to the member's profile page including profile picture

- allow members to connect their social media accounts

- add a search function to increase functionality

- add keywords to recipes to increase search capabilities

- allow members to favourite recipes, adding them to a personalised list they can easily click on later.
[Back to Contents](#contents)

## Bugs

'Image Not Showing' Bug

- When testing my app I realised the image in the recipe was not showing when the screen was narrower than the width of the image. I set breakpoints using @media screen. Finally had to remove 'd-none' from masthead image div from recipe_detail and submisssion_detail templates. This fixed the bug.

[Back to Contents](#contents)

## Wireframes

![Wireframe Homescreen](Documentation/Wireframes/Screenshot%20Wireframe%20Landing%20Page.png)
![Wireframe-Recipe-Page](Documentation/Wireframes/Screenshot%20Wireframe%20Recipe%20Page.png)
![Wireframe-Recipe-Form](Documentation/Wireframes/Screenshot%20Wireframe%20Member%20Recipe%20Form.png)

[Back to Contents](#contents)

## Technologies Used

[Cloudinary](https://cloudinary.com/) to store images used on the website.

[Canva](https://www.canva.com/) used to create the colour scheme image used in this README.

[Heroku](https://dashboard.heroku.com/apps) used to deploy the app from.

[ElephantSQL](https://www.elephantsql.com/) Postgres Database host service for the app.

[Gitpod](https://www.gitpod.io/) CDE used to develop this app.

[Github](https://github.com/) was the git repository used.

[Balsamiq](https://balsamiq.com/) used to create wireframes.

[Bootstrap](https://getbootstrap.com/) contributed to responsiveness.

[Django](https://www.djangoproject.com/) framework used while creating this app.

[Cloudconvert](https://cloudconvert.com/) was used to convert the jpg I used to WebP format.

[Tinypng](https://tinypng.com/) compressed images to shorten load time.

[W3C Validator](https://validator.w3.org/) was used to validate all the html in this app.

[AutoPrefixer](https://autoprefixer.github.io/) helped with CSS by parsing it and adding vendor prefixes.

[Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) was used through-out.

[Chrome Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk)
validated the HTML.

[CSS Validator](https://jigsaw.w3.org/css-validator/) validated the app's CSS.

[Code Institute's Python Linter](https://pep8ci.herokuapp.com/) validated python used in the app.

[Am I Responsive?](https://ui.dev/amiresponsive) was used to create the image at the beginning of the README.

[Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used for forms.

[Summernote](https://github.com/summernote/django-summernote) is an editor used in this project.

[Google Fonts](https://fonts.google.com/) was used for fonts.

[Font Awesome](https://fontawesome.com/) was used for icons.

[Back to Contents](#contents)

## Testing

Testing and results can be seen by clicking [here](/TESTING.md)

[Back to Contents](#contents)

## Deployment

### Deployment to Heroku

- Log in to Heroku and create new app by clicking on 'New' on the Dashboard.

- Choose your app name and the relevant region. Create app.

- Attach the Database by typing in Postgres under add-ons in the Resourses tab and select 'Heroku Postgres'

- Copy the Database_Url in the Config Vars in the Settings tab.

- Create an env.py file in your gitpod workspace and add the DATABASE_URL and SECRET_KEY values.

- Comment out the default database config before saving and making migrations.

- Add Cloudinary URL to env.py and cloudinary libraries to the list of installed apps.

- Add the Static file settings and link the file to the templates directory in Heroku.

- Make TEMPLATES_DIR the templates directory and add Heroku to the ALLOWED_HOSTS list.

- Create a requirements.txt file and add media, storage and templates directories to the main directory.

- Add a Procfile to the main directory and add web: gunicorn NiceAndEasyRecipes.wsgi

- In the Heroku Config Vars add the SECRET_KEY value, CLOUDINARY_URL, PORT=8000 and DISABLE_COLLECTSTATIC=1

- Ensure DEBUG is false in settings.py before deploying.

- In the Heroku app, click on the deploy tab. Connect to Github and then to your repository.

- Select Enable Automatic Deployment to prevent having to deploy after each time the repository is updated. Click on 'Deploy Branch' to deploy manually. Wait until build is ready and then click view app to see your live deployed site.

[Back to Contents](#contents)

### Forking

- To fork your repository, click the 'Fork' button to the right by the name of repository. Chose 'Create a New Fork' from the drop down menu.

[Back to Contents](#contents)

### Creating a Clone

- Clicking on the 'Code' button near the top of the chosen repository, choose your preferred clone option and copy the link.

- Then in the terminal, choose where you want your cloned directory to be located.

- Enter 'git clone' and paste in the URL copied from the Github previously. Your clone has been created.

[Back to Contents](#contents)

## Credits and Acknowledgements

### Credits

Recipes and their accompanying images were taken from the following sites:

- [Jamie Oliver's Crab Cakes](https://www.jamieoliver.com/recipes/seafood-recipes/crab-cakes/)

- [Jamie Oliver's Guinness Pie](https://www.jamieoliver.com/recipes/beef-recipes/mash-topped-beef-guinness-pie/)

- [EasyFood's Skillet Lasagne](https://easyfood.ie/recipe/quick-skillet-lasagne/)

- [Tesco Ham and Potato Casserole](https://realfood.tesco.com/step-by-step/3-ingredient-creamy-ham-and-potato-casserole.html)

- [Odlum's Rocky Road](https://www.odlums.ie/recipes/aunty-heathers-rocky-road-bars/)

- [Odlum's Chocolate Eclairs](https://www.odlums.ie/recipes/chocolate-eclairs/)

- [Tesco Pineapple Cake](https://realfood.tesco.com/recipes/upside-down-pineapple-cake-drizzled-with-honey.html)

- [Tesco Yorkshire Pudding Dessert](https://realfood.tesco.com/recipes/yorkshire-pudding-with-pears-and-chocolate-sauce.html)

Further credits:

- [Stack Overflow](www.stackoverflow.com)

- [Heroku](https://devcenter.heroku.com/categories/deployment)

- [Slack](https://slack.com/intl/en-ie/)

- [Code Institute Blog Walthrough](https://github.com/Caode-Institute-Solutions/Django3blog)

- [Django Docs](https://docs.djangoproject.com/en/4.2/)

- [Bootstrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

[Back to Contents](#contents)

### Acknowledgements

I would like to acknowledge Iris, my cohort facillitator for all her support and Bethany from Student Care for keeping me going through some really tough times. I very much appreciate all you do.

[Back to Contents](#contents)
