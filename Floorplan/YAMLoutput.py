import yaml
import datetime
class YAMLoutput:

	def __init__(self, parent, **kwargs):
		with open(kwargs['file'], "r") as stream:
			try:
				self.yaml_dict = yaml.safe_load(stream)
				# print(self.yaml_dict)
			except yaml.YAMLError as exc:
				print(exc)
		
		self.load_yaml()

		# print(self.BUILD_NAMES)						
		# print(self.DATE_ARRAYS)
		# print(self.LABEL_ARRAYS)

	def load_yaml(self):
		# Reset to 0
		# The following need to be accessed by Main App
		self.BUILD_NAMES = []
		self.DATE_ARRAYS = []
		self.LABEL_ARRAYS = []
		self.START_MONTH = 0
		self.START_YEAR = 0
		self.END_MONTH = 0
		self.END_YEAR = 0

		# Capture build names, the labels, and the dates
		for key in self.yaml_dict:
			# Get builds
			self.BUILD_NAMES.append(key)
			syslabel_arr = []
			sysdate_arr = []

			# Get labels and dates
			for keyS in self.yaml_dict[key]:
				syslabel_arr.append(keyS)	
				sysdate_arr.append(self.yaml_dict[key][keyS]['date'])
			self.LABEL_ARRAYS.append(syslabel_arr)
			self.DATE_ARRAYS.append(sysdate_arr)

		# Get the Start and End
		self.find_startend(self.DATE_ARRAYS)

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

	def update_dates(self, **kwargs):
		build_name = kwargs['build_name']
		label = kwargs['label']
		date = kwargs['date']
		# print(self.yaml_dict)
		
		# Update the yaml dict
		self.yaml_dict[build_name][label]['date'] = date

		# Reload the dict
		self.load_yaml()

		# print(self.yaml_dict)
		# # Get index of the date you need to update
		# build_idx = self.BUILD_NAMES.index(build_name)
		# label_idx = self.LABEL_ARRAYS[build_idx].index(label)
		# self.DATE_ARRAYS[build_idx][label_idx] = date

	def save_current(self, saveFile):
		with open(saveFile, 'w') as file:
			yaml.safe_dump(self.yaml_dict,file,sort_keys=False)

class MainApplication:
	def __init__(self, **kwargs):
		yamlobj = YAMLoutput(self, file=kwargs['file'])

if __name__ == "__main__":
	ymlfile = "./Sandbox/example.yaml"
	app = MainApplication(file=ymlfile)