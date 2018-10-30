import operator
T=int(input())
while T>0:
		N,M=map(int,input().split())
		capacity=list(map(int,input().split()))
		weights=list(map(int,input().split()))
		num=list(map(int,input().split()))
		if max(capacity)<max(weights):
			print(-1)
		else:
			
			
			'''
			for i in sorted_weights:
				divide[i]=0

			print("divide",divide)
			'''
			'''sorted_capacity=sorted(capacity,reverse=True)
			print("sorted_capacity",sorted_capacity)
			'''
			divide={}
			d_capacity={}
			for i in range(M):
				d_capacity[i]=capacity[i]

			
			sort_d_capacity = sorted(d_capacity.items(), key=operator.itemgetter(1),reverse=True)
			
			d_cakes={}
			for num_i,weights_j in zip(num,weights):
				d_cakes[num_i]=weights_j

			sort_d_cakes = sorted(d_cakes.items(), key=operator.itemgetter(1),reverse=True)
			print("sort_d_cakes",sort_d_cakes)
			for i in num:
				divide[i]=[]
			a=0
			b=0
			weight_=sorted(weights,reverse=True)
			while(a<M and b<N):
				friend=sort_d_capacity[a][0]
				cap=sort_d_capacity[a][1]
				weight=sort_d_cakes[b][1]
				'''
				print("a",a)
				print("weight",sort_d_cakes[b][1])
				print("b",b)
				print("capacity",sort_d_capacity[a][1])
				print("friend",friend)
				'''
				if(cap>=weight):
					a+=1
					for i in sort_d_cakes:
						print("start of divide")
						if(i[1]<=weight):
							no_cakes=i[0]
							divide[no_cakes].append(friend)
								
						
					print(divide)
				else:
					b+=1
					print("no divide")

		T-=1
		print(divide)



    
    
    
    
    


