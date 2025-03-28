# agent/state.py
class ReconState:
    def __init__(self, domain):
        self.domain = domain
        self.subdomains = []
        self.ips = []
        self.ports = []
        self.technologies = []
        self.stage = "start"

    def update(self, key, value):
        if hasattr(self, key):
            setattr(self, key, value)
