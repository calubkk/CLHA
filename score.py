import json

def concatenate_strings(string_list):
    result = ""
    for string in string_list:
        result += '\n'
        result += string
    return result

raw_pro = []
output = []
kk = 'helpful_base'
with open('/data/zhuliang/PRO/inference_res/infer_main_1_2_'+kk+'.json', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        raw_pro.append(data)

raw = []
with open('/data/fangfeiteng/backup/PRO/eval_hh/inference_res/infer_main_1_2_'+kk+'.json', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        raw.append(data)


for i in range(len(raw_pro)):
    dic = {}
    #dic['id'] = i
    for j in range(len(raw)):
        if concatenate_strings(raw[j]['prefix'][0]) == concatenate_strings(raw_pro[i]['prefix'][0]):
            dic['text'] = '问题：\n' + concatenate_strings(raw[j]['prefix'][0]) + '\n\n回答：\n\n' + 'A:\n' + raw_pro[i]['infer']['t'] +'\n' + 'B:\n' + raw[j]['infer']['t']
            #dic['model'] = "CLHA_2"
            dic["label"] = [""]
            #dic["Comments"]:[""]
            output.append(dic)

'''
with open("/data/fangfeiteng/backup/helpful_base.json", "w", encoding="utf-8") as file:
    for data in output:
        # 将字典转换为 JSON 字符串
        json_str = json.dumps(data,ensure_ascii=False)
        # 写入文件并添加换行符以确保下一个 JSON 对象在新的一行
        file.write(json_str + '\n')
'''
with open("/data/fangfeiteng/backup/"+kk+"_300_pro.json",'w',encoding='utf8') as f:
        # ensure_ascii=False才能输入中文，否则是Unicode字符
        # indent=2 JSON数据的缩进，美观
        json.dump(output[:300],f,ensure_ascii=False,indent=2)