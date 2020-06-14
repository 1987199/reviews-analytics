data = []
count = 0
with open('original.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('档案读取完了，总共有', len(data), '笔资料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均长度为', sum_len / len(data))