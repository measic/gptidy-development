# PreCondition:
# Input: Pair= Hashset-> T (Rooted Triplet) toString({1,2},3)=1 2 3
# Input is a hashset of 3 numbers.
# Input also contains a leaf set two variables x,y
# Output:
#if statement modified to so that it gets added in both ways
function computeSN(T,L,x,y)
    X= [x]
    Z= [y]
	computed= []
	L1= []
	L1= copy(L) # Creating a copy to be used again
    while(!isempty(Z)) # Run until Z becomes empty
		z=Z[1]
        for a in X
			L= copy(L1)
			# Filter starts L- (X U Z)
			for p in X
				filter!(x -> x!=p,L) #removing all the elements of X in L
			end
			for p in Z
				filter!(x -> x!=p,L) #removing all the elements of Z in L
			end
			# Filter ends  L- (X U Z)
            for c in L
            	temp = [a,c,z]
            	temp2 = [z,c,a]
				temp3=[c,a,z]
				temp4=[c,z,a]
            	if(temp in T && !(temp in computed)) #pseudo code
            		#Z=Z U {c}
					append!(Z,c)
					Z = unique(Z) # Making Z unique to avoid redundancy
					append!(computed, temp)
				end
            	if(temp2 in T && !(temp2 in computed))
            		append!(Z,c)
					Z = unique(Z)
					append!(computed, temp2)
            	end
				if(temp3 in T && !(temp3 in computed))
            		append!(Z,c)
					Z = unique(Z)
					append!(computed, temp3)
            	end
				if(temp3 in T && !(temp4 in computed))
            		append!(Z,c)
					Z = unique(Z)
					append!(computed, temp4)
            	end
            	#or contains!(T,temp2))
            end
			# print("X=",string(X))
			# println()
			# print("Z=",string(Z))
        end
        h =Z[1]
        append!(X,h)
        splice!(Z,1)
		# println(Z)
    end
	X=sort(X)
    return unique(X)			#Returns a SubNetwork
end

function finalCheck(maximal)
    sortBySize(maximal)
    println("maximal wala subset: ",maximal)
    indexOfMax = length(maximal) #index Of max is the element with maxmum size
		x=1
		index=indexOfMax
		while(index!=1 && index<=length(maximal))
			curMaxElement = maximal[index]
			# println(curMaxElement)
			while(x<indexOfMax)
				if (findin(curMaxElement,maximal[x])!=Int64[] && length(findin(curMaxElement,maximal[x])) == length(SNs[x]))
					# println("SN== and curMax=",SNs[x],curMaxElement)
					# then remove x
					deleteat!(SNs,x)
					# println("Inside If statement",string(x))
					indexOfMax-=1
					x-=1
                end
			x+=1
            end
		index-=1
    end
#     deleteat!(maximal,x)
end

function maximalSubsets(SNs, L)
		# SNs are sorted according to its size
		sortBySize(SNs)
# 		filter!(x -> x!=L,SNs)
		# actually equal to the last element as the list is sorted by size
		indexOfMax = length(SNs) #index Of max is the element with maxmum size
		x=1
		index=indexOfMax
		while(index!=1 && index<=length(SNs))
			curMaxElement = SNs[index]
			# println(curMaxElement)
			while(x<indexOfMax)
				if (findin(curMaxElement,SNs[x])!=Int64[] && length(findin(curMaxElement,SNs[x])) == length(SNs[x]))
					# println("SN== and curMax=",SNs[x],curMaxElement)
					# then remove x
					deleteat!(SNs,x)
					# println("Inside If statement",string(x))
					indexOfMax-=1
					x-=1
				end
				x+=1
			end
			index-=1
		end
        finalCheck(SNs)
		return unique(SNs)
end

function retComputeSN(T,L)
	pairs=[]
	for i in eachindex(L)
		j=i
		while(j<=length(L))
			temp=[]
			append!(temp,[L[i],L[j]])
			append!(pairs,[temp])
			j+=1
		end
		i+=1
	end
	res = Array{Int64}[]
	for element in pairs
		temp=[]
		append!(temp,computeSN(T, L,element[1],element[2]))
		append!(res,[temp])
	end
	return res
end

function sortBySize(arr)
    i=key=j=0
    # print(i)
    for i=2: length(arr)
        key = arr[i]
        j=i-1

        while(j>=1 && length(arr[j])>length(key))
            arr[j+1]=arr[j]
            j=j-1
        end
        arr[j+1]=key
    end
    print("sorted = ",arr)
end

function main_ComputeSN()
#     T= [[1,2,3], [1,2,4], [1,2,5], [2,3,4], [3,4,2], [2,3,5], [3,4,5], [1,3,4],
# 	[3,4,1], [1,3,5], [1,4,5], [2,4,5]]
    T = [[1,2,3], [1,2,4], [1,2,5], [2,3,4], [2,3,5], [4,5,3], [1,3,4], [1,3,5],
        [4,5,1], [4,5,2], [3,4,1], [3,5,1], [3,4,2], [3,5,2]]
    
	L= [1,2,3,4,5]
    set_SN = retComputeSN(T,L)
    println("sub networks =",set_SN)
	maximumSubsets= maximalSubsets(set_SN,L)
    println("maximal subset  =",maximumSubsets) 
end

main_ComputeSN()
