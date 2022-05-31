import unittest
import pytest
from PySide6 import QtCore
from AngleDisplay import AngleDisplay

class ValueTestCase(unittest.TestCase):

   def testAngles(self):
       result = AngleDisplay.getStringValue("100")
       self.assertEqual(result, "100º")
       
@pytest.fixture
def app(qtbot):
    angleApp = AngleDisplay()
    qtbot.addWidget(angleApp)
    return angleApp


def test_label(app):
    assert app.color == app.colors[app.colorIndex]


def test_label_after_click(app, qtbot):
    qtbot.mouseClick(app, QtCore.Qt.LeftButton)
    assert app.color == app.colors[app.colorIndex]
    