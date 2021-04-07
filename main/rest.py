from main import request
from flask import Blueprint

blueprint = Blueprint("rest", __name__, url_prefix="/rest")

@blueprint.route('/test', methods=['GET', 'POST'])
def hello_world():
    data = request.get_json()
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        f = open("/home/B180093/anaconda3/envs/telechips/test.txt", 'w')
        f.write("no parameter~~~")
        f.close()
        return 'No parameter'

    parameters = ''
    for key in parameter_dict.keys():
        parameters += 'key: {}, value: {}\n'.format(key, request.args[key])

    f = open("/home/B180093/anaconda3/envs/telechips/test.txt", 'w')
    f.write(parameters + "\n" + data['webhookEvent'] + "\n" + data['issue_event_type_name'])
    f.close()
    return 'Hello World!'


