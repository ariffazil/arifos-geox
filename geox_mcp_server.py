#!/usr/bin/env python3
"""
GEOX MCP Server Entry Point
═══════════════════════════════════════════════════════════════════════════════

FastMCP Cloud deployment entrypoint.
Uses 'fastmcp run' command which handles Python path correctly.

DITEMPA BUKAN DIBERI — Forged, Not Given

Usage:
    fastmcp run geox_mcp_server.py --transport http --host 127.0.0.1 --port 8081
"""

from geox.mcp.fastmcp_server import mcp

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8081))
    host = os.environ.get("HOST", "127.0.0.1")

    print(f"Starting GEOX MCP Server on {host}:{port}")

    app = mcp.streamable_http_app()
    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level="info",
        proxy_headers=True,
    )
