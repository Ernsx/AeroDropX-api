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

@app.route('/')
def home():
    return "Main endpoint for AeroDropX AI Airdrop Tracker"

@app.route('/mcp', methods=['GET', 'POST', 'OPTIONS'])
def mcp_endpoint():
    tools_list = [
        {"name": "track_airdrops", "description": "Melacak jadwal airdrop web3 terbaru", "inputSchema": { "type": "object", "properties": {} }},
        {"name": "auto_tweet", "description": "Otomatisasi postingan Twitter/X", "inputSchema": { "type": "object", "properties": {} }},
        {"name": "wallet_checker", "description": "Cek syarat dompet untuk airdrop", "inputSchema": { "type": "object", "properties": {} }},
        {"name": "task_manager", "description": "Mengatur jadwal tugas harian airdrop", "inputSchema": { "type": "object", "properties": {} }}
    ]
    prompts_list = [
        {"name": "generate_thread", "description": "Bikin thread Twitter viral buat campaign", "arguments": []},
        {"name": "analyze_project", "description": "Analisis potensi project crypto baru", "arguments": []}
    ]
    resources_list = [
        {"name": "Airdrop Database", "uri": "file:///airdrop_db", "description": "Database project airdrop", "mimeType": "application/json"}
    ]

    if request.method == 'GET':
        return jsonify({
            "serverInfo": {
                "name": "AeroDropX Agent Server",
                "version": "1.0.0"
            },
            "tools": tools_list,
            "prompts": prompts_list,
            "resources": resources_list
        })

    if request.method == 'POST':
        req_data = request.get_json(silent=True) or {}
        req_id = req_data.get("id", 1)
        method = req_data.get("method", "")

        if method == "tools/list":
            return jsonify({"jsonrpc": "2.0", "id": req_id, "result": {"tools": tools_list}})
        elif method == "prompts/list":
            return jsonify({"jsonrpc": "2.0", "id": req_id, "result": {"prompts": prompts_list}})
        elif method == "resources/list":
            return jsonify({"jsonrpc": "2.0", "id": req_id, "result": {"resources": resources_list}})
        else:
            return jsonify({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {
                        "name": "AeroDropX Agent Server",
                        "version": "1.0.0"
                    },
                    "capabilities": {
                        "prompts": {},
                        "resources": {},
                        "tools": {}
                    }
                }
            })

@app.route('/.well-known/agent-card.json', methods=['GET', 'OPTIONS'])
def a2a_endpoint():
    return jsonify({
        "name": "aerodropx",
        "version": "1.0.0",
        "description": "AeroDropX AI is an automated agent for airdrop hunting and web3 social media management.",
        "skills": [
            {"name": "Airdrop Tracking", "description": "Melacak peluang airdrop", "category": "blockchain/airdrop_tracking"},
            {"name": "Social Media Auto", "description": "Otomatisasi Twitter", "category": "automation/social_media"},
            {"name": "Task Management", "description": "Atur tugas harian", "category": "productivity/task_management"}
        ]
    })

@app.route('/oasf', methods=['GET', 'OPTIONS'])
def oasf_endpoint():
    return jsonify({
        "name": "aerodropx",
        "version": "v1.0.0",
        "skills": [
            "blockchain/airdrop_tracking",
            "automation/social_media",
            "productivity/task_management"
        ],
        "domains": [
            "web3/community_building",
            "automation/workflow",
            "crypto/research"
        ]
    })
