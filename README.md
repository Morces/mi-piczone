# MI-PICZONE
## Description 
This is a Django app that is actually a personal gallery. It allows a user to upload images for others to see.

## Screenshot
## Homepage
This is how the home page looks like.
<img src="https://raw.githubusercontent.com/Morces/mi-piczone/master/static/img/homepage.png">

## Single Image
When you click on a single image, this pops up.
<img src="https://raw.githubusercontent.com/Morces/mi-piczone/master/static/img/single-image.png">

## User Story
One should be able to:
- View different photos that interests them.
- Click on a single photo to expand it and also view details of the photo.
- Search for different categories of photos.
- Copy a link to the photo to share with friends.
- View photos based on the location they were taken.

## Setup Instructions

Clone the repo
```bash
https://github.com/Morces/mi-piczone.git
```
Navigate into the cloned repo
```bash
cd mi-piczone 
```
Install and activate venv
```bash
- python3 -m venv virtual - source virtual/bin/activate
- pip install -r requirements.txt
```
Set up database, host the and migrate.
```bash
python3 manage.py makemigrations gallery
```
Migrate
```bash
python3 manage.py migrate
```

Run the application
```bash
python3 manage.py runserver
```

## Technologies Used
- Django4.0 - for development of the application.
- Heroku -  for deployment.
- Git - for version control

## Contibutions and Support
Pull Requests are welcomed

## Contact information 
Reach me through email [karanim594@gmail.com]

## License
[MIT license](https://github.com/Morces/mi-piczone/master/LICENSE)



