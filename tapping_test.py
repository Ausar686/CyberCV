# Created by: Ausar686
# https://github.com/Ausar686

import time

import numpy as np

from base_test import BaseTest


class TappingTest(BaseTest):
    """
    Class for backward foot tapping counting test.
    """
    
    _statuses = {
        "left": 1,
        "right": 2
    }
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set test attributes
        self.max_tests = kwargs.get("max_tests", 6)
        self.info = [
            "Теппинг-тест", 
            "Выполните бег с захлестом.", 
            "Программа считает",
            "количество захлестов",
            "каждые 5 секунд." 
        ]
        self.time_interval = kwargs.get("time_interval", 5)
        self.counter = 0
        self.prev_status = None
        return
    
    def set_time(self) -> None:
        self.time_start = time.time()
        self.time_end = self.time_start + self.time_interval
        return
    
    @property
    def foot_status(self):
        """
        Returns current foot status:
            1 - left foot is bent
            2 - right foot is bent
            None - none of above
        """
        if self.pose is None:
            return None
        if abs(self.pose[25,1] - self.pose[27,1]) <= 0.1:
            return self._statuses["left"]
        if abs(self.pose[26,1] - self.pose[28,1]) <= 0.1:
            return self._statuses["right"]

    def write_status(self, frame: np.ndarray) -> None:
        height, width = frame.shape[:2]
        start_width = int(0.72 * width)
        start_height = height // 2
        completed = f"Тест: {len(self.data)+1}/{self.max_tests}"
        result = f"Повторений: {self.data[-1]}" if self.data else f"Повторений: ???"
        self.put_text(frame, completed, (start_width, start_height - 25))
        self.put_text(frame, result, (start_width, start_height + 25))
        return

    def make_inner_frame(self, frame: np.ndarray) -> None:
        pass
        
    @property
    def status(self):
        """
        Return, whether the following is true:
            One of the legs is bent now, bot both legs were not bent on the previous frame.
        """
        return self.foot_status and not self.prev_status
    
    def run(self) -> None:
        if self.time_start is None:
            self.set_time()
        if self.status:
            self.counter += 1
        if time.time() >= self.time_end:
            self.data.append(self.counter)
            self.counter = 0
            self.set_time()
        self.prev_status = self.foot_status
        return