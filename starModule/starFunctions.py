import os

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