from sandbox import YAMLoutput


class MainApplication:
    def __init__(self, **kwargs):
        yamlobj = YAMLoutput(self, file=kwargs['file'])
        print(yamlobj.DATE_ARRAYS)

if __name__ == "__main__":
	ymlfile = "./Sandbox/example.yaml"
	app = MainApplication(file=ymlfile)