#coding = utf-8
import numpy as np
from sklearn.neural_network import MLPClassifier

def read_feature():
	mat = np.zeros(shape=(23297, 666))  #602+64=666
	i=0
	with open("example_graphs/reddit.feature") as file:
		lines=file.readlines()
		for line in lines:
			line = line.split(' | ')
			mat[i][:602]=np.array(line[1].split())
			#print(mat[i])
			i+=1



	with open("example_graphs/reddit.embeddings") as file:
		lines = file.readlines()
		for line in lines:
			line = line.split()
			index=line[0]
			mat[int(index)][602:666] = np.array(line[1:65])
			# print(mat[i])

	mat1 = np.zeros(shape=(4000, 666))  # 602+64=666，unlabeled
	mat2 = np.zeros(shape=(19297, 666))  # 602+64=666，labeled
	mat1=mat[0:4000,:]
	mat2=mat[4000:,:]
	return mat1,mat2
'''
	mat = mat.tolist()
	with open("example_graphs/newreddit.feature",'w') as f:
		for i in range(len(mat)):
			f.write(str(mat[i]))
			f.write('\n')
	f.close()

	mat1 = mat1.tolist()
	with open("example_graphs/newreddit1.feature", 'w') as f:
		for i in range(len(mat1)):
			f.write(str(mat1[i]))
			f.write('\n')
	f.close()

	mat2 = mat2.tolist()
	with open("example_graphs/newreddit2.feature", 'w') as f:
		for i in range(len(mat2)):
			f.write(str(mat2[i]))
			f.write('\n')
	f.close()
'''


def read_label():
	mat = np.zeros(shape=(19297, 41))
	i = 0
	with open("example_graphs/reddit.label") as file:
		lines = file.readlines()
		for line in lines:
			line = line.split(' | ')
			mat[i][:41] = np.array(line[1].split())
			# print(mat[i])
			i += 1
	return mat
'''
	mat = mat.tolist()
	with open("example_graphs/newreddit.label", 'w') as f:
		for i in range(len(mat)):
			f.write(str(mat[i]))
			f.write('\n')
	f.close()
'''

def mlp():
	clf = MLPClassifier(hidden_layer_sizes=(100,100),
						activation='logistic', solver='adam',
						learning_rate_init=0.0001, max_iter=1000)
	clf.fit(mat2, label)
	res = clf.predict(mat1)
	return res
if __name__ == "__main__":
	mat1,mat2=read_feature()
	label=read_label()
	predict_label=mlp()
	#predict_label = predict_label.tolist()
	i=0
	with open("example_graphs/1701214038.pred.label", 'w') as f:
		for line in predict_label:
			f.write(str(i))
			f.write(' |')
			for point in line:
				f.write(' ')
				f.write(str(int(point)))
			f.write('\n')
			i+=1
	f.close()
