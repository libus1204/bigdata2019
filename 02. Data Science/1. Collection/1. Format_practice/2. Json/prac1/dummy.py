import json
from collections import OrderedDict
g_json_big_data = OrderedDict()
g_json_big_data["address"] = "dummy"
g_json_big_data["student_ID"] = "ITT000"
g_json_big_data["student_age"] = 0
g_json_big_data["student_name"] = "dummy"
g_json_big_data["total_course_info"] = {"learning_course_info":
                                [{"close_date": "dummy", "course_code": "dummy", "course_name": "dummy",
                                "open_date": "dummy", "teacher":"dummy"}],"num_of_course_learned": "dummy"}
g_json_big_data = list(g_json_big_data)
with open('dummy.json', 'w', encoding='utf8') as outfile:
    readable_result = json.dumps(g_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(readable_result)

print("학생 ID : %s" % g_json_big_data["student_ID"])