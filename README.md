# OTUS_Suite
Test suite for OTUS curse


Install Django-Debug-Toolbar

    https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
    

Credentials to admin portal
    
    login:      admin
    password:   admin


# Curses
All API request for managing curses  

### All curses
GET /curse/


### Create
**POST** /curse/create/


    {
        "name": "Curse name",
        "descriptions": "Some descriptions",
        "date_time_release": "2019-07-03 11:20:06",
        "enabled": true
    }
    
### Info
GET /curse/\<int:pk\>/
* pk - curse ID


    {
        "id": 1,
        "name": "First curse",
        "descriptions": "Some info about curse",
        "date_time_release": "2019-07-03T11:19:44Z"
    }
 
 * id - curse ID
 * name - curse name
 * descriptions - info about curse
 * date_time_release - date start curse

### Update

### Delete

### Reserved


# Lesson

### Info
### Add
### Update
### Delete

# User
### Register
### Login

# Teacher
### Info
### Nearest courses
