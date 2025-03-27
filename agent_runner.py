import requests
from config import get_api_key

def run_agent(agent_id, input_data):
    """Execute an AI agent on aiXplain platform."""
    url = f"https://api.aixplain.com/agents/{agent_id}/run"
    headers = {"Authorization": f"Bearer {get_api_key()}"}
    payload = {"input": input_data}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

if __name__ == "__main__":
    agents = ["agent_1", "agent_2", "agent_3"]  # Replace with actual agent IDs
    input_data = {"text": "Hello, AI!"}
    
    for agent in agents:
        result = run_agent(agent, input_data)
        print(f"Agent {agent} Output: {result}")
