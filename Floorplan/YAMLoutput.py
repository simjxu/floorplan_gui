import yaml
import datetime
class YAMLoutput:

	def __init__(self, parent, **kwargs):
		print(kwargs['file'])
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
		self.COLOR_ARRAYS = []
		self.START_MONTH = 0
		self.START_YEAR = 0
		self.END_MONTH = 0
		self.END_YEAR = 0

		# Capture build names, the labels, and the dates
		for key in self.yaml_dict:
			# Get builds
			self.BUILD_NAMES.append(key)
			label_arr = []
			date_arr = []
			color_arr = []

			# Get labels and dates
			for keyS in self.yaml_dict[key]:
				label_arr.append(keyS)	
				date_arr.append(self.yaml_dict[key][keyS]['date'])
				color_arr.append(self.yaml_dict[key][keyS]['color'])
			self.LABEL_ARRAYS.append(label_arr)
			self.DATE_ARRAYS.append(date_arr)
			self.COLOR_ARRAYS.append(color_arr)

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
		# Go back one month so we have buffer
		if self.START_MONTH == 1:
			self.START_MONTH = 12
			self.START_YEAR -= 1
		else:
			self.START_MONTH -= 1

		self.END_MONTH = end_date.month
		self.END_YEAR = end_date.year
		# Go forward one year so we have buffer
		if self.END_MONTH == 12:
			self.END_MONTH = 1
			self.END_YEAR += 1
		else:
			self.END_MONTH +=1
		# print(self.START_MONTH)
		# print(self.START_YEAR)
		# print(self.END_MONTH)
		# print(self.END_YEAR)

		return 0

	def add_label(self, buildname, labelname, date, color):
		self.yaml_dict[buildname][labelname] = {}
		self.yaml_dict[buildname][labelname]["date"] = date
		self.yaml_dict[buildname][labelname]["color"] = color

	def update_dates(self, **kwargs):
		build_name = kwargs['build_name']
		label = kwargs['label']
		date = kwargs['date']
		# print(self.yaml_dict)
		
		# Update the yaml dict
		self.yaml_dict[build_name][label]['date'] = date

		# Reload the dict
		self.load_yaml()


	def sort_all_dates(self):
		for build_name in self.yaml_dict:
			# Get date strings
			datetime_arr = [datetime.datetime.strptime(self.yaml_dict[build_name][label]['date'], \
				'%m/%d/%y') for label in self.yaml_dict[build_name]]

			# Sort the dates in the yaml file
			sorted_indices = [i[0] for i in sorted(enumerate(datetime_arr), key=lambda x:x[1])]
			build_order_list = [item for item in self.yaml_dict[build_name]]
			build_order_list = [build_order_list[i] for i in sorted_indices]

			reordered_dict = {k: self.yaml_dict[build_name][k] for k in build_order_list}
			self.yaml_dict[build_name] = reordered_dict

		# Reload the dict
		self.load_yaml()

	def save_current(self, saveFile):
		with open(saveFile, 'w') as file:
			yaml.safe_dump(self.yaml_dict,file,sort_keys=False)

class MainApplication:
	def __init__(self, **kwargs):
		yamlobj = YAMLoutput(self, file=kwargs['file'])

if __name__ == "__main__":
	ymlfile = "./Sandbox/example.yaml"
	app = MainApplication(file=ymlfile)