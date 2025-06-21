<h1>💬 Khizr – AI Coding Assistant (Gemini-Powered Chatbot)</h1>

  <p><strong>Khizr</strong> is an AI chatbot built using <strong>Flask</strong> and <strong>Google Gemini API</strong>, designed to serve as a versatile personal assistant with expertise in AI training, ethical hacking, coding, and general computer knowledge.</p>

  <p>It features a sleek Bootstrap-powered frontend, persistent session-based history, and a dynamic multi-conversation system.</p>

  <h2>✨ Features</h2>
  <ul>
    <li>✅ Gemini 2.0 Flash API integration</li>
    <li>✅ Persistent chat history per session</li>
    <li>✅ Multiple conversations (create, switch, resume)</li>
    <li>✅ Real-time typing animation with Markdown rendering</li>
    <li>✅ Mobile responsive dark-mode UI using Bootstrap 5</li>
    <li>✅ Secure <code>.env</code> usage with Flask sessions</li>
    <li>✅ Easy-to-deploy on Railway, Render, etc.</li>
  </ul>

  <h2>🛠️ Tech Stack</h2>
  <table>
    <tr><th>Layer</th><th>Technology</th></tr>
    <tr><td>Backend</td><td>Python + Flask</td></tr>
    <tr><td>AI Model</td><td>Google Gemini 2.0 Flash</td></tr>
    <tr><td>Frontend</td><td>HTML, CSS, Bootstrap 5</td></tr>
    <tr><td>Sessions</td><td>Flask-Session (filesystem)</td></tr>
    <tr><td>Markdown</td><td>marked.js</td></tr>
  </table>

  <h2>📁 Project Structure</h2>
  <pre><code>KhizrAI/
├── app.py                 # Flask backend logic
├── templates/
│   └── index.html         # Chat UI
├── .env                   # API keys (not committed)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
  </code></pre>

  <h2>⚙️ Installation</h2>
  <ol>
    <li><strong>Clone the repository</strong>
      <pre><code>git clone https://github.com/AhmedShaikh0/KhizrAI.git
cd KhizrAI</code></pre>
    </li>
    <li><strong>Set up virtual environment</strong>
      <pre><code>python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate</code></pre>
    </li>
    <li><strong>Install dependencies</strong>
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Create a <code>.env</code> file</strong>
      <pre><code>GOOGLE_API_KEY=your_google_gemini_api_key
FLASK_SECRET_KEY=your_flask_secret_key
PORT=5000</code></pre>
    </li>
    <li><strong>Run the app</strong>
      <pre><code>python app.py</code></pre>
    </li>
    <li><strong>Open in browser:</strong>
      <pre><code>http://localhost:5000</code></pre>
    </li>
  </ol>

  <h2>📜 Usage Instructions</h2>
  <ul>
    <li>Ask questions related to coding, AI, or ethical hacking</li>
    <li>Receive markdown/code-formatted replies</li>
    <li>Create or switch chats from the sidebar</li>
    <li>Send messages via Enter or the Send button</li>
  </ul>

  <h2>📦 <code>requirements.txt</code></h2>
  <pre><code>Flask
Flask-Session
python-dotenv
google-generativeai</code></pre>

  <p>Generate using:</p>
  <pre><code>pip freeze > requirements.txt</code></pre>

  <h2>🔐 Security Notes</h2>
  <ul>
    <li>Do not commit your <code>.env</code> file</li>
    <li>Use a strong <code>FLASK_SECRET_KEY</code> in production</li>
    <li>Use HTTPS and secure cookies when deploying publicly</li>
  </ul>

  <h2>🤝 Contributing</h2>
  <p>Pull requests are welcome! For major changes, open an issue to discuss first.</p>
  <ul>
    <li>Fork the repo</li>
    <li>Create a new branch</li>
    <li>Make your changes</li>
    <li>Submit a pull request</li>
  </ul>

