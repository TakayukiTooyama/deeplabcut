import deeplabcut
from model import DLCModel


class ReTraining(DLCModel):
    def __init__(self):
        super().__init__()
        self.videos_path = [f"{self.project_folder_path}/videos"]

    def add_new_videos(self):
        deeplabcut.add_new_videos(
            self.config_path,
            self.video_file_list,
            copy_videos=True,
            extract_frames=True,
        )

    def extract_outlier_frames(self):
        deeplabcut.extract_outlier_frames(
            self.config_path, self.videos_path, outlieralgorithm="jump", epsilon=5
        )

    def relabeling(self):
        deeplabcut.refine_labels(self.config_path)

    def merge_datasets(self):
        deeplabcut.merge_datasets(self.config_path)

    def check_labels(self):
        deeplabcut.check_labels(self.config_path, visualizeindividuals=False)
