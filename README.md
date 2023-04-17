# cs50-final-project
## cs50x final project. A webapp for estimating housing prices in Lagos and Abuja

This project is a webapp where users can estimate the price of a house in a given location in Abuja or Lagos - both states in Nigeria. The main aim of the project was to improve my machine learning knowledge and knowledge of making web based applications with flask where models can be deployed.

Teechnologies/libraries used inlude:
* python
* javascript
* flask
* tensorflow
* sklearn
* pandas
* numpy

# Implementation details
## Data used
The housing data set used for the project was obtained from kaggle via https://www.kaggle.com/datasets/eyimofeapinnick/nigeria-rent-prices-2022. Originally the dataset contained housing data from numerous Nigerian states however I decided to streamline the data down to only Abuja and Lagos for 2 reasons:
* Data for some locations was not sufficient enough to accurately represent/model those states
* Cumbersome preprocessing due to large size of the data
* Abuja and Lagos are major regions in Nigeria. This was even reflected in the data as houses from these states had the highest number of observations


## Data Processing
Most of the data manipulation and processing took place in the jupyter notebookfile. Preprocessing mainly involved the removal of house price extremes and incorrect data and making dummy variables for the house types. 
A variety of regression models were employed including neural networks, gradient boosting regression, random forest regression. Gradient boosting performed better for the dataset and was optimised using randomsearchcv. Final model was saved in the "gbr2_new" pickle file.

## Making the Flask Webapp
The flask webapp consists of 2 main routes: "/abuja" and "/lagos". These routes contain html forms for sending post request to the prediction routes "/predict_abuja" or "/predict_lagos" where the model is used to predict prices depending on the data sent to the route. See app.py.
Util.py contains information on the names of various locations. These location names are loaded in a html select tag when the window is loaded. The select tag also contains a search feature for easier interaction

## How to Launch
* Check you have the required libraries mentioned in requirements.txt
* Run flask run in terminal window
* Go to the given link

## Likely Future improvements
* Improving the accuracy of the model used 
* Adding more states 
* Improving the overall design of the webpage
