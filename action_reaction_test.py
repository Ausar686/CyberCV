# Created by: Ausar686
# https://github.com/Ausar686

from typing import Tuple
import math
import time

import cv2
import numpy as np

from single_action_test import SingleActionTest


class ActionReactionTest(SingleActionTest):
    """
    Reaction test based on reaction speed on a specific action.
    Whenever clock arrow reaches 12, user should get into star pose.
    """
    
    def __init__(self, **kwargs):
        # Initialize parent class
        super().__init__(**kwargs)
        # Set tests data
        self.max_tests = kwargs.get("max_tests", 30)
        self.info = ["Тест на движущийся объект", "Когда стрелка достигнет 12,", "выполните упражнение."]
        # Set test colors: red and green
        self.colors = [(0,0,255), (0,255,0)]
        # Set clock parameters
        self.center = kwargs.get("center", (200, 150))
        self.radius = kwargs.get("radius", 100)
        self.clock_color = kwargs.get("clock_color", (0,0,0)) # Black color
        return
    
    def draw_clock_general(
        self,
        image: np.ndarray,
        center: Tuple[int, int],
        radius: int,
        arrow_angle: float,
        font: int=None,
        font_scale: float=None,
        color: Tuple[int, int, int]=None,
        thickness: int=None) -> None:
        """
        General function for drawing clock on image.
        """
        if font is None:
            font = self.font
        if font_scale is None:
            font_scale = self.font_scale
        if color is None:
            color = self.clock_color
        if thickness is None:
            thickness = self.thickness
        # Draw clock circle
        color_white = (255, 255, 255)
        cv2.circle(image, center, radius, color, thickness)
        cv2.circle(image, center, radius, color_white, -1)
        # Set digits' origins
        origins = {
            "12": (center[0] - 15, center[1] - radius + 30),
            "3": (center[0] + radius - 30, center[1] + 10),
            "6": (center[0] - 10, center[1] + radius - 10),
            "9": (center[0] - radius + 10, center[1] + 10)
        }
        # Draw digits
        for digit, origin in origins.items():
            cv2.putText(image, digit, origin, font, font_scale, color, thickness)
        # Draw an arrow
        angle = math.radians(arrow_angle)
        endpoint = (int(center[0] + radius * math.sin(angle)), int(center[1] - radius * math.cos(angle)))
        cv2.line(image, center, endpoint, color, thickness)
        return
    
    def draw_clock(self, image: np.ndarray) -> None:
        """
        Draws clock with instance attributes
        """
        return self.draw_clock_general(image, self.center, self.radius, self.arrow_angle)
    
    @property
    def arrow_angle(self) -> float:
        """
        Returns an angle for drawing an arrow on the clock
        """
        if self.switch_time is None:
            return 0
        time_diff = time.time() - self.switch_time
        # Set angle according to the time difference and color
        # If it's action color, the arrow should be directed to 12,
        # So the angle equals 0, whenver it's action time
        angle = min(0, 60*time_diff) * (not self.is_action_color)
        return angle

    def postprocess(self, frame: np.ndarray) -> None:
        self.make_white_border(frame)
        self.write_instructions(frame)
        self.write_info(frame)
        self.write_status(frame)
        self.draw_clock(frame)
        return

    def set_time(self) -> None:
        """
        Override for SingleActionTest.set_time method,
        that allows to keep the position of the arrow stable during resest. 
        """
        # If time is not set, call parent method
        if self.time_start is None:
            super().set_time()
            return
        cur_time = time.time()
        # Early start case:
        # User performs action too early
        # We want to keep the amount of time left before the reaction almost the same
        # (we add a small value to keep time "frozen" until user gets out of star pose)
        # and yet update the start and swtich times
        # so that user was forced to wait until the arrow reaches 12
        # and only then perform an action
        if self.switch_time > cur_time:
            delta = 0.037
            time_diff = self.switch_time - cur_time
            self.time_start = time.time()
            self.switch_time = self.time_start + time_diff + delta
            return
        # Any other case:
        # Simply call parent method
        super().set_time()
        return
    
    @property
    def status(self) -> bool:
        """
        Check, that user is performing a star pose.
        """
        if self.pose is None:
            return False
        # Left hand should be directed diagonally
        left_hand = self.pose[11,0] < self.pose[15,0] and self.pose[11,1] > self.pose[15,1]
        # Right hand should be directed diagonally
        right_hand = self.pose[12,0] >  self.pose[16,0] and self.pose[12, 1] > self.pose[16,1]
        # Left hip should be closer to the right side of the frame
        hips = self.pose[23,0] >  self.pose[24,0]
        return left_hand and right_hand and hips