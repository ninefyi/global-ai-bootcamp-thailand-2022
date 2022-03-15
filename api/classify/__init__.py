import logging

import azure.functions as func
import pickle

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    filename = 'play_tennis.pkl'
    model = pickle.load(open(filename, 'rb'))
    answer = model.predict([[2,1,0,0]])
    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             f"Answer: {answer}.",
             status_code=200
        )
