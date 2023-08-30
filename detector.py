# Created by: Ausar686
# https://github.com/Ausar686

from typing import NamedTuple, Union

from mediapipe.python.solutions.pose import Pose
import numpy as np
import cv2


class Detector:
    """
    Class for human pose keypoint detection using mediapipe. 
    """

    def __init__(
        self,
        *,
        model_complexity: int=1,
        min_detection_confidence: float=0.5,
        min_tracking_confidence: float=0.5):
        """
        Initializes Detector object which uses mediapipe.solutions.pose.Pose as detection model.
        """
        self.model = Pose(
            model_complexity=model_complexity,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )
        return
    
    def detect(self, image: np.ndarray) -> Union[NamedTuple, None]:
        """
        Performs pose detection on BGR image.
        Firstly, converts image to RGB, then performs detection and then converts image back to BGR.
        """
        if image is None:
            return None
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        keypoints = self.model.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        return keypoints
    
    @staticmethod
    def to_numpy(keypoints: NamedTuple, *, world: bool=False) -> Union[np.ndarray, None]:
        """
        Converts detected keypoints to numpy array. If no keypoints were given, returns None.
        If 'world' kwarg is set to True, converts world landmarks to numpy array.
        Otherwise converts landmarks to numpy array.
        """
        if keypoints is None:
            return None
        if keypoints.pose_landmarks is None:
            return None
        if keypoints.pose_world_landmarks is None:
            return None
        if world:
            lst = [[point.x, point.y, point.z, point.visibility] 
                   for point in keypoints.pose_world_landmarks.landmark]
        else:
            lst = [[point.x, point.y, point.z, point.visibility]
                   for point in keypoints.pose_landmarks.landmark]
        array = np.array(lst)
        return array

    def run(self, image: np.ndarray) -> Union[np.ndarray, None]:
        """
        Executes 'detect' and 'to_numpy' consecutevely.
        """
        keypoints = self.detect(image)
        array = self.to_numpy(keypoints)
        return array