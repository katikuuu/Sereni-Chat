from typing import Dict
import json

class JsonHandler:
    @staticmethod
    def load_json(json_file_path: str) -> Dict:
        # JSONファイルを読み込み辞書型に格納して返す
        with open(json_file_path, 'r') as f:
            return json.load(f)
        
    @staticmethod
    def save_json(data: Dict, new_data: Dict, json_file_path: str) -> None:
        # 辞書型のデータ同士を結合する
        data.update(new_data)
        # jsonファイルの書き出し
        with open(json_file_path, 'w') as f:
            json.dump(data, f, indent=4)