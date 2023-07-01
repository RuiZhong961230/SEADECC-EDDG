function [lb, ub]=SetProbBound(probName, func_num)

    if strcmp(probName,'LargeScaleCEC2010Benchmark')
        if (func_num == 1 || func_num == 4 || func_num == 7 || func_num == 8 || func_num == 9 || func_num == 12 || func_num == 13 || func_num == 14 || func_num == 17 || func_num == 18 || func_num == 19 || func_num == 20)
            lb = -100;
            ub = 100;
        end
        if (func_num == 2 || func_num == 5 || func_num == 10 || func_num == 15)
            lb = -5;
            ub = 5;
        end
        if (func_num == 3 || func_num == 6 || func_num == 11 || func_num == 16)
            lb = -32;
            ub = 32;
        end
    end
        
    if strcmp(probName,'LargeScaleCEC2013Benchmark')
        if (func_num == 1 || func_num == 4 || func_num == 7 || func_num == 8 || func_num == 11 || func_num == 12 || func_num == 13 || func_num == 14 || func_num == 15 )
            lb =  -100; 
            ub = 100; 
        end
        if (func_num == 2 || func_num == 5 || func_num == 9)
            lb =  -5; 
            ub = 5;
        end
        if (func_num == 3 || func_num == 6 || func_num == 10)
            lb =  -32;
            ub = 32;
        end
    end
end