# JObBoard - Django Project



Steps:

1. Clone/pull/download this repository
2. Create a virtualenv with `virtualenv env` and install dependencies with `pip install -r requirements.txt`
    ###### The requirements.txt will install the latest version od django. if you want a specific version, you are free to edit the file !
3. Configure your .env variables
4. Rename your project with `python manage.py rename <yourprojectname> <newprojectname>` - if needed
## 5. After successfull migration, you need to create two groups in Group model named 'employee' and 'employer' either by going to admin panel or using shell

This project includes:

1. Settings modules for deploying with Azure
2. Django commands for renaming your project and creating a superuser
3. A cli tool for setting environment variables for deployment

