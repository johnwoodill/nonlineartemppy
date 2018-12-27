import unittest2
import nonlineartemppy.calculations as nltemp
import pandas as pd

# Initial test
#def test_numbers_3_4():
#    assert 3*4 == 12 

# Unit test function of degree days (degree_days())
def test_degree_days():

	# Build test data frame
	tdat = pd.DataFrame({"date": "2018-12-25", "tmax": [34], "tmin": [10], "location": "Estes Park, CO"})
	
	# Calculate degree days
	retdat = nltemp.degree_days(tdat, range(20,21))
	retarray = retdat['dday20C'].iloc[0]

	# Test
	assert 4.87289 == retarray


# Unit test time in each degree (degree_time())
def test_degree_time():

	# Build test data frame
	tdat = pd.DataFrame({"date": "2018-12-25", "tmax": [34], "tmin": [10], "location": "Estes Park, CO"})
	
	# Calculate time in each degree
	retdat = nltemp.degree_time(tdat, range(20,21))
	retarray = retdat['tdegree20C'].iloc[0]

	# Test
	assert 0.02918 == retarray

