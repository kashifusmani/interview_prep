# {"hospital_id":1234, "patient":"Jane Doe", "location":[-124,39], "medicalRecord":{"visitDate":"20210913", "illness":"fever"}}

#{"hospital_id":1234, "patient":"Jane Doe", "location_0":-124, "location_1":39, "medicalRecord.visitDate": "20210913", "medicalRecord.illness":"fever"}



def recursive_flatten(key, v):
    if isinstance(v, str) or isinstance(v, int):
        return [v]
    elif isinstance(v, list):
        result = []
        for i, elem in enumerate(v):
            for entry in recursive_flatten(key, elem):
                result.append((key +'_' + str(i), entry))
        return result

def flatten_2(x):
    result = {}
    for key,v in x.items():
        for entry in recursive_flatten(key,v):
            print(entry)
    print(result)



def flatten(x):
    result = {}
    for key,v in x.items():
        if isinstance(v, str) or isinstance(v, int):
            result[key]=v
        elif isinstance(v, list):
            for i, elem in enumerate(v):
                result[key + '_' + str(i)] = elem
        elif isinstance(v, dict):
            for keyi, vi in v.items():
                if isinstance(vi, str):
                    result[key + '.' + str(keyi)] = vi
                elif isinstance(vi, list):
                    for i, elem in enumerate(vi):
                        result[key + '.' + keyi +  '_' + str(i)] = elem
    print(result)

inp = {
        "hospital_id":1234,
        "patient":"Jane Doe",
        "location":[-124,39],
        "medicalRecord" : {"visitDate":"20210913", "illness":[{"symptom":"fever", "temp":102}, {"symptom":"cold"}]}
    }

#{"hospital_id":1234, "patient":"Jane Doe", "location_0":-124, "location_1":39, "medicalRecord.visitDate": "20210913", "medicalRecord.illness_0":"fever", "medicalRecord.illness_1":"cold"}


#flatten(inp)
inp_2 = {"hospital_id":1234, "patient":"Jane Doe", "location":[-124,39]}
flatten_2(inp_2)