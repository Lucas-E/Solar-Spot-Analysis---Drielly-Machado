import os
import matplotlib.pyplot as plt
import datetime

#--------------------------------------------------------------
#configuring root dir
ROOT_DIR = os.path.dirname(os.path.abspath("config.py"))
os.chdir(ROOT_DIR)
#--------------------------------------------------------------

#-----------------------------------------------------------------
def populateByDay(path):
    daily = {}
    with open(f'{path}') as f:
        for i in f:
            linha = i.rstrip().replace(' ', '').split(';')

            if(linha[0] in daily.keys()):
                if(linha[1] in daily[linha[0]].keys()):
                    daily[linha[0]][linha[1]][linha[2]] = {
                        'total':linha[4],
                        'std':linha[5],
                        'numberOfObservations':linha[6]
                    }
                else:
                    daily[linha[0]][linha[1]] = {}
                    daily[linha[0]][linha[1]][linha[2]] = {
                        'total':linha[4],
                        'std':linha[5],
                        'numberOfObservations':linha[6]
                    }
            else:
                daily[linha[0]] = {}
                daily[linha[0]][linha[1]] = {}
                daily[linha[0]][linha[1]][linha[2]] = {
                        'total':linha[4],
                        'std':linha[5],
                        'numberOfObservations':linha[6]
                    }
        
        return daily
#-----------------------------------------------------------------

#-----------------------------------------------------------------
def populateByMonth(path):
    monthly = {}
    with open(f'{path}') as f:
        for i in f:
            linha = i.rstrip().replace(' ', '').split(';')

            if(linha[0] in monthly.keys()):
                monthly[linha[0]][linha[1]] = {
                    'total': linha[3],
                    'std': linha[4],
                    'numberOfObservations':linha[5]
                }
            else:
                monthly[linha[0]] = {}
                monthly[linha[0]][linha[1]] = {
                    'total': linha[3],
                    'std': linha[4],
                    'numberOfObservations':linha[5]
                }
    return monthly
#-----------------------------------------------------------------

#-----------------------------------------------------------------
def maxMinByInterval(start, end, startMoth, endMonth, daily):
    maximum = {
        'year':0,
        'month':0,
        'day':0,
        'max':0
    }
    minimum = {
        'year':0,
        'month':0,
        'day':0,
        'minimum':999999999999
    }
    
    if(start >= 1818 and end <= 2022 and startMoth <= 12 and startMoth >= 1 and endMonth <= 12 and endMonth != 0):
        for i in range(start, end+1):
            year = daily[str(i)]
            for monthKey, monthValue in year.items():
                if((int(monthKey) == endMonth and i == end)):
                    break
                elif((int(monthKey) >= startMoth and i >= start) or (i > start)):
                    for dayKey, dayValue in monthValue.items():
                        if(int(dayValue['total']) > int(maximum['max'])):
                            maximum['year'] = str(i)
                            maximum['month'] = monthKey
                            maximum['day'] = dayKey
                            maximum['max'] = dayValue['total']
                        elif(int(dayValue['total']) < int(minimum['minimum'])):
                            minimum['year'] = str(i)
                            minimum['month'] = monthKey
                            minimum['day'] = dayKey
                            minimum['minimum'] = dayValue['total']
                        elif(endMonth == int(monthKey) and i == end):
                            break
                
        return {
            'maximum':maximum,
            'minimum':minimum
        }
    else:
        raise Exception('Error. Try using valid years and months (1818 to 2022, 1 to 12)')
#-----------------------------------------------------------------

#-----------------------------------------------------------------
def monthlyMeanByYear(monthly, year):
    means = {}
    if(str(year) in monthly.keys()):
        year = monthly[str(year)]
        for key, value in year.items():
            means[key] = value['total']
        return means
    else:
        raise Exception('Year out of range')
#-----------------------------------------------------------------


#-----------------------------------------------------------------
def maxMeanByInterval(start, end, monthly):
    if(str(start) not in monthly.keys() or str(end) not in monthly.keys()):
        raise Exception('Years out of range')
    else:
        maximum = {
            'year':0,
            'month':0,
            'max':0
        }
        for i in range(start, end+1):
            data = monthlyMeanByYear(monthly, i)
            for key, value in data.items():
                if(float(value) > maximum['max']):
                    maximum['year'] = i
                    maximum['month'] = key
                    maximum['max'] = float(value)
        return maximum

#-----------------------------------------------------------------

#-----------------------------------------------------------------
def minMeanByInterval(start, end, monthly):
    if(str(start) not in monthly.keys() or str(end) not in monthly.keys()):
        raise Exception('Years out of range')
    else:
        minimum = {
            'year':0,
            'month':0,
            'min':999999999
        }
        for i in range(start, end+1):
            data = monthlyMeanByYear(monthly, i)
            for key, value in data.items():
                if(float(value) < minimum['min']):
                    minimum['year'] = i
                    minimum['month'] = key
                    minimum['min'] = float(value)
        return minimum
#------------------------------------------------------------------

#------------------------------------------------------------------

def smoothedMeanByInterval(start, end, monthly):
    if(str(start) in monthly.keys() and str(end) in monthly.keys()):
        a = {}
    
        months = []

        means=[]

        result = {}

        years = list(monthly.keys())
        yearStart = int(years[0])
        yearEnd = int(years[len(years)-1])

        for key, value in monthly.items():
            if(int(key) >= start-1 and int(key) <= end+1):
                if(int(key) >= start and int(key) <= end):
                    result[key] = []
                for monthKey, monthValue in value.items():
                    #if(key in result.keys()):
                        #result[key][monthKey] = {
                            #'smoothedMean':0
                        #}
                    months.append(float(monthValue['total']))

        if(start > yearStart and end+1 == yearEnd):
            for i in range(12, len(months) -10):
                means.append((0.5*months[i-6] + months[i-5] + months[i-4] + months[i-3] + months[i-2] + months[i-1] + months[i] + months[i+1]+ months[i+2]+ months[i+3]+ months[i+4]+ months[i+5]+ months[i+6]*0.5)/12)
        elif(start > yearStart and end < yearEnd):
            for i in range(12, len(months) -12):
                means.append((0.5*months[i-6] + months[i-5] + months[i-4] + months[i-3] + months[i-2] + months[i-1] + months[i] + months[i+1]+ months[i+2]+ months[i+3]+ months[i+4]+ months[i+5]+ months[i+6]*0.5)/12)    
        elif(start == yearStart and end < yearEnd):
            for i in range(6, len(months) -12):
                means.append((0.5*months[i-6] + months[i-5] + months[i-4] + months[i-3] + months[i-2] + months[i-1] + months[i] + months[i+1]+ months[i+2]+ months[i+3]+ months[i+4]+ months[i+5]+ months[i+6]*0.5)/12)
        elif(start > yearStart and end == yearEnd):
            for i in range(12, len(months) -6):
                means.append((0.5*months[i-6] + months[i-5] + months[i-4] + months[i-3] + months[i-2] + months[i-1] + months[i] + months[i+1]+ months[i+2]+ months[i+3]+ months[i+4]+ months[i+5]+ months[i+6]*0.5)/12)
        else:
            for i in range(6, len(months) -6):
                means.append((0.5*months[i-6] + months[i-5] + months[i-4] + months[i-3] + months[i-2] + months[i-1] + months[i] + months[i+1]+ months[i+2]+ months[i+3]+ months[i+4]+ months[i+5]+ months[i+6]*0.5)/12)

       

        for key, value in result.items():
            if(int(key) == yearStart):
                for i in range(6, 12):
                    result[key].append(means.pop(0))
            elif(int(key) == yearEnd):
                for i in range(4):
                    result[key].append(means.pop(0))
            else:
                for i in range(12):
                    result[key].append(means.pop(0))
            #for monthKey, monthValue in value.items():
                #result[key][monthKey]['smoothedMean'] = means.pop(0)

        return result
    
    else:
        raise Exception('Years out of range')


def dataForGraph(daily, monthly, start, end):
    if(str(start) in daily.keys() and str(end) in daily.keys()):
        dayY = []
        monthY = []
        for key, value in daily.items():
            if(int(key) >= start and int(key) <= end):
                for monthKey, monthValue in value.items():
                    for dayKey, dayValue in monthValue.items():
                        dayY.append(int(dayValue['total']))



        for key, value in monthly.items():
            if(int(key) >= start and int(key) <= end):
                for monthKey, monthValue in value.items():
                    monthY.append(float(monthValue['total']))

        smoothed = smoothedMeanByInterval(start,end,monthly)
        smoothedY = []
        for key, value in smoothed.items():
            smoothedY.extend(value)

        return {
            'day':dayY,
            'month':monthY,
            'smoothed':smoothedY,
            'start':start,
            'end':end
        }
    else:
        raise Exception('Years out of range')

def createGraph(data):
    fig, ax = plt.subplots()
    
    #creating first plot
    ax.set_aspect('auto')
    line1 = ax.plot(data['day'], linewidth=.2, color="y", label="Daily Observations")
    
    #ax.set_xticklabels(range(data['start'], data['end'], 5), rotation=90)
    #ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
    ax.set_xticklabels([])
    #numTicks = math.floor((data['end'] - data['start'])/10)
    #ax.xaxis.set_major_locator(plt.MaxNLocator(numTicks))
    
    #ax.legend(loc=1)
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    
    #creating second plot
    ax2 = ax.twiny()
    line2=ax2.plot(data['month'], linewidth=.5, color="b", label="Monthly Means")
    
    ax2.set_xticklabels([])
    
    
    
    #ax2.legend(loc=2)
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    
    #creating third plot
    ax3 = ax2.twiny()
    line3=ax3.plot(data['smoothed'], linewidth=2, color="r", label="Smoothed mean")
    #period = [format(i) for i in range(data['start'], data['end'])]
    
    ax3.set_xticklabels([])
    
    ax3.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) 
    
    ax2.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)
    
    
    
    #criando legendas
    #ax3.legend(loc=2)
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    
    lins = line1+line2+line3
    labs = [l.get_label() for l in lins]
    ax.legend(lins,labs,loc=0)
    
    plt.xticks(rotation=45)

    now = datetime.datetime.now()

    saveTitle = 'plotfig-' + str(now.day) + '-' + str(now.hour) + str(now.second) + '.png'

    plt.savefig(saveTitle)

    return saveTitle