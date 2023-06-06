import deeplabcut
from model import DLCModel


class Labeling(DLCModel):
    # CSVファイルからh5ファイルに変換
    def convert_csv(self):
        deeplabcut.convertcsv2h5(f"{self.project_folder_path}/config.yaml")

    # ラベリング結果の確認
    def check_labels(self):
        deeplabcut.check_labels(self.config_path, visualizeindividuals=False)
