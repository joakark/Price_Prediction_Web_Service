## Price_Prediction_Web_Service

This is a web service for predicting housing prices using linear regression.

Training data are in the file "housing.csv". The data are part of the public domain dataset from the UCI
repository: https://archive.ics.uci.edu/ml/datasets/Housing.

<b> app.py </b> is the main application file

<b> regression.py </b> contains the regression

------------------

<b> Example request </b> (assuming that the server is running on port 5000 on localhost):

curl http://localhost:5000/predict -H "Content-Type: application/json" --data-binary '{
  "crime_rate": 0.1,
  "avg_number_of_rooms": 4.0,
  "distance_to_employment_centers": 6.5,
  "property_tax_rate": 330.0,
  "pupil_teacher_ratio": 19.5
}'
