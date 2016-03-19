#pickle模块
#用于把列表，字典，元组打包成一个二进制文件

#创建文件
import pickle

a = [1,2,3,4,5] #需要保存的列表
pickle_file = open(r'C\A\列表.pkl','wb') #创建一个文件，文件后缀任意，建议用pkl
pickle.dump(a, pickle_file)  #把列表a保存到文件中

pickle_file.close()


#调用文件
import pickle

pickle_file = open(r'C\A\列表.pkl','rb')
a = pickle.load(pickle_file)

pickle_file.close()
