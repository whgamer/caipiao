import requests
from time import *
from random import randint
from fake_useragent import UserAgent
ua = UserAgent()
header = {
    'Host' : 'www.wenjuan.com',
    # 'User-Agent': ua.random,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://www.wenjuan.com/s/22Uf6vA/',
    'Cookie' : 'Hm_lvt_ad0624cf51ddee8ef3bd2513c2add79b=1565849696; Hm_lpvt_ad0624cf51ddee8ef3bd2513c2add79b=1565849696; acw_tc=2f624a0b15658496935327142e47918d476fe022eea61a77cccbd317ba8b33; browser_id=5d54f85df27e6966fbd948fd; _xsrf=e35c229c34d645249d4d13c2b62962a9; sessionid=bms1bVhhWUxvcHE2RmI0ODVkNTRmODVk|1565849693|b2e6213407f7ea526123a104ab2593931ec733fd; mtc=f14c5e4fb512891ae7fcb40266df61e6'

           }
data ={"5d42559f3631f27315be179e":["5d42559f3631f27315be17af"],"5d42559f3631f27315be179f":{"5d42559f3631f27315be17c2_open":"张工 18563170739"},"5d42559f3631f27315be17a0":["5d42559f3631f27315be17c3"],"5d42559f3631f27315be17a2":{"5d4255a03631f27315be17da_open":"同意"},"5d4258aa92beb548ee4e2e83":{"5d4258aa92beb548ee4e2e84_open":"深圳坐标软件公司\n暂未存在"},"5d42559f3631f27315be17a3":{"5d4255a03631f27315be17db_open":"是 ，否，否 ，等待荣成市人民医院成熟解决方案"},"5d42559f3631f27315be17a5":{"5d4255a03631f27315be17dd_open":"否 否  等待荣成市人民医院成熟解决方案 预计12月中旬"},"5d42559f3631f27315be17a7":{"5d4255a03631f27315be17df_open":"是 否 否 暂未存在"},"5d42559f3631f27315be17ab":{"5d4255a03631f27315be17e3_open":"是 否 否 暂未存在"},"5d42559f3631f27315be17ac":{"5d4255a03631f27315be17e4_open":"否 否"},"5d42559f3631f27315be17a8":{"5d4255a03631f27315be17e0_open":"否 暂未确定  等待荣成市人民医院成熟模式 12月中旬\n否"},"5d42559f3631f27315be17a9":{"5d4255a03631f27315be17e1_open":"否"},"5d42559f3631f27315be17aa":{"5d4255a03631f27315be17e2_open":"否  等待荣成市人民医院成熟模式 12月中旬"},"5d42559f3631f27315be17ad":{"5d4255a03631f27315be17e5_open":"否  等待荣成市人民医院成熟模式 12月中旬"}}
url ="https://www.wenjuan.com/s/22Uf6vA/"
r =requests.post(url,data=data,headers =header)
print(r.text)