# sentiment-analysis-app
This web application allows users to classify text, putting it in one of three categories, Positive, Negative and Neutral. 

### Basic Features of The App
    
* SignUp – Users can register and create a new profile
* Login - Registered users can login using username and password
* User Profile - Each user profile contains a bio (Pointless right now, but just wanted to maintain a profile)
* Update Profile – Users can update their information such as username, email, password and bio
* Remember me – Cookie Option, users don’t have to provide credentials every time they hit the site
* Forgot Password – Users can easily retrieve their password if they forget it 

### Quick Start
To setup the project locally:

1. Set up a python virtual environment (venv)
2. Run the following commands
    ```
    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ python manage.py runserver
    ```
3. Run scripts/save_model.py to generate a model
    <br>a. add path to dir where you want to place the model
    <br>b. provide name of the model
    <br>c. both params later used in .env 
4. Open a browser and go to http://localhost:8000/
4. Sign up

