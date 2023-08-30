# Created by: Ausar686
# https://github.com/Ausar686

import time

import numpy as np

from base_test import BaseTest


class ChoiceReactionTest(BaseTest):
    """
    Class for choice reaction test:
    If the frame is blue, user should stand still.
    If the frame is green, user should perform right lunge.
    If the frame is red, user should perform left lunge.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set test attributes
        self.max_tests = kwargs.get("max_tests", 30)
        self.info = [
        "Тест на реакцию выбора",
         "Когда цвет станет зеленым,",
          "сделайте выпад вправо.",
           "Когда цвет станет красным,",
            "сделайте выпад влево."
        ]
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        return
    
    def switch_color(self) -> None:
        """
        Switches the color:
            If current color is blue (index = 0), switches to random non-blue color.
            Otherwise switches to blue color.
        """
        if not self.color_index:
            self.color_index = np.random.randint(1, len(self.colors))
            return
        self.color_index = 0
        return
    
    def set_time(self):
        self.time_start = time.time()
        self.switch_time = time.time() + np.random.randint(1, 3)
        return
    
    @property
    def left(self) -> bool:
        """
        Check if it's a left lunge.
        """
        if self.pose is None:
            return False
        return abs(self.pose[26,1] - self.pose[28,1]) <= 0.1 and abs(self.pose[25,0] - self.pose[27,0]) <= 0.1
    
    @property
    def right(self) -> bool:
        """
        Check if it's a right lunge.
        """
        if self.pose is None:
            return False
        return abs(self.pose[25,1] - self.pose[27,1]) <= 0.1 and abs(self.pose[26,0] - self.pose[28,0]) <= 0.1
    
    @property
    def status(self) -> bool:
        """
        Check if the lunge is present and correlates with the color.
        Returns self.left or self.right (logical OR), if color is blue (index = 0).
        """
        if self.color_index == 1:
            return self.right
        if self.color_index == 2:
            return self.left
        return self.left or self.right
    
    def run(self):
        if self.time_start is None:
            self.set_time()
        if self.status:
            if not self.color_index:
                self.set_time()
                return
            self.time_end = time.time()
            time_reaction = round(self.time_end - self.time_start, 2)
            self.data.append(time_reaction)
            self.switch_color()
            self.set_time()
            return
        if time.time() >= self.switch_time and not self.color_index:
            self.switch_color()
            self.set_time()
            return