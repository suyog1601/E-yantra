--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code INV_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:            INV_LUA.lua
*  Created:             07/10/2020
*  Last Modified:       07/10/2020
*  Author:              e-Yantra Team
*
*****************************************************************************************
]]--
 
-- manageInventory function to add, update / delete items to / from the Inventory
function manageInventory()
    -- reading total Items N
    N = tonumber(io.read())
    i = 1
    a = {}
    b = {}
    -- write your code here
    for i=1,N do
        str = io.read()
        j = 1
        for word in string.gmatch(str, "[^%s]+") do
            if(j == 1) then
                a[i] = word
                j = j+1
            else
                n = tonumber(word)
                b[i] = n
            end
        end

    end

    -- reading total M operations to perform
    M = tonumber(io.read())
    final = {}
    add = {}
    y = {}
    p = 1
    r = 0
    -- write your code here
    for i = 1,M do
        str1 = io.read()
        item = {}
        j = 1
        for word in string.gmatch(str1,"[^%s]+") do
            item[j] = word
            j = j+1 
        end
        num = tonumber(item[3])
        condition = false
        z = 1
        for x=1,N do
            if(item[2] == a[x]) then
                condition = true
                y[p] = z
                p=p+1
                break
            end
            y[p] = z
            z = z+1

        end
        if(condition == true) then
            if(item[1] == "ADD") then
                r = r+1
                add[r] = b[z] + num
                final[i] = string.format("UPDATED Item %s",item[2])
              
            else
                if(b[z] > num) or (b[z] == num) then
                    r = r+1
                    add[r] = b[z] - num
                    final[i] = string.format("DELETED Item %s",item[2])
                else
                    r = r+1
                    add[r] = b[z]
                    final[i] = string.format("Item %s could not be DELETED",item[2])
                end
            end
            
        else
            if(item[1] == "ADD")then
                if(num>0) then
                    r = r+1
                    add[r] = num
                    final[i] = string.format("ADDED Item %s",item[2])
                else
                    final[i] = ""
                end
            else
                final[i] = string.format("Item %s does not exist",item[2])
            end

        end

    end
    -- calculate the sum of items
    sum = 0
    q=0
    --print(r)
    for i=1,r do
        --print(add[i])
        sum = sum + add[i]
    end
    for i=1,N do
        for j=1,p do
            if(i == y[j])then
                q=q+1
            end
        end
        if(q == 0) then
            sum = sum + b[i]
        end
        q = 0
    end
 
    -- write your code here    
    return final,sum,M
end
 
-- for each case, call the manageInventory function to add, update / delete items to / from the Inventory
tc = tonumber(io.read())
i = 1
final1 = {}
sum1 = {}
M1 = {}
for i=1,tc do
    final1[i],sum1[i],M1[i] = manageInventory()
end

for i=1,tc-1 do
    for j=1,M1[i] do
        if(final1[i][j] == "") then
            io.write("")
        else
            print(final1[i][j])
        end
    end
    print(sum1[i])
end
for k=1,M1[tc] do
    if(final1[tc][k] == "") then
        io.write("")
    else
        print(final1[tc][k])
    end
end
io.write(sum1[tc])
