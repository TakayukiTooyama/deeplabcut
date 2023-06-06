import os
import re
import deeplabcut
from pathlib import Path
import glob
from model import DLCModel


class SetupDLC(DLCModel):
    def __init__(self):
        super().__init__()

    def fetch_video_file_list(self):
        files = glob.glob(f"{self.project_path}/test_video/*.mov")
        for file in files:
            self.video_file_list.append(file)

    def create_project(self):
        deeplabcut.create_new_project(
            self.project_name, self.author, self.video_file_list, copy_videos=True
        )

    def overwrite_config_yaml(self):
        if not os.path.isfile(self.config_path):
            raise FileNotFoundError("config.yamlファイルがありません。")

        # configファイルから指定したビデオのパスを取得
        read_config = Path(self.config_path).read_text()
        video_sets = re.findall(r"video_sets:[\s\S]*bodyparts:", read_config)

        # configテンプレートとビデオのパスを上書き
        read_template_config = Path(f"{self.project_path}/config.yaml").read_text()
        content = re.sub(
            r"video_sets:[\s\S]*bodyparts:", video_sets[0], read_template_config
        )
        write_path = Path(self.config_path)
        write_path.write_text(content)
