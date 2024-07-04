import os
import cv2
from pathlib import Path
class FrameExtractor:
    def __init__(self, vid, out_dir, img_frmt, required_frame_rate, start_from_seconds, img_width, verbose):
        self.vid = vid
        self.out_dir = out_dir
        self.img_frmt = img_frmt
        self.required_frame_rate = required_frame_rate or 1
        self.start_from_seconds = start_from_seconds or 0
        self.img_width = img_width
        self.verbose = verbose

    def create_dir_if_not_exists(self, dirname: str):
        """Create a directory with the specified name inside the 'out_dir' 
        directory if it doesn't exist.

        :param dirname: Name of the directory to be created.
        :return: created dir path.
        """
        target_dir = os.path.join(self.out_dir, dirname)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        else:
            return target_dir
        return target_dir

    def extract_frames(self):
        """Extract frames from a video."""
        count = 1

        vid_cap = cv2.VideoCapture(str(Path(self.vid)))
        frames = int(vid_cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
        fps = int(vid_cap.get(cv2.CAP_PROP_FPS))

        frames_to_be_extracted=(int(frames / fps))//(self.required_frame_rate)
        try:
            seconds = int(frames / fps)
        except ZeroDivisionError as ex:
            print("Unable to detect seconds")
            seconds = 1

        if self.verbose:
            print("======================================")
            print(f"[OUT FILE DIRECTORY] - {self.out_dir}")
            print(f"[TOTAL FRAMES] - {frames}")
            print(f"[FRAMES PER SECOND] - {fps}")
            print(f"[VIDEO LENGTH] - {seconds} seconds")
            print("frames to be extracted = ", frames_to_be_extracted)

        # start from 1 if 'start_from_seconds' is not passed.
        sec = int(self.start_from_seconds)
        vid_cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
        vidname = self.vid.stem

        while count <= frames_to_be_extracted:  # Modify the loop condition here
            success, image = vid_cap.read()
            if success:
                try:
                    # Create a directory for the video if it doesn't exist
                    video_dir = self.create_dir_if_not_exists(vidname)

                    # Save the frame in the directory named after the video
                    file_location = os.path.join(video_dir, f"{vidname}_{count}.{self.img_frmt}")
                    cv2.imwrite(file_location, image)

                    print(f"Done: {count}")
                except Exception as ex:
                    print("[ERROR CODE 1001]")
                    print(ex)
            else:
                print(
                    f"Done extracting frames: {count - 1} frames extracted for video '{vidname}'.")
                break

            count += 1
            sec += self.required_frame_rate
            vid_cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
