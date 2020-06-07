# COVID-19-Dashboard
An interactive covid-19 dashboard to visualize statistics from scraped data. The Dashboard is made using the Dash library in plotly. The dashboard shows interactive pie charts, line charts, bar charts and indicator charts to visualize the trend in infections (positive cases), recoveries and deaths for a range of countries. The data scraped from worldometer.info and Wikipedia page. The script for scraping and the data can be found on this repository - <a href="https://github.com/rajtulluri/COVID-19-Web-Scraper">Link to Repo</a>

### To run the application locally :-

Clone the repository using git clone.

    git clone https://github.com/rajtulluri/COVID-19-Dashboard.git
    
Run the app.py file

    python3 app.py
    
To access the dashboard, type localhost:3000 in the browser.

### To deploy the application on heroku :-

Fork the repository and make changes as you wish.
Create a new conda environment,

    conda create -n env_name python=3.6

Then activate the new environment created,

    conda activate env_name
    
Install the following dependencies using pip.

- dash
- pandas
- numpy
- gunicorn
- flask
- plotly

You can use the below command,

    pip install dash

Create a file named Procfile with the contents
    
    web: gunicorn app:server
    
Retrieve requirements.txt file using pip freeze as,

    pip freeze > requirements.txt
    
Finally, run the following commands

    heroku create my_app
    git add .
    git commit -m "Initial push"
    git push heroku master
    heroku ps:scale web=1
    
The heroku server will provide with the link. Your app is now deployed.
The above app can be checked out at this link - https://covid19-dashboard-appv1.herokuapp.com/


