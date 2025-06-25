import logging
import hashlib
from Components.config import config

def get_logger(name="AI-PowerFull"):
    """Configure plugin logger with handlers"""
    logger = logging.getLogger(name)
    
    if not logger.handlers:  # Prevent duplicate handlers
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger

def generate_cache_key(text, target_lang="ar"):
    """Create unique hash for translation caching"""
    if not text:
        return None
        
    key_string = f"{config.plugins.AIPowerFull.api_key.value}_{target_lang}_{text}"
    return hashlib.md5(key_string.encode()).hexdigest()

def check_dependencies():
    """Verify required Python packages are installed"""
    required = ['requests', 'openai']
    missing = []
    
    try:
        import importlib
        for pkg in required:
            try:
                importlib.import_module(pkg)
            except ImportError:
                missing.append(pkg)
    except Exception as e:
        get_logger().error(f"Dependency check failed: {e}")
        return False
        
    if missing:
        get_logger().warning(f"Missing packages: {', '.join(missing)}")
        return False
        
    return True
