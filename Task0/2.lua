--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code WLEN_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:            WLEN_LUA.lua
*  Created:             07/10/2020
*  Last Modified:       07/10/2020
*  Author:              e-Yantra Team
*
*****************************************************************************************
]]--
 
-- countChar function to count the characters in each word of given string
function countChar(str)
    -- write your code here
    i = 1
    x = 0
    digit = {}
    for char in string.gmatch(str,"[^%s]+") do
        if(x == 0) then
            l = string.len(char)
            z = l -1
            digit[i] = z
            x = x +1
        else
            l = string.len(char)
            digit[i] = l
        end
        i = i+1
    end
    return digit
end
 
-- for each case, call countChar function to count the characters in each word of given string
tc = tonumber(io.read())
res = {}
for i=1,tc do
    str=io.read()
    res[i] = countChar(str)
end

for i=1,tc-1 do
    y = table.concat(res[i],",")
    print(y)
end
y = table.concat(res[tc],",")
io.write(y)