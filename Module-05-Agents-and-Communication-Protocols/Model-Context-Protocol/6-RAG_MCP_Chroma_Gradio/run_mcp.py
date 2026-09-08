import os
import subprocess
import re

# Optional: Force UTF-8 environment (good for older Windows terminals)
env = os.environ.copy()
env["PYTHONIOENCODING"] = "utf-8"

def run_mcp_and_get_url(script_path: str, object_name: str = "mcp"):
    process = subprocess.Popen(
        ["fastmcp", "run", f"{script_path}:{object_name}", "--transport","sse"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=1,
        text=True,
        encoding="utf-8",  # 🔧 Force utf-8 output
        errors="replace",  # 🔧 Replace problematic characters
        env=env # Replaces problematic characters
    )

    url = None
    try:
        for line in process.stdout:
            print(line.strip())  # Show logs

            match = re.search(r"http://[^\s]+", line)
            if match:
                url = match.group(0)
                url = url.replace("0.0.0.0", "localhost")
                full_url= f"{url}/sse"
                print(f"\n✅ Found MCP Server URL: {full_url}")
                try:
                    with open(".env", "r") as f:
                        lines = f.readlines()
                except FileNotFoundError:
                    lines = []

                if not any("MCP_SERVER_URL=" in line for line in lines):
                    with open(".env", "a") as f:
                        f.write(f'\nMCP_SERVER_URL="{full_url}"')
                        print(f"✅ MCP_SERVER_URL added to .env: {full_url}")
                else:
                    print("ℹ️ MCP_SERVER_URL already exists in .env")

        if not url:
            print("❌ URL not found in logs.")
    except KeyboardInterrupt:
        process.terminate()
        print("⛔ Server stopped manually.")

    return url

# Example usage
if __name__ == "__main__":
    run_mcp_and_get_url("mcp_server.py")
