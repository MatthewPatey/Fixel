from unittest import TestCase
from src import fixel
import test_strings


class FixelTests(TestCase):
	#def oneliner_test(self):
	#	self.run_fixel_on_input(test_strings.oneliner_source, test_strings.oneliner_python)
	
	def run_fixel_on_input(self, source,expected_python_output):
		fixel_output = fixel.translate(source)
		self.assertEqual(fixel_output, expected_python_output)