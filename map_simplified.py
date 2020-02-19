
from pyecharts.charts import Map  # 引入Map
from pyecharts import options as opts  # 引入设置项

provinces=['北京','天津','河北','山西','内蒙古',
           '辽宁','吉林','黑龙江','上海','江苏',
           '浙江','安徽','福建','江西','山东',
           '河南','湖北','湖南','广东','广西',
           '海南','重庆','四川','贵州','云南',
           '陕西','甘肃','青海','宁夏','新疆','西藏']

values=[72,18,18,13,11,
        27,6,21,53,47,
        128,70,56,48,75,
        128,1423,100,151,46,
        33,110,69,7,26,
        35,14,4,7,5,0]  # 转成pyecharts所需的格式
data_list=[[provinces[i],values[i]]for i in range(len(provinces))]

# 定义数据分组、每组数据的范围及其颜色：
# 自定义的每一段的范围，以及每一段的文字，以及每一段的特别的样式。例如：
# 不指定 max，表示 max 为无限大（Infinity）
piece = [{"min": 1000, "color": 'darkred'},
         {"min": 100, "max": 999, "color": 'firebrick'},
         {"min": 10, "max": 99, "color": 'salmon'},
         {"min": 1, "max": 9, "color": 'peachpuff'}, ]

# 初始化地图
map = Map()
# 设置地图相关项
map.set_global_opts(title_opts=opts.TitleOpts(title="疫情地图", pos_left='center'),
                    visualmap_opts=opts.VisualMapOpts( max_=200, is_piecewise=True, pieces=piece), )
map.add("", data_list, "china")
# 生成地图
map.render('map_simplifed.html')  # 初始化地图