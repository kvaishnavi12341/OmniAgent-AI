import json
from datetime import datetime
import os

class Logger:
    def log(self, data):
        try:
            data["timestamp"] = str(datetime.now())

            # ✅ Absolute path fix
            base_dir = os.path.abspath(os.getcwd())
            log_path = os.path.join(base_dir, "data", "logs.json")

            os.makedirs(os.path.dirname(log_path), exist_ok=True)

            with open(log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(data) + "\n")

            print("LOG WRITTEN ✅:", log_path)

        except Exception as e:
            print("LOGGER ERROR:", e)
'''
import json
from datetime import datetime

class Logger:
    def log(self, data):
        data["timestamp"] = str(datetime.now())

        #print(str(data).encode("utf-8", "ignore").decode())

        with open("data/logs.json", "a") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")
'''