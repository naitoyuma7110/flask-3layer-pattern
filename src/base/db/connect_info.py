from flask import Flask
import yaml
import os
from pathlib import Path

db_config: dict | None = None


def get_db_connect_info(app:Flask):
    return get_local()

def get_local():
    global db_config
    
    if db_config is None:
        # localのDB接続情報を取得
        current_dir = Path(__file__).resolve().parent
        config_path = current_dir.parents[1] / 'db_config.yaml'
        with open(config_path, "r", encoding='utf-8') as yamlfile:
            db_config = yaml.safe_load(yamlfile)
        
    return  db_config['database']['uri']

# TODO：本番用接続情報の取得