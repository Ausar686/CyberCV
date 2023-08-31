# Created by: Ausar686
# https://github.com/Ausar686

from typing import List, Union
import time

import cv2
import numpy as np

from detector import Detector
from base_test import BaseTest
from utils import send_data


class CyberCVApp:
    """
    Class for reaction testing for cybersport.
    """
    
    def __init__(
        self,
        tests: List[BaseTest],
        source: Union[int, str],
        detector: Detector,
        **kwargs):
        """
        
        """
        self.detector = detector
        self.tests = [BaseTest(), *tests]
        self.source = source
        self.cap = None
        self.index = 0
        return
    
    def __len__(self):
        """
        Amount of tests.
        """
        return len(self.tests)
    
    def to_next(self) -> None:
        """
        Goes to next test (if possible)
        """
        self.index += 1
        if self.index >= len(self):
            self.index -= 1
            return
        self.start_test()
        return
    
    def to_previous(self) -> None:
        """
        Goes to previous test (if possible)
        """
        self.index -= 1
        if self.index < 1:
            self.index += 1
            return
        self.start_test()
        return
    
    def start_test(self) -> None:
        """
        Starts the test by closing all windows and showing demo.
        """
        cv2.destroyAllWindows()
        self.test.clear()
        self.test.run_demo()
        return
    
    @property
    def test(self) -> BaseTest:
        """
        Returns a test by index
        """
        return self.tests[self.index]
    
    @property
    def is_over(self):
        """
        Checks if all tests are completed
        """
        for test in self.tests:
            if len(test.data) < test.max_tests:
                return False
        return True
    
    def preprocess(self, frame: np.ndarray) -> np.ndarray:
        """
        Performs inplace frame preprocessing before landmark detection.
        """
        width, height = self.test.width, self.test.height
        frame = cv2.resize(frame, (width, height))
        return frame
    
    @property
    def postprocess(self):
        """
        An alias for self.test.postprocess
        """
        return self.test.postprocess
    
    def run(self):
        time.sleep(1)
        self.email = input("\n\nВведите Ваш email: ")
        print("Спасибо! Результаты будут зарегистрированы на сайте под вашим эл. адресом!\n\n")
        self.index = 0
        self.test.init_audio()
        self.cap = cv2.VideoCapture(self.source)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.test.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.test.height)
        while not self.is_over:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame = self.preprocess(frame)
            pose = self.detector.run(frame)
            self.test.update_pose(pose)
            self.test.run()
            self.postprocess(frame)
            cv2.imshow("CyberCV Tests", frame)
            k = cv2.waitKey(1)
            if len(self.test.data) >= self.test.max_tests and self.index:
                self.test.congratulate()
                self.to_next()
                continue
            if self.test.is_exit_key(k):
                break
            elif k == ord("d") or k == ord("D"):
                self.to_next()
            elif k == ord("a") or k == ord("A"):
                self.to_previous()
        cv2.destroyAllWindows()
        self.cap.release()
        self.test.deinit_audio()
        time.sleep(1)
        if self.is_over:
            send_data(self)
            print(f"\n\nВы успешно завершили тестирование!\nРезультаты занесены в Ваш личный кабинет\nE-mail: {self.email}")
        else:
            print("\n\nК сожалению, Вы прошли тестирование не полностью.\nПройдите его в следующий раз, когда Вам будет удобно,\nчтобы мы могли сохранить результаты в Вашем личном кабинете.")
        input("Нажмите Enter, чтобы продолжить.\n")
        return