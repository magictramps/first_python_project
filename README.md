# 腾讯实时疫情获取数据
## 第一节

 `https://news.qq.com/zt2020/page/feiyan.htm#/area?pool=bj` 
 发现数据通过调用api返回json格式的数据 
 

 `https://view.inews.qq.com/g2/getOnsInfo?name=disease_other` 
 `https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5` 两个API返回全国历史数据和全国各城市数据
 
 通过`requests` 添加消息头请求获取消息以后，使用json来格式化获取的数据，主要考察`Tuple（元组）`和`Dictionary（字典）`的数据获取和转换，其中涉及 `for`循环的使用
 
 ```python
# Tuple 
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素

# Dictionary（字典）
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
```
## 第二节 （`Object of type 'Decimal' is not JSON serializable 错误` ）
* 将获取到的数据存放到`mysql`数据库中，实现数据持久化 
* 通过`pymysql` 来创建数据库连接，将数据存放到数据库对应的表中，后续也将通过数据库连接获取表中的数据传给前端页面
 此时发现一个`error` 既`Object of type 'Decimal' is not JSON serializable` 导入`simplejson` 
* 知识点：`dict.get(key, default=None)` `%s 占位符` `for循环` `sql 语句执行完成以后的commit操作`
```python
for k, v in dic.items():
            # item 格式 {'2020-01-13': {'confirm': 41, 'suspect': 0, 'heal': 0, 'dead': 1}
            if not cursor.execute(sql_query, k):
                cursor.execute(sql, [k, v.get("confirm"), v.get("confirm_add"), v.get("suspect"),
                                     v.get("suspect_add"), v.get("heal"), v.get("heal_add"),
                                     v.get("dead"), v.get("dead_add")])
```
