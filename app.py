import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

####
# step 1) create a databse from scratch code
# database validation part -> if false run db creation
###
# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Now import and run the server
import uvicorn
from server.core.config import config

from server.db_manager.creation import initialize_db
initialize_db()

if __name__ == "__main__":
    uvicorn.run(
        "server.main:app",
        host=config.host,
        port=config.port,
        log_level=config.log_level.lower(),
        reload=True
    )
