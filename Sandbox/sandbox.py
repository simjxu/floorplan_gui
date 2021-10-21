import yaml
import datetime
class YAMLoutput:
	TOP_LEVELS = []

	# The following need to be accessed by Main App
	BUILD_NAMES = []
	DATE_ARRAYS = []
	LABEL_ARRAYS = []
	START_MONTH = 0
	START_YEAR = 0
	END_MONTH = 0
	END_YEAR = 0


	def __init__(self, parent, **kwargs):
		with open(kwargs['file'], "r") as stream:
			try:
				yaml_dict = yaml.safe_load(stream)
				# print(yaml_dict)
			except yaml.YAMLError as exc:
				print(exc)
		
		print(yaml_dict)
		print(yaml_dict['System']['Proto'])
		print(yaml_dict['System']['Proto']['date'])
		# Capture build names, the labels, and the dates
		for key in yaml_dict:
			self.BUILD_NAMES.append(key)
			syslabel_arr = []
			sysdate_arr = []

			# System Label Level
			for keyS in yaml_dict[key]:
				syslabel_arr.append(keyS)	
				sysdate_arr.append(yaml_dict[key][keyS]['date'])
			self.LABEL_ARRAYS.append(syslabel_arr)
			self.DATE_ARRAYS.append(sysdate_arr)

		# Get the Start and End
		a = self.find_startend(self.DATE_ARRAYS)

		# print(self.BUILD_NAMES)						
		# print(self.DATE_ARRAYS)
		# print(self.LABEL_ARRAYS)

	def find_startend(self, date_array):
		# Combine the lists into a single array
		full_array = [sub for date in date_array for sub in date]
		datetime_array = []
		for date in full_array:
			datetime_array.append( \
				datetime.datetime.strptime(date, "%m/%d/%y"))
		
		start_date = min(datetime_array)
		end_date = max(datetime_array)
		
		self.START_MONTH = start_date.month
		self.START_YEAR = start_date.year
		self.END_MONTH = end_date.month
		self.END_YEAR = end_date.year
		
		# print(self.START_MONTH)
		# print(self.START_YEAR)
		# print(self.END_MONTH)
		# print(self.END_YEAR)

		return 0

	def get_dates(selection):
		print("placeholder")

	def save_current():
		print("placeholder")

class YAMLApplication:
	def __init__(self, **kwargs):
		yamlobj = YAMLoutput(self, file=kwargs['file'])

if __name__ == "__main__":
	ymlfile = "./Sample_YAML/example.yaml"
	app = YAMLApplication(file=ymlfile)