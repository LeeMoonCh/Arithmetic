#coding:utf8

from sklearn import tree
from sklearn import preprocessing
import pydotplus

#将数据集data中的字符串属性全部转化为对应的标签
#data为矩阵，同tree.DecisionTreeClassifier.fit方法中的数据
#返回值le_list是preprocessing.LabelEncoder()对象的列表
#str_index是属性中字符串类型的下标
def preprocess(data):
    str_index = []
    #temp_label = []
    le_list = []
    le_num = 0
    for i in range(0,len(data[1])):
        if (isinstance(data[1][i], str)):
            str_index.append(i)
     #整理出labelEncoder
    for index in str_index:
        temp_label = []
        for i in data:
             temp_label.append(i[index])
             le_list.append(preprocessing.LabelEncoder())
             le_list[le_num].fit(temp_label)
         #根据labelEncoder修改原始数据
         #print temp_label
        for i in data:
             i[index] = le_list[le_num].transform([(i[index])])[0]
         
        le_num += 1
        
    return (le_list, str_index)
#天气情况,每行是一个数据，分别为天气，温度，湿度风况
data = [["Sunny", 85, 85, "No"], 
         ["Sunny", 80, 90, "Yes"],
         ["Cloudy", 83, 78, "No"], 
         ["Rainy", 70, 96, "No"], 
         ["Rainy", 68, 80, "No"],
         ["Rainy", 65, 70, "Yes"],
         ["Cloudy", 64, 65, "Yes"],
         ["Sunny", 72, 95, "No"],
         ["Sunny", 69, 70, "No"],
         ["Rainy", 75, 80, "No"],
         ["Sunny", 75, 70, "Yes"],
         ["Cloudy", 72, 90, "Yes"],
         ["Cloudy", 81, 75, "No"],
         ["Rainy", 71, 80, "Yes"]]
#针对每行数据，分类为适合运动与不适合运动
labels = ["nosuit", "nosuit", "suit", "suit", "suit",
           "nosuit", "suit", "nosuit", "suit", "suit",
           "suit", "suit", "suit","nosuit"]
#新建一个DecisionTreeClassifier的实例，这个实例默认为基尼指数，我们这里改成香农值，也就是信息增益
le_list, str_index = preprocess(data)
#print le_list
#print str_index
#clf是DecisionTreeClassifier的一个实例，这个实例默认使用基尼指数进行树创建，我们这里改成香农熵
clf = tree.DecisionTreeClassifier(criterion="entropy")
#训练数据
trees = clf.fit(data,labels)

#print clf.feature_importances_
#使用export_graphviz()函数，将树结构存储起来。
with open("iris.txt", 'w') as f:
    f = tree.export_graphviz(trees, out_file=f)
#但是我想看图怎么办？看决策树的结构图？
#有两种办法，一个使用from IPython.display import Image和pydotplus一起使用，另一个使用import pydotplus将图片存为pdf格式。我们这里使用pydotplus
#哎，第一种使用没成功，可能我的环境没有配好。graph没有write_pdf方法！！！！
#dot_data = StringIO()
#dot_data = tree.export_graphviz(trees, out_file=None) 
#graph = pydotplus.graph_from_dot_data(dot_data)

test = [["Rainy", 71, 80, "Yes"]]
for index in range(0, len(str_index)):
    for i in test:
        i[str_index[index]] = le_list[index].transform([i[str_index[index]]])[0]
#print test
#使用predictc测试数据
print clf.predict(test)
print clf.predict_proba(test)
print clf.score(data, labels)





















