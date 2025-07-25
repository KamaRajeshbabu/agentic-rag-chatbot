from typing import Any, Dict

class MCPMessage:
    def __init__(self, content: Any, metadata: Dict[str, Any] = None):
        self.content = content
        self.metadata = metadata or {}

    def get(self) -> Any:
        return self.content

    def add_metadata(self, key: str, value: Any):
        self.metadata[key] = value

    def get_metadata(self, key: str, default=None) -> Any:
        return self.metadata.get(key, default)

    def __repr__(self):
        return f"<MCPMessage content={str(self.content)[:60]}... metadata={self.metadata}>"
