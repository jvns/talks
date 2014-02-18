import pandas as pd
crashes = pd.read_csv('./CAR-CRASHES-2007.csv', parse_dates=['DT_ACCDN'])
remappings = {
    'DT_ACCDN': 'Date',
    'HR_ACCDN': 'Time',
    'CD_ETAT_VICTM': 'Victim count',
    # 'CD_MUNCP',
    # 'CIVIC_NUMBER',
    # 'RUE_ACCN_TYPE',
    'RUE_ACCDN': 'Street',
    # 'RUE_ACCDN_DIR',
    # 'PRES_DE_TYPE',
    'ACCDN_PRES_DE': 'Cross Street',
    # 'ACCDN_PRES_DIR',
    'Address concatenation': 'Address',
    # 'Geocoding address',
    'LATITUDE': 'Latitude',
    'LONGITUDE': 'Latitude',
    'NB_MORT_C': 'Deaths',
    'NB_BLESE_GRAVE_C': 'Serious Injuries',
    'NB_BLESE_LEGER_C': 'Injuries'}
crashes = crashes[remappings.keys()].rename(columns=remappings)
crashes['Intersection'] = crashes['Street'] + ' / ' + crashes['Cross Street']
crashes.to_csv('car_crashes_2007.csv', index=False)
