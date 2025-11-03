import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Now import and run the server
import uvicorn
from server.core.config import config

if __name__ == "__main__":
    uvicorn.run(
        "server.main:app",
        host=config.host,
        port=config.port,
        log_level=config.log_level.lower(),
        reload=True
    )
