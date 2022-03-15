import logging
import os
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
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, filename)
    model = pickle.load(open(filepath, 'rb'))
    answer = model.predict([[2,1,0,0]])
    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             f"Answer: {answer}.",
             status_code=200
        )
