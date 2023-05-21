import os

files = os.listdir("./pics/")
files.sort()
print(files)
lines = """
<html><head></head><body>
<div style="font-size:36px;font-weight:bold;background-color:red;color:yellow;">
以下为程序测试数据，未经任何人工干预，所涉及标的不作推荐，不作为任何指导和买卖依据，据此买卖，风险自负。股市有风险，入市须谨慎！
</div>
<hr/>
<div>
<div style="font-weight:bold;font-size:24px;color:red;">+8%</div>
<div style="font-weight:bold;font-size:24px;color:blue;">-5%</div>
</div>
<hr/>
<div style="font-size:36px;font-weight:bold;background-color:red;color:yellow;">
所有测试数据，仅按每日价格进行计算，未考虑其他因素，如基本面变化、分红、转股、派现、停牌、风险警示、退市等等。
</div>
<hr/>
"""
for f in files:
    if f.endswith(".py"):
        continue
    else:
        lines = lines + '<div><img width="800px" src="./pics/'+f+'"/></div>'
lines = lines + "</body></html>"
with open("index.html", "w") as fp:
    fp.write(lines)

