import json


data = {}
input1=''
input2=''
input3=''
input4=''

def list_to_json(input1,input2,input3,input4):
	data['type']    = input1
	data['status1'] = input2
	
	if input3 != '':
		data['status2'] = input3
	
	if input4 != '':
		data['status3'] = input4

	return json.dumps(data)
	#return data

json_data = list_to_json('door','true','2','3')


