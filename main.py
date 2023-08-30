# Created by: Ausar686
# https://github.com/Ausar686

from detector import Detector
from base_test import BaseTest
from action_reaction_test import ActionReactionTest
from choice_reaction_test import ChoiceReactionTest
from color_reaction_test import ColorReactionTest
from noisy_test import NoisyTest
from reaction_test import ReactionTest
from tapping_test import TappingTest
from app import CyberCVApp
from utils import send_data

test1 = ReactionTest(demo_path="ex1.mp4")
test2 = ColorReactionTest(demo_path="ex2.mp4")
test3 = ActionReactionTest(demo_path="ex3.mp4")
test4 = ChoiceReactionTest(demo_path="ex4.mp4")
test5 = TappingTest(demo_path="ex5.mp4")
test6 = NoisyTest(demo_path="ex6.mp4")
tests = [test1, test2, test3, test4, test5, test6]

detector = Detector()
source = 0

app = CyberCVApp(tests, source, detector)
app.run()
if app.is_over:
	send_data(app)