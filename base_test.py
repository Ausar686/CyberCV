# Created by: Ausar686
# https://github.com/Ausar686

from typing import Union, Tuple

import cv2
import numpy as np

from detector import Detector


class BaseTest:
    """
    Base class for all functional tests
    """
    
    _defaults = {
        "width": 1920,
        "height": 1080,
        "font": cv2.FONT_HERSHEY_COMPLEX,
        "font_scale": 1,
        "font_color": (255,0,0), # Blue
        "thickness": 2,
        "border_thickness": 150
    }
    
    def __init__(self, **kwargs):
        """
        Initializes base class instance.
        """
        # Set data attributes
        self.demo_path = kwargs.get("demo_path")
        self.window_name = kwargs.get("window_name", "Demo")
        self.data = []
        self.max_tests = 0
        self.info = kwargs.get("info", [])
        # Set cv2 parameters
        for param in self._defaults:
            setattr(self, param, kwargs.get(param, self._defaults[param]))
        # Set pose attribute
        self.pose = None
        # Set color attributes
        self.init_colors()
        # Init time attributes
        self.init_time()
        return
    
    def init_time(self) -> None:
        """
        Initializes time attributes for test
        """
        self.time_start = None
        self.time_end = None
        self.switch_time = None
        return

    def init_colors(self) -> None:
        """
        Initializes color attributes
        """
        self.colors = None
        self.color_index = 0
        return

    @property
    def color(self) -> tuple:
        """
        Returns current color (tuple), according to the index
        """
        return self.colors[self.color_index] if self.colors else (0,255,0)

    def switch_color(self) -> None:
        """
        Increments self.color_index
        """
        self.color_index = (self.color_index + 1) % len(self.colors)
    
    def update_pose(self, pose: Union[np.ndarray, None]) -> None:
        """
        Updates self.pose with 'pose' argument
        """
        self.pose = pose
        return
    
    def clear(self) -> None:
        """
        Clears self.data and sets all timers to None
        """
        self.data.clear()
        self.init_time()
        return

    @staticmethod
    def is_exit_key(key: int) -> bool:
        """
        Check if key is q/Q
        """
        return key == ord("q") or key == ord("Q")
    
    def run_demo(self) -> None:
        """
        Shows demo video of test, executed by professional.
        """
        if self.demo_path is None:
            return
        cap = cv2.VideoCapture(self.demo_path)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            self.edit_demo_frame(frame)
            cv2.imshow(self.window_name, frame)
            k = cv2.waitKey(7) # 15 ms is enough to make a demo look smooth
            if self.is_exit_key(k):
                break
        cap.release()
        cv2.destroyAllWindows()
        return
            
    def edit_demo_frame(self, frame: np.ndarray, *args, **kwargs) -> None:
        """
        Performs demo frame edit before display.
        Override this method for subclasses.
        """
        self.make_white_border(frame)
        self.write_instructions(frame)
        self.write_info(frame)
        return

    def postprocess(self, frame: np.ndarray) -> None:
        """
        Performs inplace frame post-processing for further display.
        This method is recommended to be overridden by subclasses.
        """
        self.make_inner_frame(frame)
        self.make_outer_frame(frame)
        self.make_white_border(frame)
        self.write_instructions(frame)
        self.write_info(frame)
        self.write_status(frame)
        return

    def make_outer_frame(self, frame: np.ndarray) -> None:
        """
        Colors inner part of the decorated video frame (for noisy test)
        """
        if not hasattr(self, "outer_color"):
            return
        height, width = frame.shape[:2]
        cv2.rectangle(frame, (0, 0), (int(0.66*width), height), self.outer_color, int(self.border_thickness//1.5) + 1)
        return

    def make_inner_frame(self, frame: np.ndarray) -> None:
        """
        Colors outer part of the decorated video frame
        """
        if not self.max_tests:
            return
        height, width = frame.shape[:2]
        cv2.rectangle(frame, (0, 0), (int(0.66*width), height), self.color, self.border_thickness)
        return

    def make_white_border(self, frame: np.ndarray) -> None:
        """
        Colors right part of the frame into white.
        """
        height, width = frame.shape[:2]
        color_white = (255,255,255)
        white_start_width = int(0.7 * width)
        cv2.rectangle(frame, (white_start_width, 0), (width, height), color_white, -1)
        return

    def put_text(self, frame: np.ndarray, text: str, origin: Tuple[int, int]) -> None:
        """
        cv2.putText with parameters from self
        """
        line_type = 1
        cv2.putText(frame, text, origin, self.font, self.font_scale, self.font_color, self.thickness, line_type)
        return

    def put_text_narrow(self, frame: np.ndarray, text: str, origin: Tuple[int, int]) -> None:
        """
        The same as self.put_text, but thickness is 2 times smaller
        """
        line_type = 1
        cv2.putText(frame, text, origin, self.font, self.font_scale, self.font_color, self.thickness // 2, line_type)
        return

    def write_info(self, frame: np.ndarray) -> None:
        """
        Writes information about test in the top-right corner.
        """
        height, width = frame.shape[:2]
        start_height = 50
        start_width = int(0.72 * width)
        for i, row in enumerate(self.info):
            origin = (start_width, start_height + 50*i)
            if not i:
                self.put_text(frame, row, origin)
            else:
                self.put_text_narrow(frame, row, origin)
        return

    def write_instructions(self, frame: np.ndarray) -> None:
        """
        Write instructions in the bottom right corner.
        """
        height, width = frame.shape[:2]
        start_width = int(width * 0.72)
        self.put_text(frame, "Далее: нажмите d", (start_width, height-140))
        self.put_text(frame, "Назад: нажмите a", (start_width, height-90))
        self.put_text(frame, "Выход: нажмите q", (start_width, height-40))
        return

    def write_status(self, frame: np.ndarray) -> None:
        """
        Writes test status on the frame.
        How many tests are completed and the results of the last test.
        """
        if not self.max_tests:
            return
        height, width = frame.shape[:2]
        start_width = int(0.72 * width)
        start_height = height // 2
        completed = f"Тест: {len(self.data)+1}/{self.max_tests}"
        result = f"Время реакции: {self.data[-1]}с" if self.data else f"Время реакции: ???"
        self.put_text(frame, completed, (start_width, start_height - 25))
        self.put_text(frame, result, (start_width, start_height + 25))
        return

    @property
    def status(self) -> bool:
        """
        Computes current test status. Override this method for subclasses.
        """
        pass
    
    def run(self, *args, **kwargs) -> None:
        """
        Runs a test. Override this method for subclasses.
        """
        pass