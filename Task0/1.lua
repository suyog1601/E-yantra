--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code SCOR_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			SCOR_LUA.lua
*  Created:				07/10/2020
*  Last Modified:		07/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
]]--

-- getTheTopper function finds the student name who scored max, i.e. Topper's name from the scorelist created by readScoreList function
function getTheTopper(score_list,N)
    -- find the max score
    top = {}
    topper = {}
    i = 1
    k = 1
    for token in string.gmatch(score_list[1], "[^%s]+") do
        topper[i] = token
        i = i+1
    end
    large = tonumber(topper[2])
    highest = topper[1]
    for j=1,N do
        i = 1
        for token in string.gmatch(score_list[j], "[^%s]+") do
            topper[i] = token
            i = i+1
        end
        num = tonumber(topper[2])
        if (num > large) then
            large = num
            highest = topper[1]
        end
    end
    top[k] = highest
    k =2
    for j=1,N do
        i = 1
        for token in string.gmatch(score_list[j], "[^%s]+") do
            topper[i] = token
            i = i+1
        end
        num = tonumber(topper[2])
        if(topper[1] ~= highest) then
            if (num == large) then
                large = num
                top[k] = topper[1]
                k = k+1
            end
        end
    end
    return top
    -- write your code here
 
end
 
-- readScoreList function creates the scorelist table from input
function readScoreList(N)
    local scorelist={}
    for i=1,N do
        list = io.read()
        scorelist[i] = list
    end
    -- write your code here
 
    return scorelist
end
 
-- for each case, call the readScoreList and getTheTopper functions to get the scores of students and then find the student name who scored max, i.e. Topper's name
tc = tonumber(io.read())
rankers = {}
for i=1,tc do
    local N=tonumber(io.read())
    score_list=readScoreList(N)

    rankers[i] = getTheTopper(score_list,N)
    
end

for n=1,tc-1 do
    l = 0
    table.sort(rankers[n])
    for Index, Value in pairs( rankers[n] ) do
        l = l + 1
        print(Value)
    end
end
l = 0
i=1
a = {}
table.sort(rankers[tc])
for Index, Value in pairs( rankers[tc] ) do
    l = l + 1
    a[i] = Value
    i = i + 1
end
for m=1,l-1 do
    print(a[m])
end
io.write(a[l])
