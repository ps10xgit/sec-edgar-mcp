import os
from dotenv import load_dotenv


def initialize_config():
    """Initialize the SEC EDGAR configuration"""
    load_dotenv()

    sec_edgar_user_agent = os.getenv("SEC_EDGAR_USER_AGENT")
    if not sec_edgar_user_agent:
        raise ValueError("SEC_EDGAR_USER_AGENT environment variable is not set.")

    return sec_edgar_user_agent
