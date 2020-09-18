import time
import datetime
import json
import requests

# 健康打卡的URL地址
check_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"

sckey = input()

# POST提交的json字段，根据自己的修改
jsons = {"businessType":"epmpics","method":"submitUpInfo","jsonData":{"deptStr":{"deptid":226924,"text":"信息工程学院-计算机系-计20-2"},"areaStr":"{\"streetNumber\":\"\",\"street\":\"\",\"district\":\"土默特左旗\",\"city\":\"呼和浩特市\",\"province\":\"内蒙古自治区\",\"town\":\"\",\"pois\":\"北苑公寓\",\"lng\":111.56177100000286,\"lat\":40.80136598122704,\"address\":\"土默特左旗北苑公寓\",\"text\":\"内蒙古自治区-呼和浩特市\",\"code\":\"\"}","reportdate":1600435475607,"customerid":"533","deptid":226924,"source":"app","templateid":"pneumonia","stuNo":"202010201016","username":"于峰","phonenum":"","userid":"24902731",
"updatainfo":[{"propertyname":"temperature","value":"36.4"},{"propertyname":"symptom","value":"无症状"},{"propertyname":"isTouch","value":"否"},{"propertyname":"bodyzk","value":"否"},{"propertyname":"xinqing","value":"否"},{"propertyname":"assistRemark","value":""},{"propertyname":"cxjh","value":"无"},{"propertyname":"isAlreadyInSchool","value":"本专科生"},{"propertyname":"area1","value":"金川校区"},{"propertyname":"jtdz","value":"汉族"},{"propertyname":"emergencyContact","value":"18247640704"},{"propertyname":"age","value":"许霞"}],"gpsType":1}}
response = requests.post(check_url, json=jsons)
# 以json格式打印json字符串
res = json.dumps(response.json(), sort_keys=True, indent=4, ensure_ascii=False)
print(res)

SCKEY = sckey
now_time = datetime.datetime.now()
bj_time = now_time + datetime.timedelta(hours=8)

test_day = datetime.datetime.strptime('2020-12-19 00:00:00', '%Y-%m-%d %H:%M:%S')
date = (test_day - bj_time).days
desp = f"""
------
### 现在时间：
```
{bj_time.strftime("%Y-%m-%d %H:%M:%S %p")}
```
### 打卡信息：
------
| Text                           | Message |
| :----------------------------------- | ---: |
| 专业/部门                            | 1 |
| 姓名                                 | 2  |
| 学号                                 |  3   |
| 当前位置                             |  4  |
| 今日体温                             |   正常温度(小于37.3)   |
| 自己当日所在位置                     |   在校（含当日在校内居住）   |
| 身份类别                             |   内地学生   |
| 是否出现可以症状                     |   无   |
| 是否存在高危行为                      |    无  |
| 被要求采取医学措施                    |   无   |
| 家庭成员身体状况                      |   良好   |
| 所在小区是否有疫情                   |   无   |
| 居民健康码颜色                       |   绿色   |
| 本人电话                             | 5  |
| 紧急联系人姓名                       |    6  |
| 紧急联系人电话                       |  7    |
------
```
{res}
```
> 关于打卡信息
>
> 1、成功则打卡成功
>
> 2、系统异常则是打卡频繁

### ⚡考研倒计时:
```
{date}天
```

>
> [GitHub项目地址](https://github.com/ReaJason/17wanxiaoCheckin-Actions) 
>
>期待你给项目的star✨
"""

headers = {
    "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
}

send_url = f"https://sc.ftqq.com/{SCKEY}.send"

params = {
    "text": f"完美校园健康打卡---{bj_time.strftime('%m-%d')}",
    "desp": desp
}

# 发送消息
response = requests.post(send_url, data=params, headers=headers)
if response.json()["errmsg"] == 'success':
    print("Server酱推送服务成功")
else:
    print("Server酱推送服务失败")
