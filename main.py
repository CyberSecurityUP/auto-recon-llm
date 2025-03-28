# main.py
from llm.openllm_agent import LLMReconAgent
from agent.executor import run_command
from agent.state import ReconState

def main():
    print("=== 🕵️ AutoRecon LLM Agent ===")

    # 1. Get target domain
    domain = input("🔍 Enter the target domain (e.g., example.com): ").strip()
    if not domain:
        print("⚠️ Domain is required. Exiting.")
        return

    # 2. Get recon objective
    objective = input("🎯 Describe your recon objective (e.g., find subdomains and open ports): ").strip()
    if not objective:
        objective = "Discover subdomains, IPs and technologies."

    # 3. Get available tools
    tools = input("🧰 List available tools (comma-separated, e.g., amass,naabu,httpx): ").strip()
    if not tools:
        tools = "amass,assetfinder,httpx"

    tools_formatted = ", ".join([t.strip() for t in tools.split(",")])

    # Initialize recon agent
    state = ReconState(domain)
    agent = LLMReconAgent()

    # Build dynamic prompt
    prompt = f"""
You are a Recon agent.

Target domain: {domain}
Objective: {objective}
Available tools: {tools_formatted}

Current stage: {state.stage}
No previous history.

What shell command should be executed now to start the recon process?
Return ONLY the shell command.
"""

    print("\n🧠 Sending prompt to LLM...\n")
    command = agent.generate_command(prompt)

    print(f"💡 Suggested command: \033[92m{command}\033[0m")

    confirm = input("\n❓ Do you want to run this command? (y/n): ").strip().lower()
    if confirm != 'y':
        print("❌ Execution canceled.")
        return

    print("\n🚀 Running command...")
    result = run_command(command)

    print("\n📥 Command Output:")
    print("-" * 50)
    print(result["stdout"])
    print("-" * 50)

    if result["stderr"]:
        print("\n⚠️ Errors:")
        print(result["stderr"])

if __name__ == "__main__":
    main()
