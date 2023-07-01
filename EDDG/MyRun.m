% The original version code is provided copyrighted by Ming Yang (yangming0702@gmail.com).
% Where referred paper is:
% Ming Yang, Aimin Zhou, Changhe Li, and Xin Yao, An Efficient Recursive Differential Grouping 
% for Large-Scale Continuous Problems (ERDG), IEEE Transactions on Evolutionary Computation.
% And we embedded the Dual DG (DDG) into ERDG and proposed EDDG. 
% Notice that the decomposition by this program is not further limit the
% scale of each subcomponent.

% MyRun('LargeScaleCEC2013Benchmark', 'benchmark_func', 12, 1000)


function MyRun(varargin)
    warning off;
    global benchmarkName;
 
    benchmarkName = varargin{1};
    fName = varargin{2};
    if isdeployed
        func_num = str2num(varargin{3});
        D001 = str2num(varargin{4});
    else
        func_num = varargin{3};
        D001 = varargin{4};
    end  
    AddPath(benchmarkName);
    

    if strcmp(benchmarkName,'LargeScaleCEC2013Benchmark')==1 && ismember(func_num, [13,14])
        D = 905;
    else
        D = D001;
    end
    
    [lb, ub]=SetProbBound(benchmarkName,func_num);
    Lbound = lb * ones(1,D);
    Ubound = ub * ones(1,D);
    
    global initial_flag;
    initial_flag = 0;
    
    [groups, fEvalNum] = EDDG(fName, func_num, D, Lbound, Ubound);    
    for idx = 1 : numel(nonseps)
       
    end
 
    groupFilePath = strcat('./',benchmarkName,'/EDDG/');
    if ~exist(groupFilePath, 'dir')
        mkdir(groupFilePath);
    end
    save(strcat(groupFilePath, '/f', num2str(func_num), '.mat'), 'fEvalNum', 'groups',  '-mat');   
end
