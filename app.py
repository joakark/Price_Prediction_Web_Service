from flask import Flask
from flask_restful import Api, Resource, reqparse
from regression import run_regression


app = Flask(__name__)
api = Api(app)

class Data(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("crime_rate", type=float, required=True)
        parser.add_argument("avg_number_of_rooms", type=float, required=True)
        parser.add_argument("distance_to_employment_centers", type=float, required=True)
        parser.add_argument("property_tax_rate", type=float, required=True)
        parser.add_argument("pupil_teacher_ratio", type=float, required=True)
        args = parser.parse_args()

        result = run_regression(args)

        return result, 200


api.add_resource(Data, '/predict')
app.run(debug=True)
