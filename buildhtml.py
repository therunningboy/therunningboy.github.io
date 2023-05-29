import os

files = os.listdir("./pics/")
files.sort()
print(files)
lines = """
<html>

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</head>


<body>
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

<pre>
2023-05-29
600438 -4 通威股份 感觉 第二天 根据分时走势 考虑卖出 或 有一定获利卖出 或 成交量明显放大卖出
601012 -5 隆基绿能 感觉 第二天 可以考虑 卖出
601633 -4 长城汽车 感觉 第二天 根据分时走势 考虑卖出 或 有一定获利卖出 或 成交量明显放大卖出
601868 -2 中国能建 没有感觉
002709 -5 天赐材料 感觉 第二天 可以考虑 卖出
300059 -4 东方财富 感觉 第二天 根据分时走势 考虑卖出 或 有一定获利卖出 或 成交量明显放大卖出
------------------------------
600660 -5 福耀玻璃 感觉 第二天 可以考虑 卖出
300003 4 乐普医疗 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
600845 0 宝信软件 没有感觉
000858 -1 五粮液 没有感觉
600690 -4 海尔智家 感觉 第二天 根据分时走势 考虑卖出 或 有一定获利卖出 或 成交量明显放大卖出
------------------------------
002337 -4 赛象科技 感觉 第二天 根据分时走势 考虑卖出 或 有一定获利卖出 或 成交量明显放大卖出
002859 -1 洁美科技 没有感觉
002960 -3 青鸟消防 感觉 第二天 根据分时走势 考虑卖出 或 有一定获利卖出 或 成交量明显放大卖出
002129 -3 TCL中环 感觉 第二天 根据分时走势 考虑卖出 或 有一定获利卖出 或 成交量明显放大卖出
002515 -4 金字火腿 感觉 第二天 根据分时走势 考虑卖出 或 有一定获利卖出 或 成交量明显放大卖出
002050 1 三花智控 没有感觉


</pre>

<hr/>

<pre>
2023-05-12 	 -2	3272.36		指数 可能 长周期下降趋势 ↓ 
2023-05-15 	 0	3310.74		指数 可能 延续前趋势......
2023-05-16 	 -1	3290.99		指数 可能 长周期下降趋势 ↓ 
2023-05-17 	 1	3284.23		 ↑ 指数 可能 长周期上升趋势
2023-05-18 	 0	3297.32		指数 可能 延续前趋势......
2023-05-19 	 2	3283.54		 ↑ 指数 可能 长周期上升趋势
2023-05-22 	 0	3296.47		指数 可能 延续前趋势......
2023-05-23 	 -2	3246.24		指数 可能 长周期下降趋势 ↓ 
2023-05-24 	 0	3204.75		指数 可能 延续前趋势......
2023-05-25 	 0	3201.26		指数 可能 延续前趋势......
2023-05-26 	 0	3212.5		指数 可能 延续前趋势......
2023-05-29 	 -1	3221.45		指数 可能 长周期下降趋势 ↓ 


</pre>

<hr/>

<pre>
2023-05-29
001231 5 农心科技 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002382 5 蓝帆医疗 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002913 4 奥士康 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
300007 5 汉威科技 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300570 5 太辰光 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300667 5 必创科技 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300884 5 狄耐克 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301072 5 中捷精工 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301132 5 满坤科技 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301176 5 逸豪新材 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301187 5 欧圣电气 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301191 5 菲菱科思 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301282 5 金禄电子 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
603165 5 荣晟环保 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
603203 5 快克智能 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出

</pre>
<hr/>
"""
for f in files:
    if f.endswith(".py"):
        continue
    else:
        stockcode = f.split("_")[1]
        if stockcode.startswith("60"):
            stockcode = "SH" + stockcode
        elif stockcode.startswith("68"):
            stockcode = "SH" + stockcode
        elif stockcode.startswith("00"):
            stockcode = "SZ" + stockcode
        elif stockcode.startswith("30"):
            stockcode = "SZ" + stockcode
        elif stockcode.startswith("43"):
            stockcode = "BJ" + stockcode
        elif stockcode.startswith("87"):
            stockcode = "BJ" + stockcode
        elif stockcode.startswith("83"):
            stockcode = "BJ" + stockcode
        lines = lines + '''
        <div>
        <div style="float:left; width:800px; 
        text-align:center;background-color:#dddddd;
        padding-top:10px;padding-bottom:10px;">
            <a  style="text-decoration:none;font-weight:bold;
            color:red;" 
            target="_blank" href="https://xueqiu.com/S/'''+stockcode+'''">'''+stockcode+'''</a>
            </div>
            <div>
            <img width="800px" src="./pics/'''+f+'''"/>
            </div>
        </div>
        '''
lines = lines + "</body></html>"
with open("index.html", "w") as fp:
    fp.write(lines)

