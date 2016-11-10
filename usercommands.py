from subprocess import Popen, PIPE

def get_list():
	list_process = Popen(["ls","/home/filesystem_user"],stdout=PIPE,stderr=PIPE).communicate()[0].split('\n')
	return filter(None,list_process)

def create_archive(filename,content):
	
	nuevoArchivo= Popen(["touch",filename], stdout=PIPE, stderr=PIPE)
	nuevoArchivo.wait()
	file=open(filename,"w")
	file.write(content)
	file.close()

	Popen(["mv", filename, "/home/filesystem_user"],stdout=PIPE,stderr=PIPE)

	return True if filename in get_list() else False

def delete_archs(filename):
	vip = ["environment","python"]
	if filename in vip:
		return True
	else:
		remove_process = Popen(["rm","-f","/home/filesystem_user/"+filename],stdout=PIPE,stderr=PIPE)
		remove_process.wait()
		return False if filename in get_list() else True

def recently_archs():
	list_process = Popen(["find","/home/filesystem_user/","-type", "f","-mmin","-60"],stdout=PIPE,stderr=PIPE)
	sub_list = Popen(["awk",'-F','/home/filesystem_user/','{print $2}'],stdin=list_process.stdout,stdout=PIPE,stderr=PIPE).communicate()[0].split('\n')
	return sub_list
