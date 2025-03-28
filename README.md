# 🕵️ AutoRecon LLM Agent

AutoRecon is an AI-powered reconnaissance automation framework for offensive security and Red Team operations.  
It leverages OpenLLM with local language models (e.g., Mistral, DeepSeek) to generate, execute, and adapt recon commands using prompts and real-time system state.

---

## 🔥 Features

- 🤖 Prompt-based Recon Agent powered by local LLM (OpenLLM)
- 🧠 Maintains internal state and history of commands
- 🔁 Self-adaptive loop: decides the next recon step based on output
- 🔎 Supports tools like:
  - Subdomain Enumeration: `amass`, `assetfinder`
  - Port Scanning: `naabu`, `nmap`
  - HTTP Probing: `httpx`, `whatweb`
  - Technology Detection: `wappalyzer`, `nuclei`
- 📝 CLI interface (API and Web UI coming soon)

---

## 🚀 Getting Started

### 1. Requirements

- Python 3.10+
- Linux (recommended)
- OpenLLM installed and configured
- Recon tools installed (e.g., `amass`, `naabu`, `assetfinder`, etc.)

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start your OpenLLM server

> Example with a compatible model:
```bash
export HF_TOKEN=your_huggingface_token
openllm start mistral --model-id deepseek-ai/deepseek-coder-6.7b-instruct
```

### 4. Run AutoRecon

```bash
python main.py
```

---

## 📂 Project Structure

```
autorecon/
│
├── main.py                  # Entry point
├── llm/
│   └── openllm_agent.py     # Interface to OpenLLM (HTTP client)
│
├── agent/
│   ├── executor.py          # Runs system commands
│   ├── prompt_engine.py     # Generates contextual prompts
│   ├── state.py             # Maintains recon state
│   ├── history.py           # Stores command/result history
│   └── tools.py             # Recon tool registry
│
├── data/
│   └── targets.json         # Optional storage for scanned targets
```

---

## 🧠 Example Prompt Used

```text
Context: You are a recon agent. Target domain: example.com.
Objective: Discover subdomains, IPs and exposed services.
Tools available: assetfinder, amass, naabu, httpx.

History: none.
Current stage: start.

What command should I execute next? 
Respond only with the shell command.
```

---

## 🛡️ Use Cases

- Red Team recon automation
- Pentest intelligence collection
- OSINT operations
- Recon-as-a-Loop via LLM

---

## 📌 Roadmap

- [x] LLM agent with prompt-based command generation
- [x] Real-time command execution
- [ ] Web UI with scan control
- [ ] CVE/Exploit stage after recon
- [ ] Integration with reporting tools (HTML/PDF)

---

## ⚠️ Disclaimer

This project is for **educational and authorized security testing purposes only**.  
Do not use it on unauthorized systems.

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Developed by Joas Antonio dos Santos 🚀  
