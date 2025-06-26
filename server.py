from mcp.server.fastmcp import FastMCP
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
    mcp.run(transport="streamable-http",host="0.0.0.0",port=8000,debug=True,fast=True)

