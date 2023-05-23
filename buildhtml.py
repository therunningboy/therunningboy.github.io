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

<pre>
2023-05-23
600438 通威股份 感觉 第二天 可以考虑 卖出
601012 隆基绿能 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
601633 长城汽车 感觉 第二天 根据分时走势 考虑卖出 或 有一定获利卖出 或 成交量明显放大卖出
601868 中国能建 感觉 第二天 根据分时走势 考虑卖出 或 有一定获利卖出 或 成交量明显放大卖出
002709 天赐材料 感觉 第二天 可以考虑 卖出
300059 东方财富 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
------------------------------
600660 福耀玻璃 感觉 第二天 可以考虑 卖出
300003 乐普医疗 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
600845 宝信软件 感觉 第二天 根据分时走势 考虑卖出 或 有一定获利卖出 或 成交量明显放大卖出
000858 五粮液 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
600690 海尔智家 感觉 第二天 可以考虑 卖出
------------------------------
002337 赛象科技 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002859 洁美科技 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
002050 三花智控 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
</pre>

<hr/>

<pre>
2023-05-12       -2     3272.36         指数 可能 长周期下降趋势 ↓ 
2023-05-15       0      3310.74         指数 可能 延续前趋势......
2023-05-16       -1     3290.99         指数 可能 长周期下降趋势 ↓ 
2023-05-17       1      3284.23          ↑ 指数 可能 长周期上升趋势
2023-05-18       0      3297.32         指数 可能 延续前趋势......
2023-05-19       2      3283.54          ↑ 指数 可能 长周期上升趋势
2023-05-22       0      3296.47         指数 可能 延续前趋势......
2023-05-23       -2     3246.24         指数 可能 长周期下降趋势 ↓ 
</pre>

<hr/>

<pre>
2023-05-23
000722 湖南发展 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
001229 魅视科技 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
001268 联合精密 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
002050 三花智控 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002129 TCL中环 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002138 顺络电子 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
002151 北斗星通 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002173 创新医疗 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002180 纳思达 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002360 同德化工 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002380 科远智慧 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002413 雷科防务 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002705 新宝股份 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002729 好利科技 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002747 埃斯顿 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002767 先锋电子 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002782 可立克 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002859 洁美科技 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
002880 卫光生物 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002896 中大力德 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
002921 联诚精密 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
002960 青鸟消防 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
003025 思进智能 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
003028 振邦智能 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
003042 中农联合 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300007 汉威科技 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300018 中元股份 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300086 康芝药业 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300112 万讯自控 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300188 美亚柏科 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300250 初灵信息 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
300481 濮阳惠成 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
300486 东杰智能 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300537 广信材料 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300667 必创科技 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300679 电连技术 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300690 双一科技 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300707 威唐工业 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300708 聚灿光电 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
300780 德恩精工 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
300787 海能实业 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
300806 斯迪克 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300817 双飞股份 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300921 南凌科技 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
300946 恒而达 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
300960 通业科技 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301008 宏昌科技 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301022 海泰科 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301033 迈普医学 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301086 鸿富瀚 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301111 粤万年青 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301113 雅艺科技 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301130 西点药业 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301131 聚赛龙 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301151 冠龙节能 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301160 翔楼新材 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301206 三元生物 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
301218 华是科技 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
301327 华宝新能 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
301377 鼎泰高科 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
600032 浙江新能 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
600262 北方股份 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
600562 国睿科技 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
600862 中航高科 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
600992 贵绳股份 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
603003 龙宇股份 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
603070 万控智造 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
603165 荣晟环保 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
603192 汇得科技 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
603538 美诺华 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
603773 沃格光电 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
603789 星光农机 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
603848 好太太 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
603990 麦迪科技 感觉 第二天 根据分时走势 考虑买入 或 继续持仓 或 成交量明显放大卖出
605286 同力日升 感觉 第二天 可以考虑买入 或 继续持仓 或 成交量明显放大卖出
</pre>
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

