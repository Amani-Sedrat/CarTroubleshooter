from flask import Flask, request, jsonify

app = Flask(__name__)

# define knowledge base
knowledge_base = {
    'rules': [
        {'condition': ['engine starts', 'fuel tank not empty'], 'action': 'check fuel pump'},
        {'condition': ['engine starts', 'fuel tank empty'], 'action': 'check fuel level'},
        {'condition': ['engine starts', 'fuel pump working', 'air filter clean'], 'action': 'no problem found'},
        {'condition': ['engine starts', 'fuel pump working', 'air filter dirty'], 'action': 'replace air filter'},
        {'condition': ['engine starts', 'fuel pump not working'], 'action': 'replace fuel pump'},
        {'condition': ['engine does not start'], 'action': 'check battery'},
        {'condition': ['battery faulty'], 'action': 'replace battery'},
        {'condition': ['oil light on'], 'action': 'check oil level'},
        {'condition': ['oil level low'], 'action': 'add oil'},
        {'condition': ['oil leak'], 'action': 'check engine gasket'},
        {'condition': ['brakes squeaking'], 'action': 'replace brake pads'},
        {'condition': ['brakes not responding'], 'action': 'check brake fluid'},
        {'condition': ['brake fluid low'], 'action': 'add brake fluid'},
        {'condition': ['steering wheel vibrating'], 'action': 'balance wheels'},
        {'condition': ['car pulls to one side'], 'action': 'check wheel alignment'},
        {'condition': ['check engine light on'], 'action': 'check engine error codes'},
        {'condition': ['engine overheating'], 'action': 'check coolant level'},
        {'condition': ['coolant level low'], 'action': 'add coolant'}
    ],
    'facts': {
        'engine starts': False,
        'fuel tank not empty': False,
        'fuel tank empty': False,
        'fuel pump working': False,
        'air filter clean': False,
        'air filter dirty': False,
        'fuel pump not working': False,
        'engine does not start': False,
        'battery faulty': False,
        'oil light on': False,
        'oil level low': False,
        'oil leak': False,
        'brakes squeaking': False,
        'brakes not responding': False,
        'brake fluid low': False,
        'steering wheel vibrating': False,
        'car pulls to one side': False,
        'check engine light on': False,
        'engine overheating': False,
        'coolant level low': False
    }
}

# define working memory
working_memory = knowledge_base['facts']

# define inference engine
def inference_engine(knowledge_base):
    agenda = []
    for rule in knowledge_base['rules']:
        if all(knowledge_base['facts'][condition] for condition in rule['condition']):
            agenda.append(rule['action'])
    return agenda

# define API endpoint
@app.route('/infer', methods=['POST'])
def car_troubleshooter():
    data = request.get_json()
    input_data = data['input']
    if input_data in working_memory:
        working_memory[input_data] = True
    agenda = inference_engine(knowledge_base)
    return jsonify({'actions': agenda})

if __name__ == '__main__':
    app.run()
