import glob


class DLCModel:
    def __init__(self):
        self.project_name = "RunAnalysis"
        self.author = "TakayukiTooyama"
        self.project_path = f"/Users/takayuki/Project/deeplabcut"
        self.project_folder_name = f"{self.project_name}-{self.author}-2023-06-04"
        self.project_folder_path = f"{self.project_path}/{self.project_folder_name}"
        self.config_path = f"{self.project_folder_path}/config.yaml"
        self.video_file_list = []

    def fetch_video_file_list(self):
        files = glob.glob(f"{self.project_path}/test_video/*.mov")
        for file in files:
            self.video_file_list.append(file)
