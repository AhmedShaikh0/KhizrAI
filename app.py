from flask import Flask, render_template, request, jsonify, session
import os
import uuid
from dotenv import load_dotenv
from flask_session import Session
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-2.0-flash-exp')

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret")
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = "./flask_session"
Session(app)

# System prompt with Khizr roles
SYSTEM_PROMPT = (
    "You are Khizr, an expert AI assistant.\n"
    "Roles:\n"
    "- Artificial Intelligence Trainer\n"
    "- Ethical Hacker Trainer\n"
    "- Helpful AI coding assistant\n"
    "- Full-fledged computer and internet expert\n"
    "- Respond using clear explanations, markdown formatting, and syntax-highlighted code blocks\n"
    "- Always include examples where appropriate\n"
    "- If user asks 'Who are you?', say: 'I am Khizr, your AI coding assistant.'"
)

# Initialize a new chat session
def init_chat(title="New Chat"):
    chat_id = str(uuid.uuid4())
    session['conversations'][chat_id] = {
        "title": title,
        "history": [{"role": "user", "parts": [SYSTEM_PROMPT]}]
    }
    session['current_chat_id'] = chat_id
    return chat_id

@app.route('/')
def index():
    if 'conversations' not in session:
        session['conversations'] = {}
        init_chat("First Chat")
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_route():
    message = request.json.get('message', '').strip()
    if not message:
        return jsonify({'reply': "Please enter a message."})

    chat_id = session.get('current_chat_id')
    if not chat_id or chat_id not in session['conversations']:
        chat_id = init_chat("Recovered Chat")

    conv = session['conversations'][chat_id]

    # Start chat with stored history
    chat = model.start_chat(history=conv["history"])
    try:
        response = chat.send_message(message)
        reply = response.text.strip()
    except Exception as e:
        reply = f"An error occurred: {str(e)}"

    # Update chat history
    conv["history"].append({"role": "user", "parts": [message]})
    conv["history"].append({"role": "model", "parts": [reply]})

    return jsonify({'reply': reply})

@app.route('/history')
def get_history():
    chat_id = session.get('current_chat_id')
    if not chat_id or chat_id not in session['conversations']:
        return jsonify([])

    history = session['conversations'][chat_id]["history"][1:]  # skip system prompt
    messages = []
    for i in range(0, len(history), 2):
        if i+1 < len(history):
            user_msg = history[i]["parts"][0]
            bot_msg = history[i+1]["parts"][0]
            messages.append({"user": user_msg, "bot": bot_msg})
    return jsonify(messages)

@app.route('/conversations')
def get_conversations():
    return jsonify([
        {"id": cid, "title": conv["title"]}
        for cid, conv in session.get('conversations', {}).items()
    ])

@app.route('/switch', methods=['POST'])
def switch_conversation():
    chat_id = request.json.get('chat_id')
    if chat_id in session.get('conversations', {}):
        session['current_chat_id'] = chat_id
        return jsonify({"status": "ok"})
    return jsonify({"status": "error", "message": "Chat not found"}), 404

@app.route('/new', methods=['POST'])
def new_conversation():
    title = request.json.get('title', 'New Chat')
    new_id = init_chat(title)
    return jsonify({"chat_id": new_id})

if __name__ == "__main__":
    os.makedirs(app.config["SESSION_FILE_DIR"], exist_ok=True)
    app.run(debug=True)
