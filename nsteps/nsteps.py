def perm(n,X):
	i_ls=[0 for i in range(n+1)]
	i_ls[0]=1
	for i in range(1,n+1):
		i_ls[i]+=sum(i_ls[i-x] for x in X if i-x>=0)
	return i_ls[n]

print(perm(4,[1,2]))