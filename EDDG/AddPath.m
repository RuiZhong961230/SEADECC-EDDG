function AddPath(probName)
    if ~isdeployed && strcmp(probName,'LargeScaleCEC2010Benchmark')
        addpath('./LargeScaleCEC2010Benchmark');
        addpath('./LargeScaleCEC2010Benchmark/datafiles');       
        rmpath('./LargeScaleCEC2013Benchmark');
        rmpath('./LargeScaleCEC2013Benchmark/datafiles');        
    end
    if ~isdeployed && strcmp(probName,'LargeScaleCEC2013Benchmark')
        addpath('./LargeScaleCEC2013Benchmark');
        addpath('./LargeScaleCEC2013Benchmark/datafiles');   
        rmpath('./LargeScaleCEC2010Benchmark');
        rmpath('./LargeScaleCEC2010Benchmark/datafiles');      
    end   
end