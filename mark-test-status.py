from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.BuiltIn import _Misc
import robot.api.logger as logger
from robot.api.deco import keyword
from robot.api import SkipExecution

@keyword("TEST STATUS")
def testStatus():
     raise SkipExecution('Cannot proceed, skipping test.')
