from mcp.server.fastmcp import FastMCP
import os
os.environ["FASTMCP_HOST"] = "0.0.0.0"
os.environ["FASTMCP_PORT"] = "8000"

mcp = FastMCP("server")
@mcp.tool()
def getinformation(topic:str)->str:
    """
    Get information about the topic,
    Args:
    topic: information of topic
    """
    return f"information about {topic}"
if __name__ == "__main__":
    mcp.run(transport="streamable-http")



