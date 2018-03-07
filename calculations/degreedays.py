def degreedays(data, threshold):
    '''Calculates degree days with specific thresholds
    
    Keyword arguments
    data - data frame with tmax and tmin in columns
    threshold - specific thresholds to integrate over'''
    
    
    retdat = data
    retdat = retdat.sort_values('date', ascending=True)
    retdat['tavg'] = (retdat.tmax + retdat.tmin)/2
    #nc = len(retdat.columns)
    

    for i in range(0, (len(threshold))):
        col = ("dday" + str(threshold[i]) + "C")

        b = threshold[i]

        retdat[col] = np.where(b <= retdat['tmin'], retdat['tavg']- b, 0)
        retdat[col]

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            temp = np.arccos((2*b - retdat['tmax']- retdat['tmin'])/(retdat['tmax'] - retdat['tmin']))

        retdat[col] = np.where((retdat.tmin < b) & (b < retdat.tmax), 
                               ((retdat.tavg -b)*temp + (retdat.tmax - retdat.tmin)*np.sin(temp)/2)/np.pi, 
                               retdat[col])
        retdat[col] = retdat[col].round(5)
    return(retdat)



