knowledge_base = {
    ('engine wont crank', 'dashboard lights on'): 'The problem is with the starter. It needs to be replaced.',
    ('engine wont crank', 'dashboard lights off'): 'The battery is dead and needs to be recharged or replaced.',
    ('engine crank slowly', 'clicking noise'): 'The battery is weak and needs to be recharged or replaced.',
    ('engine crank slowly', 'whirring noise'): 'The starter is faulty and needs to be replaced.',
    ('engine crank slowly', 'dim lights'): 'The charging system is bad and needs to be repaired or replaced.',
    ('engine crank slowly', 'normal lights'): 'The battery is weak and needs to be recharged or replaced.',
    ('engine crank normally', 'immediate stall'): 'The fuel pump is faulty and needs to be replaced.',
    ('engine crank normally', 'rough idling'): 'The fuel filter is clogged and needs to be replaced.',
    ('engine crank normally', 'noisy engine'): 'The engine mounts are faulty and need to be replaced.',
    ('engine runs rough', 'smell of gasoline'): 'The fuel injectors are clogged and need to be cleaned or replaced.',
    ('engine runs rough', 'smoke from tailpipe'): 'The oxygen sensor is faulty and needs to be replaced.',
    ('engine runs rough', 'rattling noise'): 'The timing chain is loose and needs to be replaced.',
    ('engine overheats', 'coolant leak'): 'The water pump is faulty and needs to be replaced.',
    ('engine overheats', 'low coolant'): 'The radiator is leaking and needs to be repaired or replaced.',
    ('engine overheats', 'steam from hood'): 'The head gasket is blown and needs to be replaced.',
    ('car shakes', 'steering wheel vibrates'): 'The wheels are unbalanced and need to be balanced.',
    ('car shakes', 'brake pedal vibrates'): 'The brake rotors are warped and need to be resurfaced or replaced.',
    ('car shakes', 'whole car vibrates'): 'The driveshaft is faulty and needs to be repaired or replaced.',
    ('car pulls to one side', 'uneven tire wear'): 'The wheels are not properly aligned and need to be aligned.',
    ('car pulls to one side', 'no tire wear'): 'The brake caliper is faulty and needs to be replaced.'
    
}

agenda = []

# Define the working memory as a set
working_memory = set()

# Define a function to perform inference
def infer(symptoms):
    global agenda, working_memory
    # Add the symptoms to the working memory
    working_memory.update(symptoms)
    # Check if any of the rules match the current state of the working memory
    for antecedent, consequent in knowledge_base.items():
        if set(antecedent).issubset(working_memory):
            # Add the consequent to the agenda if it's not already in the working memory or agenda
            if consequent not in working_memory and consequent not in agenda:
                agenda.append(consequent)
    # If the agenda is not empty, return the next item on the agenda
    if agenda:
        return agenda.pop(0)
    # Otherwise, return None
    return None

# Define a Flask app to provide an API endpoint for the inference engine
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/infer', methods=['POST'])
def handle_infer():
    # Get the symptoms from the request body
    symptoms = request.json.get('symptoms', [])
    # Perform inference to find the solution
    solution = infer(symptoms)
    # Return the solution as a JSON response
    return jsonify({'solution': solution})

if __name__ == '__main__':
    app.run(debug=True,port=8080,use_reloader=False)