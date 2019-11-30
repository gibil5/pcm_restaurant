

	# Test 1
	def test_index_empty(self):
		"""
		Test Index View with no Objects
		"""
		print()
		print('Test Family 1: Begin')



		# Create Client 
		c = Client()

		path = 'families'
		
		lib.test_status_code_ok(self, c, path)


		print()
		print('Test Family 1: End')

