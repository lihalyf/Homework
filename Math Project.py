import pandas as pd
def main():
    # input the departure airport
    print("Enter the first airport")
    start = str(input())
    #input the destination airport
    print("Enter the second airport")
    end = str(input())
    
    #narrow down the dataframe with distance only less than 8
    f = pd.read_csv('December 2017 Flights.csv')
    df = f[f.DISTANCE_GROUP < 8]
    list_origin = list(set(df.ORIGIN)) # get the list of departure
    
    # create a dictionary, key = origin, value = {destination: weight}, and the dictionary is the graph, --
    # key is the vertice of departure, the key in value is the vertice of destination, the value in value is the wegihted edge between those two vertices
    dic_origin = {}
    for i in range(len(list_origin)):
        df_new_origin = df[df.ORIGIN == str(list_origin[i])]
        dic_dest = {}
        list_dest = list(set(df_new_origin.DEST))
        for j in range(len(list_dest)):
            df_new_dest = df_new_origin[df_new_origin.DEST == str(list_dest[j])]
            dic_dest[list_dest[j]] = list(set(df_new_dest.DISTANCE_GROUP))
    
        dic_origin[list_origin[i]] = dic_dest
    
    #get all possible path between airports that is less than 8
    dic_path = {}
    findpath(start, 0, dic_origin, [start], dic_path, [start], end)
    
    #get the path with most connections, shortest distance and longest distance
    most_connections = 0
    shortest = 8
    longest = 0
    for path,distance_group in dic_path.items():
        if len(path) >= most_connections:
            most_connections = len(path)
        if distance_group <= shortest:
            shortest = distance_group
        if distance_group >= longest:
            longest = distance_group
    
    path_most_connection = {}
    path_shortest_distance = {}
    path_longest_distance = {}
    for path, distance_group in dic_path.items():
        if len(path) == most_connections:
            path_most_connection[path] = distance_group
        if distance_group == shortest:
            path_shortest_distance[path] = distance_group
        if distance_group == longest:
            path_longest_distance[path] = distance_group
    
    return dic_path, path_shortest_distance, path_longest_distance, path_most_connection
    
def findpath(airport, distance, dic_origin, path, result, memo, end): #memo stores the visited airport in the current path, which elimitate cycle in the path
    # return when the distance is larger than 7
    if distance > 7:
        return
    
    #return when we find the target destination airport
    if airport == end:
        strpath = str("")
        for ap in path:
            strpath = strpath + '_' + str(ap)
        
        result[strpath] = distance
        return
    
    #find the path
    for key,value in dic_origin[airport].items():
        # if airport is visted, directly continue the for loop
        if key not in memo:
            memo.append(key)
            for ds in value:
                distance = distance + ds
            path.append(key) # append current connected airport to the path
       
            findpath(key, distance, dic_origin, path, result, memo, end) # recursion
            
            # pop out current airport from path and for loop the next airport connected
            path.pop()
            for ds in value:
                distance = distance - ds
            memo.pop()
        else:
            continue
     
whole_path, shortest, longest, most_connections = main()
print("The whole path between two airports is", whole_path)
print("The shortest distance path between two airports is", shortest)
print("The longest distance path between two airports is", longest)
print("The path has most connections is", most_connections)