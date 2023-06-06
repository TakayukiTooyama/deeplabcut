import torch
import os
import deeplabcut
from model import DLCModel


class Training(DLCModel):
    def __init__(self):
        super().__init__()
        os.environ["DLClight"] = True

    def create_training_dataset(self):
        if torch.cuda.is_available():
            deeplabcut.create_training_dataset(
                self.config_path, net_type="resnet_101", augmenter_type="imgaug"
            )
        else:
            raise "GoogleColabのGPUを活用してください。"

    def train_network(self):
        deeplabcut.train_network(
            self.config_path,
            shuffle=1,
            max_snapshots_to_keep=5,
            displayiters=100,
            maxiters=50000,
            saveiters=2500,
        )

    def evaluate_network(self):
        deeplabcut.evaluate_network(self.config_path, plotting=True)

    def analyze_videos(self):
        deeplabcut.analyze_videos(
            self.config_path,
            self.video_file_list,
            videotype=self.video_type,
            save_as_csv=True,
        )

    def plot_trajectories(self):
        deeplabcut.plot_trajectories(
            self.config_path, self.video_file_list, videotype=self.video_type
        )

    def create_labeled_video(self):
        deeplabcut.create_labeled_video(
            self.config_path,
            self.video_file_list,
            videotype=self.video_type,
            draw_skeleton=True,
        )
