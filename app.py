from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize conversation history as an empty list
conversation_history = []

@app.route('/')
def home():
    return render_template('index.html', conversation=conversation_history)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']

    # Implement more sophisticated chatbot logic here based on user input
    chatbot_response = process_user_input(user_message)

    # Store the current conversation in the history
    conversation_history.append({'user': user_message, 'chatbot': chatbot_response})

    return render_template('index.html', conversation=conversation_history)

def process_user_input(user_message):
    # Example: Check if user mentions having a fever
    if 'fever' in user_message.lower():
        return "Assistant:It's important to stay hydrated and get plenty of rest. If your symptoms persist, consider consulting a healthcare professional."

    if 'cold' in user_message.lower():
        return "Assistant:Drink hot water and eat honey. Wear mask so that it should not spread to others. Wear sweater. If your symptoms persist, consider consulting a healthcare professional."

    if 'joint pain' in user_message.lower():
        return "Assistant:take painkiller & apply heating pads or ice packs which may help to relieve arthritis pain."

    if 'headache' in user_message.lower():
        return "Assistant:drink coffe or tea. have a good sleep. dont skip meals."

    if 'stomach' in user_message.lower():
        return "Assistant:reduce intake of coffe,tea,alcohol...dont eat sweet food...try to put heatpad or hot towels on stomach"

    if 'eyes' in user_message.lower():
        return "Assistant:clean your eyes with warm water... avoid watching mobile phones."

    if 'dizzyness' in user_message.lower():
        return "Assistant:drink plenty of fluids especially water..get plenty of rest..eat glucose..."
    # Add more conditions based on different user inputs

    # Default response
    return "Assistant:Hi..I'm here to help! How can I assist you today?"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
