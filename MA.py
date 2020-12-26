import matplotlib.pyplot as plt

statData ="ex4.csv"

def getNAvg(file,N):
    """
    file - File containting all the raw weather station data
    N - The number of days to compute the moving average over
    
    Return a list of containg the moving average of all data points
    """
    
    mean = [0]
    lastN = [0]
    row = 0
    
    with open(statData,"r") as rawData:
        for line in rawData:
            if (row == 0): # Ignore the headers
                row = row + 1
                continue

            rowFullData = line
            rowData = float(line.split(",")[1])

            if (row<=N): 
                lastN.append(rowData)
                mean[0] = float(sum(lastN)/len(lastN))
            else:
                lastN = lastN[1:]
                lastN.append(rowData)
                calMA = float(sum(lastN)/N)
                mean.append(calMA)
            row = row +1
    return mean
                    
def plotData(mean,N):
        """ 
        mean - series to plot
        N - parameter for legend
        Plots running averages 
        
        """
        mean = [round(x,3) for x in mean]
        plt.plot(mean,label=str(N) + ' day average')
        plt.xlabel('Day')
        plt.ylabel('Precipiation')
        plt.legend()
       

        
plotData(getNAvg(statData,1),1)
plotData ([0 for x in range(1,5)]+ getNAvg(statData,5),5 )
plotData([0 for x in range(1,7)] + getNAvg(statData,7),7)
