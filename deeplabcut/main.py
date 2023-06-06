import dlc_setup
import dlc_labeling
import dlc_training
import dlc_re_training


class DeepLabCutTraining:
    def main():
        setup = dlc_setup.SetupDLC()
        setup.fetch_video_file_list()
        setup.create_project()
        setup.overwrite_config_yaml()

        labeling = dlc_labeling.Labeling()
        labeling.convert_csv()
        labeling.check_labels()

        training = dlc_training.Training()
        training.create_training_dataset()
        training.train_network()
        training.evaluate_network()
        training.analyze_videos()
        training.plot_trajectories()
        training.create_labeled_video()

        re_training = dlc_re_training.ReTraining()
        re_training.add_new_videos()
        re_training.extract_outlier_frames()
        re_training.relabeling()
        re_training.merge_datasets()
        re_training.check_labels()


if __name__ == "__main__":
    deeplabcut_training = DeepLabCutTraining()
    deeplabcut_training.main()
