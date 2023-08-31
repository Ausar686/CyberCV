# Created by: Ausar686
# https://github.com/Ausar686

import numpy as np

from single_action_test import SingleActionTest


class NoisyTest(SingleActionTest):
    """
    Class for reaction test, based onn reaction on color of the inner frame:
    If inner frame is red, user should bend his head
    """
    
    def __init__(self, **kwargs):
        # Initialize parent class
        super().__init__(**kwargs)
        # Set tests data
        self.max_tests = kwargs.get("max_tests", 30)
        self.info = ["Помехоустрочивость", "Когда цвет внутри рамки", "станет красным,", "выполните приседание."]
        # Set colors
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 200, 255), (124, 156, 145), (0, 0, 255)]
        self.set_random_index()
        return
    
    def set_random_index(self) -> None:
        """
        Sets random index for selecting outer frame color
        """
        while True:
            self.random_index = np.random.randint(0, len(self.colors))
            if self.random_index != self.color_index:
                return
    
    @property
    def outer_color(self):
        """
        Returns an outer frame color.
        """
        return self.colors[self.random_index]
    
    def switch_color(self):
        """
        Selects new colors for inner and outer frames
        """
        super().switch_color() # Inner frame
        self.set_random_index() # Outer frame
        return
    
    @property
    def status(self):
        """
        Check, whether user is performing a squat.
        """
        if self.pose is None:
            return False
        # return self.pose[0, 1] > self.pose[11, 1] and self.pose[0, 1] > self.pose[12, 1]
        delta = 0.07
        return (self.pose[23, 1] - self.pose[25, 1] > -delta 
            and self.pose[24, 1] - self.pose[26, 1] > -delta)