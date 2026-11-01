from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Study Notes")
notes = {}


@mcp.tool()
def add_note(topic: str, text: str) -> str:
    notes[topic] = text
    return f"Saved notes about {topic}"

@mcp.tool()
def search_notes(topic: str) -> str:
    if topic in notes:
        return f"{topic}: {notes[topic]}"
    return f"no notes found for {topic}"

if __name__ == "__main__":
    mcp.run(transport="stdio")

