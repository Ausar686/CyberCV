# Created by: Ausar686
# https://github.com/Ausar686

from single_action_test import SingleActionTest


class ColorReactionTest(SingleActionTest):
    """
    Class, that implements test of reaction on color change:
    Whenever color changes to red, bend your head to your hips.
    """
    
    def __init__(self, **kwargs):
        # Initialize parent class
        super().__init__(**kwargs)
        # Set tests data
        self.max_tests = kwargs.get("max_tests", 30)
        self.info = ["Реакция различия", "Когда цвет станет красным,", "выполните наклон вперед."]
        # Set test colors: blue, green, red
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        return
    
    @property
    def status(self) -> bool:
        """
        Check, whether user's head is bended low.
        """
        if self.pose is None:
            return False
        return self.pose[0,1] > self.pose[23,1] and  self.pose[0,1] > self.pose[24,1]