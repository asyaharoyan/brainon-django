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
- For the admin, there is a chance to approve och disapprove the comments

### Future development

- Provide a filter to make it easy to find lessons
- Provide a search form to find a specific lesson or teacher's videos
- Have one shorter video lesson for everyone who has not signed up yet to attract more users
- Provide actual videos instead of pictures
- Provide 2 sign-up methods for teachers and students
- Give teachers access to upload their videos

## Designing The Models

The project and the models has been designed by the help of Blog walkthrough project. As it is recommended the models 
was designed on a paper to get some overview how it will look like. During the development some names had been changed.

![Courses Form](static/media/form-courses.jpg)

![Courses Form](static/media/form-comment.jpg)

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
It is expected to extend this part of the project adding search and filter when the users are on online lessons page.

### About Page

![Header mobiles](static/media/about-page.png)

On the about page, the user gets to know about BrainON. It is more useful for the teachers who want to collaborate.
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

Next and Preview buttons appear as needed depending on which page the user is and if there is a next or preview page.

### Comment Form

![Comment Form](static/media/comments-form.png)

The comment form can be used only by registered users. The user has the possibility to change or delete their own comments.
When a user leaves a comment there is a clear message which pops up to inform the user that the comment is awaiting 
approval. After approval the user still can edit or delete the comment however the user can not see or edit someone 
else's comment.

![Comment Form](static/media/comment.png)

### Register Form

![Register Form](static/media/sign-up-form.png)

Register form has been taken from django's standard library. It has been styled and adapted the design of the website.

### Log Out Form

![Log Out Form](static/media/login-form.png)

Log out form, as register form has been taken from django's standard library. It has been styled and adapted the 
design of the website.

### Footer

![Footer](static/media/footer.png)

Footer includes the links to the social media and each page opens in a new window as a good UX.

### Admin Panel

![Admin Panel](static/media/admin-panel.png)

The admin panel has access to see, approve comments, to create a teacher profile and lessons.

![Collaboration Requests](static/media/collaboration-requests.png)

From admin panel the user can see the requests and which ones are already read.

![Comments Approval](static/media/comments-approval.png)

Admin can approve or delete the comments which are not appropriate.

## Debugging

- Error has been shown while deploying the project.
- Added env.py file to fix it.

- Error has been shown when uploading the pictures from admin panel.
- The error has been fixed b adding cloudinary link.

- Edit and delete buttons did not work properly.
- Fixed the bug by console logging. The ID of the comment was not beeing taken. Fixed the error.

### Unfixed Errors

- Uncought(in promise) Error

![Error](static/media/bug.png)

- Mixed content

![Error](static/media/bug-1.png)

## Manual Testing

The web-site has been tested on Google Chrome, Mozilla, Google Egde on both bigger screens and mobile phone.
The content is loading on all webbrowsers.
Several manual tests has been done on both computer and mobile devices. 

- All the social media links are opening in a new tab
- All the buttons are reacting as it is expected
- It is possible to send a collaboration request

![Collaboration Request](static/media/collaboration-request.png)

- It is not possible to send collaboration request without e-mail, name or a message

![Empty Comment](static/media/empty-comment.png)

- It is possible to register a new account on both mobile devices and computers
 The user Nare and JS has registered and left comments from a mobile while asya
 has registered from a laptop

- It is possible to log in
- Logged in user can leave a comment
- Users can not see unapproved comments except for their own
- One user can not edit or delete another ones comment
- Edit comment/Delete comment buttons are working as expected

![Edit Delete comment](static/media/delete-btn.png)

- Users can not leave a empty comment

![Empty comment](static/media/empty-comment.png)

- All the menu buttons are leading to the pages as expected
- Not authorized user can not see online lessons as expected
- Logged in user sees different buttons accordingly

![Not logged in user](static/media/sing-in.png)

![Logged in user](static/media/watch-online-lessons.png)

- Admin gets collaborations requests as expected

![Collaboration Request](static/media/collaboration-requests.png)

- Admin can approve or delete comments

![Approve comment](static/media/approve-delete.png)

- Admin can create and delete a teacher/courses profile

![Delete Courses](static/media/delete-courses.png)

- Draft lessons don't show on the website
- By deleting a lesson, the comment deletes with the lesson
- By deleting a teacher all the lessons are being deleted
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

Online lessons
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
Has changed the version of allauth
![Log in validated](static/media/login-valid.png)

Register
- Error
![Register nonvalid](static/media/register-nonvalid.png)

- Validated
Has changed the version of allauth
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

The code has been deployed on the early stages of the project. Deployment steps has been followed from Django Blog project.

The variables has been added in Heroku as expected

![Github Deployment](static/media/deployment.png)

![Heroku](static/media/heroku.png)

## Credits

The website has been made with help of Django Blog project. About model, collaboration models and comment models
are taken from blog project. JS file has been taken from blog project and adapted to serve BrainOn project.
Most of the help for planning the project has been taken from [Django Recepie Sharing tutorial by Dee Mc](https://www.youtube.com/watch?v=_GNvmwvvS70&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=24).
Some help for coding has been taken from [Python Django tutorial](https://www.youtube.com/watch?v=kmeEIJE7JDU).

For designing the UI has been used Marvelapp.com
The pictures has been downloaded from free sourse [Pixaby](https://pixabay.com/)
For resizing the pictures to shorten loadtime has been used [Imagesizer](https://imageresizer.com/)
For favicon has been used [Faicon Generator](https://favicon.io/favicon-converter/)