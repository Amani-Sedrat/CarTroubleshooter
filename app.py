from flask import Flask, jsonify, request

app = Flask(__name__)

# Knowledge base
rules = [
    (['check engine light is on', 'car wont start'], 'Dead battery'),
    (['car wont start', 'clicking sound'], 'Bad starter motor'),
    (['car wont start', 'no sound'], 'Bad battery connection'),
    (['car stalls or dies while driving', 'car wont restart'], 'Faulty alternator'),
    (['car shakes or vibrates', 'steering wheel vibrates'], 'Wheel balance problem'),
    (['car makes a squealing noise', 'hard to steer'], 'Loose or worn belt'),
    (['car makes a grinding noise', 'brake pedal pulsates'], 'Worn brake pads'),
    (['car makes a clicking noise', 'car wont start'], 'Bad starter solenoid'),
    (['car wont start', 'engine cranks'], 'Fuel system problem'),
    (['car wont start', 'engine does not crank'], 'Starter motor problem'),
    (['car runs rough', 'check engine light is on'], 'Misfiring cylinder'),
    (['car stalls or dies while driving', 'check engine light is on'], 'Faulty oxygen sensor'),
    (['car pulls to one side', 'tire wear is uneven'], 'Wheel alignment problem'),
    (['car pulls to one side', 'steering wheel off-center'], 'Wheel alignment problem'),
    (['car makes a whining noise', 'steering feels heavy'], 'Low power steering fluid'),
    (['car makes a rattling noise', 'car is idling roughly'], 'Loose or damaged muffler'),
    (['car makes a hissing noise', 'car overheats'], 'Coolant leak'),
    (['brake pedal goes all the way to the floor', 'brake warning light is on'], 'Brake fluid leak'),
    (['brake pedal feels spongy', 'car pulls to one side when braking'], 'Worn brake caliper'),
    (['car makes a clicking noise when turning', 'car feels loose when turning'], 'Worn ball joint'),
    (['car makes a grinding noise when turning', 'car feels loose when  turning'], 'Worn wheel bearing'),
    (['car makes a popping noise when turning', 'steering wheel feels loose'], 'Worn tie rod end'),
    (['car makes a clunking noise over bumps', 'car bounces excessively'], 'Worn shock absorber')
 
]

# Working memory and agenda
working_memory = []
agenda = []

# Inference engine
def backward_chaining(symptoms):
    global working_memory, agenda
    
    working_memory.extend(symptoms)
    agenda.extend(symptoms)
    
    while agenda:
        symptom = agenda.pop()
        
        for rule in rules:
            if symptom in rule[0]:
                premise = [s for s in rule[0] if s != symptom]
                
                if all(p in working_memory for p in premise):
                    working_memory.append(rule[1])
                    agenda.append(rule[1])
    
    return working_memory

# Endpoint
@app.route('/infer', methods=['POST'])
def diagnose():
    symptoms = request.json['symptoms']
    diagnosis = backward_chaining(symptoms)
    return jsonify({'diagnosis': diagnosis})

if __name__ == '__main__':
    app.run()
