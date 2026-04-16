#!/usr/bin/env python3
"""
GEOX MCP Server Entry Point
═══════════════════════════════════════════════════════════════════════════════

FastMCP Cloud deployment entrypoint.
Sets PYTHONPATH correctly for the geox package.

DITEMPA BUKAN DIBERI — Forged, Not Given
"""

import os
import sys

# In Docker: /app/geox_mcp_server.py, geox package is at /app/geox/
# So SCRIPT_DIR=/app is the parent directory containing geox/
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Set PYTHONPATH so 'geox' package is found
os.environ["PYTHONPATH"] = SCRIPT_DIR

# Now we can import the geox module
sys.path.insert(0, SCRIPT_DIR)

from geox.mcp.fastmcp_server import mcp

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8081))
    host = os.environ.get("HOST", "127.0.0.1")

    print(f"Starting GEOX MCP Server on {host}:{port}")
    print(f"PYTHONPATH={os.environ.get('PYTHONPATH')}")

    app = mcp.streamable_http_app()
    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level="info",
        proxy_headers=True,
    )
