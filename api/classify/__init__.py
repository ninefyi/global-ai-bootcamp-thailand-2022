import logging
import os

from numpy import outer
import azure.functions as func
import pickle

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        temp = req_body.get('temp')
        outlook = req_body.get('outlook')
        humidity = req_body.get('humidity')
        windy = req_body.get('windy')

    filename = 'play_tennis.pkl'
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, filename)
    model = pickle.load(open(filepath, 'rb'))
    answer = model.predict([[outlook,temp,humidity,windy]])

    if answer == 0:
        answer = "Yes"
    else:
        answer = "No"

    return func.HttpResponse(
            f"Answer: {answer}.",
            status_code=200
    )
