import logging
import os
from Components.config import config

def get_logger(name="AI-PowerFull"):
    """Configure a logger with file and console output"""
    logger = logging.getLogger(name)
    
    if not logger.handlers:  # Prevent duplicate handlers
        logger.setLevel(logging.DEBUG)
        
        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        ))
        logger.addHandler(ch)
        
        # File handler (logs to /tmp/)
        log_file = "/tmp/ai_powerfull.log"
        fh = logging.FileHandler(log_file)
        fh.setFormatter(logging.Formatter(
            '[%(asctime)s] %(levelname)s: %(message)s'
        ))
        logger.addHandler(fh)
        
    return logger

def validate_api_key(key):
    """Basic OpenAI key validation"""
    return key.startswith("sk-") and len(key) == 51
