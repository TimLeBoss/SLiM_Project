#import matplotlib.pyplot as mp
#import numpy as np
import sys
import ast
        
piA = ast.literal_eval(sys.argv[1])
#piX = ast.literal_eval(sys.argv[2])
#piY = ast.literal_eval(sys.argv[3])
        
#meanA = np.mean(piA)
#meanX = np.mean(piX)
#meanY = np.mean(piY)
#legend = ["piA","piX","piY"]

meanA = sum(piA)/len(piA)
print("Average PI for Autosome:",meanA)
        
        
#mp.subplot(2,1,1)
#mp.boxplot([piA,piX,piY],tick_labels=legend,showmeans=True)
#mp.title('Differences of Nucleotide Diversity between Autosome Chromosomes and Sexual Chromosomes')
        
# mp.subplot(2,1,2)
# mp.pie([meanA,meanX,meanY],labels=legend)

# mp.show()