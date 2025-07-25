from core.base_agent import BaseAgent
from core.utils import generate_response
from core.mcp import MCPMessage

class LLMResponseAgent(BaseAgent):
    def __init__(self):
        super().__init__("LLMResponseAgent")

    def handle(self, mcp_msg: MCPMessage) -> MCPMessage:
        return self.process_message(mcp_msg)

    def process_message(self, mcp_msg: MCPMessage) -> MCPMessage:
        chunks = mcp_msg.payload.get("top_chunks", [])
        query = mcp_msg.payload.get("query", "")

        if not chunks:
            self.log("⚠️ No chunks to process.")
            return self.reply_to(mcp_msg, "User", "LLM_RESPONSE", {
                "response": "⚠️ No relevant content found."
            })

        context = "\n".join(chunks)
        prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
        self.log("🧠 Sending prompt to LLM...")
        response = generate_response(prompt)

        return self.reply_to(
            mcp_msg,
            "User",
            "LLM_RESPONSE",
           {"response": response}
)

