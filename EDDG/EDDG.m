function [groups001, fEvalNum] = EDDG(fun, fun_number, dim, lb, ub)
   seps      = [];
   nongroups = {};
   FEs       = 0;
   
   p1  = lb .* ones(1,dim);
   y1  = feval(fun, p1, fun_number);
   FEs=FEs+1;
        
   sub1 = 1;
   sub2 = 2 : dim;
    
   while ~isempty(sub2)       
       p2 = p1;
       p2(sub1)=ub(sub1).*ones(1,numel(sub1));
       y2=feval(fun, p2, fun_number);
       FEs=FEs+1;
       
       y = [y1 -y2 nan nan];
       [sub1_a,FEs, ~, ~]=INTERACT(fun,fun_number,sub1,sub2,p1,p2,FEs,ub,lb,y);
        
       if numel(sub1_a)==numel(sub1) %sub1 does not interrelate with sub2
           if numel(sub1)==1
              seps=[seps;sub1];
           else
              nongroups = {nongroups{:},sub1};
           end 
           sub1 = sub2(1);
           sub2 = sub2(2:end);            
       else
           sub1=sub1_a;
           sub2=sub2(~ismember(sub2, sub1));
       end         
       if isempty(sub2)
           if numel(sub1) <= 1
                seps = [seps; sub1];
           else
               nongroups = {nongroups{:},sub1};
           end
       end
   end
    
    nonseps = nongroups;
    groups001 = cell(numel(nonseps)+numel(seps), 1);
    for sepsIndex = 1 : numel(nonseps)
        groups001(sepsIndex) = {nonseps{sepsIndex}};
    end
    for sepsIndex = numel(nonseps)+1 : numel(nonseps)+numel(seps)
       groups001(sepsIndex) = {seps(sepsIndex - numel(nonseps))};
    end
    fEvalNum = FEs;
end


function [sub1,FEs, y001, t001]= INTERACT(fun, fun_number,sub1,sub2,p1,p2,FEs,ub,lb,y)
   muM = eps / 2;
   gamma = @(n)((n.*muM)./(1-n.*muM));


   nonsepFlag = 1;
   y001 = y;
   t001 = [log(y001(1)) -log(-y001(2)) -log(-y001(3)) log(y001(4))];

   if any(isnan(y))
       p3=p1;
       p4=p2;
       p3(sub2) =(ub(sub2)+lb(sub2))/2 .* ones(1,numel(sub2));
       p4(sub2) = (ub(sub2)+lb(sub2))/2 .* ones(1,numel(sub2));
       y3=feval(fun, p3, fun_number);
       y4=feval(fun, p4, fun_number);
       FEs = FEs + 2;
       
       y001(3:4) = [-y3 y4];
       t001(3:4) = [-log(y3), log(y4)];
       
       Fmax = sum(abs(y001));
       Jmax = sum(abs(t001));
       epsilonAdd = gamma(numel(ub)^0.5+2) * Fmax;
       epsilonMulti = gamma(numel(ub)^0.5+2) * Jmax; % embedded DDG

       deltaDiff001 = abs(sum(y001));
       deltaMulti = abs(sum(t001));
       if deltaDiff001 <= epsilonAdd || deltaMulti <= epsilonMulti
           nonsepFlag = 0;
       end
   end   
   
   if nonsepFlag == 1
       if numel(sub2)==1
           sub1=union(sub1,sub2);
       else
           k=floor(numel(sub2)/2);
           sub2_1=sub2(1:k);
           sub2_2=sub2(k+1:end);  
           
           [sub1_1,FEs, y002, t002]= INTERACT(fun, fun_number,sub1,sub2_1,p1,p2,FEs,ub,lb,[y(1) y(2) nan nan]);
           deltaDiffDiff = sum(y001) - sum(y002);
           deltaDiffDiff2 = sum(t001) - sum(t002);
           if deltaDiffDiff ~= 0 && deltaDiffDiff2 ~= 0
               if numel(sub1_1) == numel(sub1) %the left child is separable
                    [sub1_2,FEs, ~, ~]=INTERACT(fun, fun_number, sub1, sub2_2, p1, p2, FEs, ub, lb, y001);
               else
                    [sub1_2,FEs, ~, ~]=INTERACT(fun, fun_number,sub1, sub2_2, p1, p2, FEs, ub, lb, [y(1) y(2) nan nan]);
               end
               sub1 = union(sub1_1,sub1_2); 
           else
               sub1 = sub1_1;      
           end
       end
   end   
end