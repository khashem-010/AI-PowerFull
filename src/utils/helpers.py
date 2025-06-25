import logging
import hashlib
from Components.config import config

def get_logger():
    """Configure plugin logger"""
    logger = logging.getLogger("AI-PowerFull")
    logger.setLevel(logging.DEBUG)
    
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    logger.addHandler(handler)
    
    return logger

def create_cache_key(text, target_lang="ar"):
    """Generate MD5 hash for translation caching"""
    return hashlib.md5(
        f"{config.plugins.AIPowerFull.api_key.value}_{target_lang}_{text}".encode()
    ).hexdigest()

def check_dependencies():
    """Verify required packages are installed"""
    try:
        import requests
        import openai
        return True
    except ImportError as e:
        get_logger().error(f"Missing dependency: {str(e)}")
        return False
