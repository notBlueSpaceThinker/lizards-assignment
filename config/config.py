"""
Сontains model configurations
and useful constants.
"""
from pathlib import Path
import yaml

PROJECT_ROOT = Path(__file__).parent.parent
CONFIG_PATH = PROJECT_ROOT / "config"
DATA_PATH = PROJECT_ROOT / "data"

RANDOM_STATE = 777

class DecisionTreeConfig:
    def __init__(self):
        with open(CONFIG_PATH / "model_config.yaml", "r") as f:
            self.params = yaml.safe_load(f)['DecisionTreeConfig']
