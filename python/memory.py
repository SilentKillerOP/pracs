import random 

L1_cache = [] 

L2_cache = [] 

l1p = 0 

l2p = 0 

low = 0 

high = 511 

L1_cache_hits = 0 

L2_cache_hits = 0 

l1_cache_time = 20 

l2_cache_time = 60 

main_memory_time = 120 

main_memory = [] 

print('Word \t\t Location \tTime') 

for i in range(0, 100):  

    word = random.randint(low, high) 

    main_memory+= [word] 

    if (word in L1_cache):  

        L1_cache_hits += 1 

        avg1 = int(((L1_cache_hits*1.0/(i+1))*l1_cache_time) + ((1-(L1_cache_hits*1.0/(i+1)))*(L2_cache_hits*1.0/(i+1)) * (l2_cache_time+l1_cache_time)*1.0) + ((1-(L1_cache_hits*1.0/(i+1))) * (1-(L2_cache_hits*1.0/(i+1))) * (l2_cache_time+l1_cache_time+main_memory_time)*1.0)) 

        print(str(word)+"\t\t in L1 \t\t"+str(avg1)) 

        continue 

    elif(word in L2_cache):  

        L2_cache_hits += 1 

        avg2=int(((L1_cache_hits*1.0/(i+1))*l1_cache_time) +((1-(L1_cache_hits*1.0/(i+1)))*(L2_cache_hits*1.0/(i+1))*(l2_cache_time+l1_cache_time)*1.0 ) + ( (1-(L1_cache_hits*1.0/(i+1))) * (1-(L2_cache_hits*1.0/(i+1))) * (l2_cache_time+l1_cache_time+main_memory_time)*1.0 ) ) 

        print(str(word)+"\t\t in L1 \t\t"+str(avg2)) 

        if(len(L1_cache)<32): 

            L1_cache.append(word) 

        else: 

            l1p=(l1p+1)%32 

            L1_cache.insert(l1p,word) 

            continue 

    else: 

        avg3=int(((L1_cache_hits*1.0/(i+1))*l1_cache_time)+((1-(L1_cache_hits*1.0/(i+1)))*(L2_cache_hits*1.0/(i+1))*(l2_cache_time+l1_cache_time)*1.0 ) + ( (1-(L1_cache_hits*1.0/(i+1))) * (1-(L2_cache_hits*1.0/(i+1))) * (l2_cache_time+l1_cache_time+main_memory_time)*1.0 ) ) 

        print(str(word)+"\t\t in MM \t\t"+str(avg3)) 

        if(len(L1_cache)<32):L1_cache.append(word) 

        else:L1_cache.insert(l1p,word) 

        l1p=(l1p+1)%32 

        if(len(L2_cache)<128): 

            L2_cache.insert(l2p,word) 

            L2_cache.append(word+1) 

        else: 

            L2_cache.insert(l2p,word-1) 

            L2_cache.insert(l2p+1,word) 

            l2p = (l2p+2) % 64 

    L1_cache = list(set(L1_cache)) 

    L2_cache = list(set(L2_cache)) 

print("Size of L1 cache:",len(L1_cache) ,"\nSize of L2_cache:" ,random.randint(len(L1_cache) , len(main_memory)) ,"\nSize of memory", len(main_memory)) 
print("Hits of L1 cache:",L1_cache_hits , "\nHits of L2 cache:",L2_cache_hits)