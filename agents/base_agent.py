from core.mcp import MCPMessage

class BaseAgent:
    def __init__(self, name):
        self.name = name

    def log(self, message):
        if isinstance(message, MCPMessage):
            print(f"[{self.name}] received ➜ {message.type} from {message.sender} (trace_id={message.trace_id})")
        else:
            print(f"[{self.name}] {message}")

    def handle(self, mcp_msg):
        if not isinstance(mcp_msg, MCPMessage):
            raise TypeError(f"[{self.name}] Expected MCPMessage, got {type(mcp_msg).__name__}")
        result = self.process_message(mcp_msg)
        if not isinstance(result, MCPMessage):
            raise TypeError(f"[{self.name}] process_message returned {type(result).__name__}, expected MCPMessage")
        return result

    def reply_to(self, incoming, receiver, msg_type, payload):
        if not isinstance(incoming, MCPMessage):
            raise TypeError(f"[{self.name}] Expected incoming MCPMessage, got {type(incoming).__name__}")
        return MCPMessage(
            trace_id=incoming.trace_id,
            sender=self.name,
            receiver=receiver,
            type=msg_type,
            payload=payload
        )

    def process_message(self, mcp_msg):
        raise NotImplementedError("process_message must be implemented by subclass")
