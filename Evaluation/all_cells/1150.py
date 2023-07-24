include("ComputeSN.jl")
include("OneHybridLeaf.jl")

# Bugs:
# Bug1: One node is always missing in the OneHybridLeaf algorith (OneHybridLeaf.jl)
# Bug2: Maximal Subsets algorithm is giving a wrong answer for Example2 (ComputeSN.jl)

# finalAdjList = Dict{Int64,Array}()

function levelOne(T,L, finalAdjList, rootNode)
	set_SN = retComputeSN(T,L)
	maximumSubsets= maximalSubsets(set_SN,L)
	println("maximal subsets=", maximumSubsets)
    
	for SN in maximumSubsets
		if (length(SN)>=3)
			# temp=retComputeSN(T,SN)
			# maximumSets=maximalSubsets(temp,L)
			# println(maximumSets)
			L=SN
			finalAdjList= levelOne(T,L, finalAdjList, rootNode)
		else
            # TODO Check for overlapping
#           println("need to make a tree with these 2 nodes/ make adjacency list")
#           newAdjList = Dict{Int64,Array}()
            println("Maximal Subsets in else case", SN)
            leastNode =-1
            if(length(finalAdjList) > 0)
                leastNode = minimum(collect(keys(finalAdjList)))-1 
            end
            
            if(length(SN)==2)
                addVertex(finalAdjList,leastNode,SN)
            end
            println("newAdjList",finalAdjList)
#             return finalAdjList
		end
	end
    
    if(length(maximumSubsets)==2)
        println("Maximal Subsets second if case", maximumSubsets)
        println("adjList before adding edge=",finalAdjList) 
        
        if(rootNode==0)
            rootNode=-1
        end
        
          #TODO get -5 and 5 programmatically
        # new root = least negative node -1 and behaves as new root node.
        newRoot = minimum(collect(keys(finalAdjList))) -1 
        
#         println("maximumSubset containing 5",maximumSubsets)
        
        keysOfAdjList=collect(keys(finalAdjList))
        
#         println("keysOfAdjList",keysOfAdjList)
        # bug if maximalsubset[1]= 1234 and maximalSubset[2]= 5 and when 4 is in the keys alread
        newNode = 0
        for i in maximumSubsets[1]
            if (any(x->x!=maximumSubsets[1], keysOfAdjList))# if keys contains value
                newNode = maximumSubsets[1]
            else
                newNode = maximumSubsets[2]
            end
            break
        end
                     
        println("newNode", newNode)
        
        addVertex(finalAdjList,rootNode,[newRoot])
        addVertex(finalAdjList,newRoot,newNode)
        rootNode = newRoot        
        println("adding 5 to adjList", finalAdjList)
        
        return finalAdjList
        
    elseif(length(maximumSubsets)>=3)
        println("SNs before finding consistentcy ",maximumSubsets)
        adjLists = oneHybridLeaf(maximumSubsets)
        rootNode = -1
        consistentAdjList = returnConsistentAdjList(adjLists,maximumSubsets,L,T) 

        #         connect the consistent adjList with final AdjList
        println("consistentN=",consistentAdjList)
        println("adjlist before replacing ", finalAdjList)

        finalAdjList= consistentAdjList

        return finalAdjList
    end
    return finalAdjList
end

function main_func()
	T= [[1,2,3], [1,2,4], [1,2,5], [2,3,4], [3,4,2], [2,3,5], [3,4,5], [1,3,4],
	[3,4,1], [1,3,5], [1,4,5], [2,4,5],[2,1,3]]
#     T = [[1,2,3], [1,2,4], [1,2,5], [2,3,4], [2,3,5], [4,5,3], [1,3,4], [1,3,5],
#         [4,5,1], [4,5,2], [3,4,1], [3,5,1], [3,4,2], [3,5,2]]
    
	L= [1,2,3,4,5]
# 	set_SN = retComputeSN(T,L)
	# # println(set_SN)
	# var =maximalSubsets(set_SN,L)
	# println("Maximal Subsets=",string(var))
    adjList=Dict{Int64,Array}()
#     root node passed as 0
	levelOne(T,L, adjList, 0)
end
main_func()

# answer: adding 5 to adjListDict{Int64,Array}(Pair{Int64,Array}(4, [-2]),Pair{Int64,Array}(-4, [-2, -3, 3]),Pair{Int64,Array}(-3, [1, 2, -4, -1]),Pair{Int64,Array}(2, [-3]),Pair{Int64,Array}(-2, [4, -4, -1]),Pair{Int64,Array}(-1, [-2, -3, -5]),Pair{Int64,Array}(3, [-4]),Pair{Int64,Array}(-5, [-1, 5]),Pair{Int64,Array}(5, [-5]),Pair{Int64,Array}(1, [-3]))