class MCPMessage:
    def __init__(self, trace_id, sender, receiver, type, payload):
        self.trace_id = trace_id
        self.sender = sender
        self.receiver = receiver
        self.type = type
        self.payload = payload
    