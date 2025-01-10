## BrainON
![Responcive BrainON](static/media/brainon-responcive.png)

## About BrainOn
BrainOn is an innovative online learning portal designed to connect teachers and students through engaging video content.
The portal is designed for school students to learn the daily lessons in a more interactive way and make the learning journey
more fun.
The platform has features to come as it is going to develop in time. It is going to have a search and filter form as well as 
2 types of sign-in - one for teachers and one for students.

## Design
The design of the website is aimed to be interesting and easy to use for younger students. It is fully responsive so the
users can log in and study regardless of where they are. The main UX rules are kept such as readable text, and clear signs to find
and locate things on the page.

The logo has been designed by me, using CorelDraw.

## User stories

- The existing users can log in and watch online courses
- There is clear navigation on the website to use it easily
- The teachers who wish to share video lessons can send a collaboration request
- After each request/comment there is a clear message for the user
- For new users, the first page includes full information about the website
- For the new users there is clear guidance on how to sign up and why
- For admin, there is a designed UX to read requests, answer them
- For the admin, there is a chance to approve or disapprove the comments

### Future development

- Provide a filter to make it easy to find lessons
- Provide a search form to find a specific lesson or teacher's videos
- Have one shorter video(teaser) lesson for everyone who has not signed up yet to attract more users
- Provide actual videos instead of pictures
- Provide 2 sign-up methods for teachers and students
- Give teachers access to upload their videos

## Entity Relationship Diagram

To visualize the connections between the models in the BrainOn app, I have created a relationships diagram. This diagram provides a clear representation of how the models interact with each other.

![Entity Relationship Diagram](static/media/diagram.png)

## Models

The project and the models have been designed with the help of the Blog walkthrough project. 

- About model

![About Model](static/media/about-model.png)

- Course model

![Course Model](static/media/course-model.png)

- Lesson model

![Lesson Model](static/media/lesson-model.png)

- Comment model

![Comment Model](static/media/comment-model.png)


## Designing The UI

Before diving into coding BrainON logo had been designed on CorelDraw and the UI on the Marvel App. During the development 
process some features had been removed and added to serve its purpose and to fit in the time frame.
The search feature has been removed at this stage of the project, Contact Us page has been moved to the About Page as a collaborate form.
In this stage, the colours have not been decided so it has been chosen grey as a neutral colour.

![Home page](static/media/design-home.png)

![About page](static/media/desing-about.png)

![Collaborate form](static/media/design-collaborate.png)

![Lessons page](static/media/design-lessons.png)

![Signup form](static/media/design-signup.png)

## Typography

The fonts chosen were 'Karla' for headings and 'Quicksand' for the rest of the app. As a fall back has been choosen standars 'serif' in case the choosen font does not load.
It has been used different font-weights and font-sizes to give clearity.

## Color Scheme

The app's color scheme primarily features black, white, gray, and subtle light shades. This minimalistic palette ensures the focus remains on the educational content, particularly the videos uploaded by the teachers.

However, the welcome page introduces a touch of color—soft and not overly bright. This page is designed to be inviting and visually engaging, using interactive elements and images rather than being text-heavy. This thoughtful design approach creates a warm and approachable entry point for users while maintaining the app's overall clean and professional aesthetic.

![Colors](static/media/colors.png)

## Features

### Header

![Header](static/media/header.png)

The header has been designed to navigate the students and the teachers easily through the website.
It is fully responsive and easy to use on all gadgets.

When the device is smaller the menu is moved to the side as a small burger button to save space.

![Header mobiles](static/media/mobile-header.png)

### Home Page

![Header mobiles](static/media/home-page.png)

The home page has been designed to give some information and motivate young learners to register and be a part of fun learning
experience.
It gives reasons why to sign up as it has been requested in user stories.
It is expected to extend this part of the project by adding a search and filter when the users are on the online lessons page.

### About Page

![Header mobiles](static/media/about-page.png)

On the About page, the user gets to know about BrainON. It is more useful for the teachers who want to collaborate.
The short introduction leads the teachers to send an e-mail to the admin to share their videos.

### Collaboration form

![Collaboration form](static/media/collaboration-form.png)

The form comes just after About BrainON as a user would expect to find it quickly after reading about
the page and deciding to collaborate with BrainON.

### Online Lessons

![Online Lessons](static/media/online-lessons.png)

Online lessons are available only for registered users. On the website, it shows only pictures. There is a short information 
including the name of the teacher, the subject and the name of the lesson as it is expected to have more than one teachers 
on one subject, some students might have favorite teachers and it is important to see the information before opening the
lesson. 
It is expected to develop in the future and have video lessons, and show a relevant picture on this page, however since this
project is only for learning purposes, no videos have been uploaded. There are only standard pictures to keep the website
interesting.

### Next/Prev Buttons

![Next/Prev Buttons](static/media/next-btn.png)

Next and Preview buttons appear as needed depending on which page the user is on and if there is a next or preview page.

### Comment Form

![Comment Form](static/media/comments-form.png)

The comment form can be used only by registered users. The user can change or delete their comments.
When a user leaves a comment there is a clear message which pops up to inform the user that the comment is awaiting 
approval. After approval the user still can edit or delete the comment however the user can not see or edit someone 
else's comment.

![Comment Form](static/media/comment.png)

### Register Form

![Register Form](static/media/sign-up-form.png)

The register form has been taken from Django's standard library. It has been styled and adapted to the design of the website.

### Log Out Form

![Log Out Form](static/media/login-form.png)

Log out form, as a register form has been taken from Django's standard library. It has been styled and adapted to the 
design of the website.

### Footer

![Footer](static/media/footer.png)

The footer includes the links to the social media and each page opens in a new window as a good UX.

### Admin Panel

![Admin Panel](static/media/admin-panel.png)

The admin panel has access to see, and approve comments, to create a teacher profile and lessons.

![Collaboration Requests](static/media/collaboration-requests.png)

From the admin panel, the user can see the requests and which ones are already read.

![Comments Approval](static/media/comments-approval.png)

Admin can approve or delete the comments which are not appropriate.

## 404 page

The website has a custom 404 page which has been designed to lead the user back to the home page.

![404 page](static/media/404-page.png)

## Debugging

- Error has been shown while deploying the project.
- Added env.py file to fix it.

- Error has been shown when uploading the pictures from the admin panel.
- The error has been fixed by adding a Cloudinary link.

- Edit and delete buttons did not work properly.
- Fixed the bug by console logging. The ID of the comment was not being taken. Fixed the error.

### Unfixed Errors

- Uncought(in promise) Error

![Error](static/media/bug.png)

- Mixed content

![Error](static/media/bug-1.png)

## Manual Testing

The website has been tested on Google Chrome, Mozilla, and Google Edge on both bigger screens and mobile phones.
The content is loading on all web browsers.
Several manual tests have been done on both computer and mobile devices. 

- All the social media links are opening in a new tab
- All the buttons are reacting as it is expected
- It is possible to send a collaboration request

![Collaboration Request](static/media/collaboration-request.png)

- It is not possible to send a collaboration request without e-mail, name or a message

![Empty Comment](static/media/empty-comment.png)

- It is possible to register a new account on both mobile devices and computers
 The users Nare and JS have registered and left comments from mobile while asya
 has registered from a laptop

- It is possible to log in
- Logged-user can leave a comment
- Users can not see unapproved comments except for their own
- One user can not edit or delete another one's comment
- Edit comment/Delete comment buttons are working as expected

![Edit Delete comment](static/media/delete-btn.png)

- Users can not leave an empty comment

![Empty comment](static/media/empty-comment.png)

- All the menu buttons are leading to the pages as expected
- Not authorized users can not see online lessons as expected
- Logged-user sees different buttons accordingly

![Not logged in user](static/media/sing-in.png)

![Logged in user](static/media/watch-online-lessons.png)

- Admin gets collaboration requests as expected

![Collaboration Request](static/media/collaboration-requests.png)

- Admin can approve or delete comments

![Approve comment](static/media/approve-delete.png)

- Admin can create and delete a teacher/course profile

![Delete Courses](static/media/delete-courses.png)

- Draft lessons don't show on the website
- By deleting a lesson, the comment deletes with the lesson
- By deleting a teacher all the lessons are deleted
- Log in and register pages check for valid passwords


## Validating Code

- Validating templates
Home page 
![Home](static/media/home-app-valid.png)

About page
- Error
![About page error](static/media/about-error.png)

- Validated
![About page valid](static/media/about-page-valid.png)

Online Lessons
![Online lessons valid](static/media/online-lessons-valid.png)

Lesson details
- Error
![Lesson detail error](static/media/lesson-detail-nonvalid.png)

- Validated
![Lesson detail valid](static/media/lesson-detail.valid.png)

Log in
- Error
![Log in nonvalid](static/media/login-nonvalid.png)

- Validated
Has changed the version of all auth
![Log in validated](static/media/login-valid.png)

Register
- Error
![Register nonvalid](static/media/register-nonvalid.png)

- Validated
Has changed the version of all auth
![Log in validated](static/media/login-valid.png)

Log out
![Register valid](static/media/register-valid.png)


All the CSS validation has passed through without any errors

![CSS home](static/media/css-home.png)

![CSS about](static/media/css-about.png)

![CSS courses not logged in](static/media/css-courses-nonauth.png)

![CSS courses](static/media/css-courses-auth.png)

![CSS login](static/media/css-login.png)

![CSS logout](static/media/css-logout.png)

![CSS register](static/media/css-register.png)

About App has been validated without errors

![Admin](static/media/admin-about.png)

![Forms](static/media/form-about.png)

![Models](static/media/models-about.png)

![Views](static/media/views-about.png)

Courses App has been validated without errors

![Admin](static/media/admin-courses.png)

![Forms](static/media/forms-courses.png)

![Models](static/media/models-courses.png)

![Views](static/media/views-courses.png)

The settings file has been validated without any errors

![Settings](static/media/settings-main.png)

## Lighthouse

The website has been tested on Lighthouse to see the performance.

Before resizing the pictures: 

![Lighthouse](static/media/lighthouse1.png)

After resizing the pictures.

Mobile:
![Lighthouse](static/media/lighthouse2.png)

Computers:
![Lighthouse](static/media/lighthouse3.png)

## Deployment

The project was deployed to **Heroku**. The deployment process is as follows:

1. Create repository

- Create a new **GitHub** repository from CI template and  click on Create repository from template.
- Click 'Code' and then copy either the HTTPS or SSH link. I used SSH.

![Copy URL](static/media/copy-url.png)

- Open GitPod and paste the URL then click open workspace

![Copy URL](static/media/open-gitpod.png)

2. Installing Django and supporting libraries:

- Now it's time to install Django and it's supporting libraries. In the terminal, type the following commands:

        pip3 install Django~=4.2.1
        pip3 install dj_database_url psycopg2
        pip3 install dj3-cloudinary-storage

- After you have successfully installed the above, type the following command:

        pip3 freeze --local > requirements.txt

- This will create a requirements.txt file as show below

- Now we need to create our Django project and the applications. In the terminal type the following command:

        django-admin startproject PROJ_NAME .
        django-admin startapp APP_NAME .

- You then need to add your application to the INSTALLED_APPS section in your settings.py as shown below

![Installed APP](static/media/installed-app.png)

- After creating models, type the following commands in the terminal:

        python manage.py makemigrations
        python manage.py migrate

3. Create the Heroku app:

- Navigate to your Heroku dashboard and create a new app with a unique name and choose your preferred region.

![Step 1](static/media/heroku1.png)

- Since we are in Heroku, navigate to your project settings and click 'Reveal Config Vars'. Add your Heroku config vars to your project as shown below

        DISABLE_COLLECTSTATIC = 1 is a temporary step for the moment and it will be removed before deployment

- Create a file named Procfile at the root directory of the project. In the Procfile, declare this is a web process followed by the command to execute your Django project.

        web: gunicorn poject_name.wsgi

- In settings.py file change DEBUG=True with DEBUG=False.

- Also, in settings.py we need to append the Heroku hostname to the ALLOWED_HOSTS list.

![Aloowed Hosts](static/media/allowed-hosts.png)

- Back in code, create a new file called env.py and ensure this is added to your gitignore file. Copy the below code but change the variable content to your specific details.

        import os

        os.environ["DATABASE_URL"] = "Your PostgreSQL link"
        os.environ["CLOUDINARY_URL"] = "Your PostgreSQL link"
        os.environ["SECRET_KEY"] = "Your PostgreSQL link"

- In settings.py, look for the line that says 'from pathlib import Path' and then insert the code below.

![Settings Import](static/media/settings-import.png)

- Replace the default random security key that Django provides with your SECRET_KEY that you created in your env.py file.

![Secret Key](static/media/secret-key.png)

- Now you can git add, commit and push changes.

4. Deploying an app to Heroku:

- Now, let's return to the Heroku dashboard, and in your app, click on the Deploy tab.

![Deploy 1](static/media/deploy-heroku.png)

- In the Deployment method section enable GitHub integration by clicking on Connect to GitHub.

![Deploy 2](static/media/deploy-heroku1.png)

- Start typing your project repo name into the search box and click Search. A list of repositories from your GitHub account should appear. Click on the GitHub repo you want to deploy from.

![Deploy 3](static/media/deploy-heroku2.png)

- Scroll to the bottom of the page and click Deploy Branch to start a manual deployment of the main branch.

![Deploy 3](static/media/deploy-heroku3.png)

- Click on Open app to view your deployed project.

![Open App](static/media/open-app.png)

## Credits

The website has been made with the help of the Django Blog project. The About model, Collaboration models and Comment models
are taken from the blog project. JS file has been taken from the blog project and adapted to serve the BrainOn project.
Most of the help for planning the project has been taken from [Django Recipe Sharing tutorial by Dee Mc](https://www.youtube.com/watch?v=_GNvmwvvS70&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=24).
Some help for coding has been taken from [Python Django tutorial](https://www.youtube.com/watch?v=kmeEIJE7JDU).

Designing the UI has been used Marvelapp.com
The pictures have been downloaded from the free source [Pixaby](https://pixabay.com/)
For resizing the pictures to shorten load time has been used [Imagesizer](https://imageresizer.com/)
For favicon has been used [Faicon Generator](https://favicon.io/favicon-converter/)
How to create 404 page [404 page in django](https://www.makeuseof.com/create-custom-404-error-page-django/)
