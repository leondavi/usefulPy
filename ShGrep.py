import subprocess

class ShGrep():
	def __init__(self,command : str, argsList : list, grepQuery : str):
		self.command = command
		self.argsList = argsList
		self.grepQuery = grepQuery

	def __enter__(self):
		self.commandToExecute = [self.command] + self.argsList

	def __exit__(self, exception_type, exception_value, traceback):
		if exception_value:
			print(traceback) 

	def run(self) -> str:
		new_process = subprocess.Popen(self.commandToExecute , stdout=subprocess.PIPE)
		grep_process = subprocess.run(["grep", self.grepQuery], stdin=new_process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		return grep_process.stdout.decode("utf-8") 