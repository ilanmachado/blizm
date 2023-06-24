from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)

# Initial setup and route definitions
@app.route('/')
def home():
    # Home page of the website
    return render_template('home.html')

@app.route('/influencers')
def influencers():
    # Page that lists the available influencers
    # Function to retrieve influencers from the database
    influencers = get_influencers()
    return render_template('influencers.html', influencers=influencers)

@app.route('/campaigns', methods=['GET', 'POST'])
@login_required # Only logged in users can access this page
def campaigns():
    # Page that lists the available campaigns
    # Function to retrieve campaigns from the database
    campaigns = get_campaigns()
    return render_template('campaigns.html', campaigns=campaigns)
    if request.method == 'POST':
        # Code to create a new influencer marketing campaign
        campaign_data = request.form  # Data submitted from the form
        # Function to create the campaign in the database
        create_campaign(campaign_data)
        return redirect('/campaigns')
    else:
        # Page that lists the existing campaigns
        campaigns = get_campaigns() # Function to retrieve campaigns from the database
        return render_template('campaigns.html', campaigns=campaigns)
    

@app.route('/campaigns/<int:id>', methods=['GET', 'POST'])
@login_required # Only logged in users can access this page
def campaign(id):
    # Page that lists the available campaigns
    if request.method == 'POST':
        # Function to create a new campaign
        return render_template('campaigns.html', campaigns=campaigns)
    else:
        # Page that lists the existing campaigns
        return render_template('campaigns.html', campaigns=campaigns)
    

# Other routes
@app.route('/influencers/<int:id>', methods=['GET', 'POST'])
def new_func():
    create_campaign(campaign_data)app.route('/campaigns/<int:id>', methods=['GET', 'POST'])
@login_required # Only logged in users can access this page
def create_campaign(id):
    # Page that lists the available campaigns
    if request.method == 'POST':
        # Function to create a new campaign
        return render_template('campaigns.html', campaigns=campaigns) # Return the page with the new campaign added
    else:
        # Page that lists the existing campaigns
        return render_template('campaigns.html', campaigns=campaigns) # Function to retrieve campaigns from the database
    
    
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login page
    if request.method == 'POST':
        # Function to log in the user
        return redirect('/')
    else:
        # Page that lists the existing campaigns
        return render_template('login.html')

@app.route('/logout')
def logout():
    # Function to log out the user
    return redirect('/')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Signup page
    if request.method == 'POST':
        # Function to sign up the user
        return redirect('/')
    else:
        # Page that lists the existing campaigns
        return render_template('signup.html')
    
if __name__ == '__main__':
    app.run(debug=True)

