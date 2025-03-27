import os

def deploy():
    """Simulates deployment of the multi-agent system."""
    print("Starting deployment...")
    os.system("python agent_runner.py")
    print("Deployment complete.")

if __name__ == "__main__":
    deploy()
