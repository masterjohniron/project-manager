import pandas as pd
import json
import requests
import datetime
import time

file_name = 'server_delopy.csv'


def send_dingding_msg(content, robot_id=''):
    try:
        msg = {
            "msgtype": "text",
            "text": {"content": content}}
        headers = {"Content-Type": "application/json;charset=utf-8"}
        url = 'https://oapi.dingtalk.com/robot/send?access_token=' + robot_id
        body = json.dumps(msg)
        requests.post(url, data=body, headers=headers)
        print('成功发送钉钉')
    except Exception as e:
        print("发送钉钉失败:", e)


def main():
    now_time = datetime.datetime.now()
    if datetime.datetime.now().hour >= 11:
        nex_time = now_time + datetime.timedelta(days=1)
    else:
        nex_time = now_time
    nex_time = nex_time.replace(hour=11, minute=0, second=0, microsecond=0)
    print(nex_time)
    while True:  # 在靠近目标时间时
        if datetime.datetime.now() < nex_time:
            continue
        else:
            break
    msg_content = '今日作业内容:\n'
    df = pd.read_csv(file_name, index_col=None)
    post_stat = 0
    for i in range(len(df)):
        time = datetime.datetime.strptime(df.at[i, 'date'], "%Y-%m-%d")
        if time <= datetime.datetime.now():
            pass
        else:
            post_stat = 1
            msg_content += '作业日期:' + str(time .year) + str('年') + str(time .month) + str('月') + str(time .day)\
                           + str('日') + '\n'
            msg_content += '作业时间:' + str(df.at[i, 'hour']) + '时' + '\n'
            msg_content += '作业地点:' + str(df.at[i, 'location']) + '\n'
            msg_content += '数量:' + str(df.at[i, 'number']) + str('台') + '\n'
            msg_content += '所属公司:' + str(df.at[i, 'company']) + '\n'
            if df.at[i, 'company'] == 'alibaba':
                msg_content += '注意事项:' + str('不要堵住地面通风口') + '\n'
    if post_stat == 1:
        send_dingding_msg(msg_content, robot_id='0d55a169f83d65c62337d9046ee74728fcd02e76aa9e576001854bf6fda36639')
    else:
        mss = '无最新工作任务'
        send_dingding_msg(mss, robot_id='0d55a169f83d65c62337d9046ee74728fcd02e76aa9e576001854bf6fda36639')
        pass


while True:
    try:
        main()
    except Exception as e:
        print(e)
        time.sleep(10)
