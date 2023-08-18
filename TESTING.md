# Contents

-[Validation Testing](#validation-testing)

  *[HTML](#html)
  
  *[CSS](#css)

  *[Python](#python)

  *[Lighthouse](#lighthouse)

-[Browser Testing](#browser-testing)

-[Device Testing](#device-testing)

-[Manual Testing](#manual-testing)

## Validation Testing

### HTML

Html was validated using W3.org Nu validator.

<details>

<summary>Click for validation screenshots</summary>

Homepage
![Recipes Page](Documentation/Testing%20Documentation/Screenshot%20Nu%20Html%20Validation%20HomePage.png)

Log Out Page
![Log Out Page](Documentation/Testing%20Documentation/Screenshot%20Nu%20Html%20Validation%20Log%20Out%20Page.png)

Members Recipes Page
![Members Recipes Page](Documentation/Testing%20Documentation/Screenshot%20Nu%20Html%20Validation%20Members'%20Recipes%20Page.png)

Recipe Detail Page
![Recipe Detail Page](Documentation/Testing%20Documentation/Screenshot%20Nu%20Html%20Validation%20Recipe.png)

Sign In Page
![Sign In Page](Documentation/Testing%20Documentation/Screenshot%20Nu%20Html%20Validation%20Sign%20In%20Page.png)

</details>

<br>

[Back to Contents](#contents)

### CSS

Jigsaw.w3.org was used to validate CSS in this app.

<details>

<summary>Click for validation screenshots</summary>

CSS Validation Test Pass
![CSS Validation](Documentation/Testing%20Documentation/Screenshot%20Jigsaw%20CSS%20Validation.png)

</details>

<br>

[Back to Contents](#contents)

### Python

Code Institute Python Linter was used to validate the python code in the app.

<details>

<summary>Click for validation screenshots</summary>

manage.py Pass
![manage.py](Documentation/Testing%20Documentation/Screenshot%20Python%20Linter%20Pass%20%20manage.py.png)

admin.py pass
![admin.py](Documentation/Testing%20Documentation/Screenshot%20Python%20Linter%20Pass%20admin.py.png)

apps.py pass
![apps.py](Documentation/Testing%20Documentation/Screenshot%20Python%20Linter%20Pass%20apps.py.png)

forms.py pass
![forms.py](Documentation/Testing%20Documentation/Screenshot%20Python%20Linter%20Pass%20forms.py.png)

models.py pass
![models.py](Documentation/Testing%20Documentation/Screenshot%20Python%20Linter%20Pass%20models.py.png)

settings.py pass
![settings.py](Documentation/Testing%20Documentation/Screenshot%20Python%20Linter%20Pass%20settings.py.png)

urls.py1 pass
![urls.py1](Documentation/Testing%20Documentation/Screenshot%20Python%20Linter%20Pass%20urls.py1.png)

urls.py2 pass
![urls.py2](Documentation/Testing%20Documentation/Screenshot%20Python%20Linter%20Pass%20urls.py2.png)

views.py pass
![views.py](Documentation/Testing%20Documentation/Screenshot%20Python%20Linter%20Pass%20views.py.png)

wsgi.py pass
![wsgi.py](Documentation/Testing%20Documentation/Screenshot%20Python%20Linter%20Pass%20wsgi.py.png)

</details>

<br>

[Back to Contents](#contents)

### Lighthouse

<details>

<summary>Click for validation screenshots</summary>

Homepage Validation
![Recipes Page](Documentation/Testing%20Documentation/Screenshot%20Lighthouse%20Result.png)

Recipe Validation
![recipe](Documentation/Testing%20Documentation/Screenshot%20lighthouse%20test%20recipe%20page.png)

Submit Recipe Validation
![submit recipe](Documentation/Testing%20Documentation/Screenshot%20Lighthouse%20Test%20Submit%20Recipe.png)

Members Recipes Validation
![members' recipes](Documentation/Testing%20Documentation/Screenshot%20Lighthouse%20Test%20Members'%20Page.png)

Edit Profile Validation
![edit profile](Documentation/Testing%20Documentation/Screenshot%20Lighthouse%20Test%20Edit%20Profile%20Page.png)

Log Out Page Validation
![log out](Documentation/Testing%20Documentation/Screenshot%20Lighthouse%20Test%20Log%20Out%20Page.png)

</details>

<br>

[Back to Contents](#contents)

## Browser Testing

App was tested on Chrome, Firefox, Microsoft Edge and performed normally on each browser.

[Back to Contents](#contents)

## Device Testing

The app was tested on a range of devices and performed well on all of them. Devices tried include Samsung Galaxy Note 8, iPad Pro, iPhone 12 Pro, iPhone SE, Samsung Galaxy S9+ and Nokia N9.

[Back to Contents](#contents)

## Manual Testing

### Site Navigation

|Element         |Expected Result                                |Pass/Fail |
|----------------|-----------------------------------------------|----------|
|Logo            |Link to bk to Home Page                        | Pass     |
|Home            |Direct to Home Page                            | Pass     |
|Home            |Show admins published recipes                  | Pass     |
|Members Recipes |Open Members Recipes Page                      | Pass     |
|Members Recipes |Shows only published members recipes           | Pass     |
|Submit a Recipe |Only visible to members                        | Pass     |
|Submit a Recipe |Open Submission Form                           | Pass     |
|Submit a Recipe |Submit button submits form to admin            | Pass     |
|Edit Profile    |Only visible to members                        | Pass     |
|Edit Profile    |Open Member's Profile Page                     | Pass     |
|Edit Profile Pg |Displays List of member's recipes              | Pass     |
|Edit Profile Pg |Allow member to update email                   | Pass     |
|Edit Profile Pg |Allow member to read/update/delete own recipes | Pass     |
|Log Out         |Only visible to signed in members              | Pass     |
|Log Out         |Open Sign Out Page                             | Pass     |
|Sign Out Page   |Visible after clicking log out                 | Pass     |
|Sign Out        |Signs member out                               | Pass     |
|Log In          |Only visible when not signed in                | Pass     |
|Log In          |Logs member in to site                         | Pass     |
|Sign Up         |Only visible when not signed in                | Pass     |
|Sign Up         |Registers new member                           | Pass     |
|Recipe Card     |Display correct content                        | Pass     |
|Recipe Card     |Click title to enter recipe                    | Pass     |
|Recipe Card     |Responsive to screen size                      | Pass     |
|Recipe Card     |Paginate 6 cards to page                       | Pass     |
|Footer          |Logo opens to Home Page                        | Pass     |
|Footer          |Buttons open socials in new tab                | Pass     |
|User Comments   |Display approved comments                      | Pass     |
|Comment Form    |Display only to members                        | Pass     |
|Comment Form    |Button submits comment for approval            | Pass     |
|Like button     |Count likes for recipe                         | Pass     |
|Like button     |only allow members to click                    | Pass     |



[Back to Contents](#contents)
