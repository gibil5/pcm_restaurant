

def test_status_code_ok(self, c, path):

	req = '/' + path + '/'


	# Get Response to /path/
	response = c.post(req)
	#print(response)



	# Test1 - Check Status Code - Response OK
	print()
	print('\tCheck Status Code')
	self.assertEqual(response.status_code, 200)


