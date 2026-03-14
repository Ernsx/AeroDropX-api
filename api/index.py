from flask import Flask, jsonify, request

app = Flask(__name__)

def add_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.after_request
def after_request(response):
    return add_cors(response)

# --- 1. HALAMAN UTAMA (HTML) ---
@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AeroDropX AI Agent</title>
        <style>
            body {
                background-color: #0d1117;
                color: #c9d1d9;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                padding: 50px;
                border: 1px solid #30363d;
                border-radius: 15px;
                background-color: #161b22;
                box-shadow: 0 8px 24px rgba(0,0,0,0.5);
                max-width: 500px;
            }
            h1 { color: #58a6ff; margin-bottom: 10px; }
            p { font-size: 16px; line-height: 1.5; color: #8b949e; margin-bottom: 30px; }
            .status-badge {
                padding: 8px 16px; background-color: #238636; color: #ffffff;
                border-radius: 20px; font-size: 14px; font-weight: bold;
                display: inline-block; border: 1px solid #2ea043;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AeroDropX AI</h1>
            <p>Automated AI agent specializing in web3 airdrop tracking, task management, and social media automation on the Base network.</p>
            <div class="status-badge">🟢 System Online & Healthy (Rank 1 Configuration)</div>
        </div>
    </body>
    </html>
    """
    return html_content

# --- 2. ENDPOINT MCP (TANPA RESOURCES) ---
@app.route('/mcp', methods=['GET', 'POST', 'OPTIONS'])
def mcp_endpoint():
    server_info = {
        "name": "AeroDropX Agent Server",
        "version": "1.0.0",
        "website": "https://aero-drop-x-api.vercel.app",
        "description": "Airdrop tracking and web3 automation agent on Base network"
    }
    tools = [
        {"name": "track_airdrops", "description": "Track latest web3 airdrops", "inputSchema": {"type": "object","properties": {}}},
        {"name": "auto_tweet", "description": "Automate X/Twitter posts", "inputSchema": {"type": "object","properties": {}}},
        {"name": "wallet_checker", "description": "Check wallet eligibility", "inputSchema": {"type": "object","properties": {}}},
        {"name": "task_manager", "description": "Manage daily airdrop tasks", "inputSchema": {"type": "object","properties": {}}}
    ]
    prompts = [
        {"name": "generate_thread", "description": "Generate viral X thread", "arguments": []},
        {"name": "analyze_project", "description": "Analyze new crypto project potential", "arguments": []}
    ]
    
    if request.method == 'GET':
        return jsonify({
            "protocolVersion": "2024-11-05",
            "serverInfo": server_info,
            "tools": tools,
            "prompts": prompts,
            "resources": []  # KOSONG SEPERTI SUKMAXS
        })

    req_data = request.get_json(silent=True) or {}
    req_id = req_data.get("id", 1)
    method = req_data.get("method", "")

    if method == "tools/list":
        result = {"tools": tools}
    elif method == "prompts/list":
        result = {"prompts": prompts}
    else:
        result = {
            "protocolVersion": "2024-11-05",
            "serverInfo": server_info,
            "capabilities": {"tools": {},"prompts": {},"resources": {}}
        }

    return jsonify({"jsonrpc": "2.0", "id": req_id, "result": result})

# --- 3. ENDPOINT A2A (SUNTIKAN JAMES RANK 1) ---
@app.route('/.well-known/agent-card.json', methods=['GET','OPTIONS'])
def a2a_endpoint():
    return jsonify({
        "id": "aerodropx",
        "name": "aerodropx",
        "version": "1.0.0",
        "description": "Automated AI agent for web3 airdrop tracking and social media management.",
        "website": "https://aero-drop-x-api.vercel.app",
        "url": "https://aero-drop-x-api.vercel.app",
        "documentation_url": "https://aero-drop-x-api.vercel.app",
        "provider": {
            "organization": "AeroDropX Labs",
            "url": "https://aero-drop-x-api.vercel.app"
        },
        "registrations": [
            {
                "agentId": 22332,
                "agentRegistry": "eip155:8453:0x8004A169FB4a3325136EB29fA0ceB6D2e539a432"
            }
        ],
        "supportedTrust": ["reputation", "crypto-economic", "tee-attestation"],
        "skills": [
            {"name": "Airdrop Tracking", "description": "Track airdrop opportunities", "category": "blockchain/airdrop_tracking"},
            {"name": "Social Media Auto", "description": "Twitter automation", "category": "automation/social_media"},
            {"name": "Task Management", "description": "Manage daily tasks", "category": "productivity/task_management"}
        ]
    })

# --- 4. ENDPOINT OASF (DIBIARKAN DI KODE TAPI HAPUS DI METADATA) ---
@app.route('/oasf', methods=['GET','OPTIONS'])
def oasf_endpoint():
    return jsonify({
        "id": "aerodropx",
        "name": "aerodropx",
        "version": "v0.8.0",
        "description": "Main endpoint for AeroDropX AI",
        "website": "https://aero-drop-x-api.vercel.app",
        "protocols": ["mcp","a2a"],
        "capabilities": ["airdrop_tracking", "social_automation", "task_management"],
        "skills": [
            {"name": "blockchain/airdrop_tracking","type": "operational"},
            {"name": "automation/social_media","type": "operational"},
            {"name": "productivity/task_management","type": "operational"}
        ],
        "domains": [
            "web3/community_building",
            "automation/workflow",
            "crypto/research"
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
