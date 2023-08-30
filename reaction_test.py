# Created by: Ausar686
# https://github.com/Ausar686

from single_action_test import SingleActionTest


class ReactionTest(SingleActionTest):
    """
    Class for running reaction test:
    User should put his hands up, when the frame becomes green. 
    """
    
    def __init__(self, **kwargs):
        # Initialize parent class
        super().__init__(**kwargs)
        # Set tests data
        self.max_tests = kwargs.get("max_tests", 30)
        self.info = ["Тест на реакцию", "Когда цвет станет зеленым,", "поднимите руки"]
        # Set test colors: red and green
        self.colors = [(0,0,255), (0,255,0)]
        return
    
    @property
    def status(self) -> bool:
        """
        Checks, whether user's hands are up or not.
        """
        if self.pose is None:
            return False
        return self.pose[0,1] > self.pose[15,1] and self.pose[0,1] > self.pose[16,1]