import requests
import json
import time


def search_song(filename):
    # filename = r'C:\Users\aarrt17\Desktop\FinalProject\bolshie-goroda-mini.wav'
    apikey = '5265c25414c1abd8a22edd7a03fc4601'  # generate and place here your unique API access key
    payload = {'action': 'identify', 'apikey': apikey, 'start_time': 0, 'time_len': 20}
    result = requests.post('https://audiotag.info/api', data=payload, files={'file': open(filename, 'rb')})
    result_object = json.loads(result.text)
    if result_object['success'] is True and result_object['job_status'] == 'wait':
        token = result_object['token']
        n = 1
        job_status = 'wait'
        while n < 100 and job_status == 'wait':
            time.sleep(0.5)
            n += 1
            payload = {'action': 'get_result', 'token': token, 'apikey': apikey}
            result = requests.post('https://audiotag.info/api', data=payload)
            result_object = json.loads(result.text)
            if result_object['success'] is True:
                job_status = result_object['result']
            else:
                break

    else:
        return 'not success'
    dct = check_true_name(result_object['data'])
    return dct


def check_true_name(data_dct):
    dct = {'name': None}
    check_dct = []
    for i in data_dct:
        name = i['tracks'][0][0]
        check_dct.append(name)
    repeats = {}
    for item in check_dct:
        if item in repeats:
            repeats[item] += 1
        else:
            repeats[item] = 1
    n = 1
    for i in repeats:
        if repeats[i] > n:
            dct['name'] = i
            n = i
    if dct['name'] is None:
        dct['name'] = data_dct[0]['tracks'][0][0]
    dct['author'] = data_dct[0]['tracks'][0][1]
    return dct
