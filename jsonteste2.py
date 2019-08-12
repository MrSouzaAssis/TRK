import json
import jsonteste as teste

def json_decode(input5):
	json_data_decode = {}
	json_data_decode = json.loads(input5)
	return json_data_decode


def list_separator(input6):
	type = ''
	status1 = ''
	status2 = ''
	status3 = ''
	

	type = json_decode(input6)['type']
	status1 = json_decode(input6)['status1']
	
	try:
		status2 = json_decode(input6)['status2']
	except Exception as error:
		#print(error)
		pass
	try:
		status3 = json_decode(input6)['status3']
	except Exception as error:
		#print(error)
		pass
	
	if status2 == '' and status3 == '':
		#INSERT INTO `status` (`id`, `id_sensors`, `status1`, `status2`, `status3`, `time`) VALUES (NULL, '1', 'True', NULL, NULL, current_timestamp());
		print('1')
	elif status2 != '' and status3 == '':
		#INSERT INTO `status` (`id`, `id_sensors`, `status1`, `status2`, `status3`, `time`) VALUES (NULL, '1', 'True', 'True', NULL, current_timestamp());
		print('2')
	else:
		#INSERT INTO `status` (`id`, `id_sensors`, `status1`, `status2`, `status3`, `time`) VALUES (NULL, '1', 'True', 'True', 'True', current_timestamp());
		print('3')		
	#return 'alguma coisa'

list_separator(teste.json_data)


