# Created by: Ausar686
# https://github.com/Ausar686

import time

from base_test import BaseTest


class SingleActionTest(BaseTest):
    """
    Base class, for single action tests.
    """
    
    def set_time(self) -> None:
        """
        Sets time for test.
        """
        self.time_start = time.time()
        self.switch_time = time.time() + 1
        return
    
    @property
    def is_action_color(self) -> bool:
        """
        Bool, that represents, that color is green
        """
        return self.color_index == len(self.colors) - 1
    
    def run(self) -> None:
        """
        Common method for all subclasses.
        """
        if self.time_start is None:
            self.set_time()
        if self.status:
            if self.is_action_color:
                self.time_end = time.time()
                time_reaction = round(self.time_end - self.time_start, 2)
                self.data.append(time_reaction)
                self.switch_color()
            else:
                self.set_time()
        elif time.time() >= self.switch_time and not self.is_action_color:
            self.switch_color()
            self.set_time()
        return