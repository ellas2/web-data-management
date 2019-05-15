import sys

def AlteredFagin(input_files, k):
	data = []
	for i in range(len(input_files)):
		data.append(LoadData(input_files[i]))
	return FaginAlg(data, k)


def LoadData(filename):
	with open(filename) as f:
		data = f.readlines()

	ranks = {}
	order = []
	for lines in data:
		params = lines.split(",")
		name = params[0]
		score = params[1]
		ranks[name] = float(score)
		order.append(name)

	return [ranks, order]


def FaginAlg(data, k):
	seen = {}
	for p in range(len(data)):
		seen[p] = {}
	seen_all = {}
	ranks_aggr = {}
	i = 0
	stop = 0

	while stop != 1:
		for m in range(len(data)):
			max_arr = []
			item = data[m][1][i]
			for elem in data:
				if item in elem[0]:
					max_arr.append(elem[0][item])
				else:
					avg_in_file = sum(elem[0].values())/len(elem[0])
					max_arr.append(avg_in_file)
			aggregator = max(max_arr)
			ranks_aggr[item] = aggregator
			seen[m][item] = 1

			seen_in_all = True
			for j in range(len(data)):
				if item not in data[j][0]:
					seen_in_all = False
					break
				elif item not in seen[j]:
					seen_in_all = False
					break
			if seen_in_all:
				seen_all[item] = ranks_aggr[item]
			if len(seen_all) >= k:
				stop = 1
				break
		i = i + 1

	print("Ranked: " + str(ranks_aggr))
	print("Seen all: " + str(seen_all))
	print("Actions: " + str(i * len(data)) + "\n")
	return sorted(ranks_aggr.items(), key=lambda x: x[1], reverse=True)[0:k]

input_files = ["data1.csv","data2.csv","data3.csv"]
print("for k = 1: ")
print(AlteredFagin(input_files, 1))
print("\n")
print("for k = 2: ")
print(AlteredFagin(input_files, 2))
print("\n")
print("for k = 3: ")
print(AlteredFagin(input_files, 3))

