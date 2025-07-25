from core.base_agent import BaseAgent
from core.utils import retrieve_relevant_chunks
from core.mcp import MCPMessage

class RetrievalAgent(BaseAgent):
    def __init__(self):
        super().__init__("RetrievalAgent")

    def handle(self, mcp_msg: MCPMessage) -> MCPMessage:
        return self.process_message(mcp_msg)

    def process_message(self, mcp_msg: MCPMessage) -> MCPMessage:
        chunks = mcp_msg.payload.get("chunks", [])
        query = mcp_msg.payload.get("query", "")
        top_chunks = retrieve_relevant_chunks(query, chunks)

        self.log(f"📦 Retrieved {len(top_chunks)} relevant chunks.")

        return self.reply_to(
            mcp_msg,
            "LLMResponseAgent",
            "RETRIEVAL_RESULT",
            {"top_chunks": top_chunks, "query": query}
)

