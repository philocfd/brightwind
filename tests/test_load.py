import pytest
import brightwind as bw
import os
import pandas as pd
import numpy as np

DEMO_DATA_FOLDER = os.path.join(os.path.dirname(__file__), '../brightwind/demo_datasets')


def test_apply_cleaning_windographer():
    data = bw.load_campbell_scientific(bw.demo_datasets.demo_campbell_scientific_data)
    data_clnd = bw.apply_cleaning_windographer(data, bw.demo_datasets.demo_windographer_flagging_log)
    data_clnd2 = bw.apply_cleaning_windographer(data, bw.demo_datasets.demo_windographer_flagging_log2, dayfirst=True)

    assert (data_clnd2.fillna(-999) == data_clnd.fillna(-999)).all().all()


def test_apply_cleaning():
    data = bw.load_campbell_scientific(bw.demo_datasets.demo_campbell_scientific_data)
    data_clnd2 = bw.apply_cleaning_windographer(data, bw.demo_datasets.demo_windographer_flagging_log2, dayfirst=True)
    data_clnd3 = bw.apply_cleaning(data, bw.demo_datasets.demo_cleaning_file)
    data_clnd4 = bw.apply_cleaning(data, os.path.join(DEMO_DATA_FOLDER, 'demo_cleaning_file2.csv'), dayfirst=True)
    data_clnd5 = bw.apply_cleaning(data, os.path.join(DEMO_DATA_FOLDER, 'demo_cleaning_file3.csv'), dayfirst=True)

    cleaning_dict = {0: {'Sensor': 'All', 'Start': '2016-01-09 15:30:00', 'Stop': '2016-01-09 17:10:00',
                         'Reason': 'Installation'},
                     1: {'Sensor': 'Spd', 'Start': '2016-03-09 06:20:00', 'Stop': '2016-03-11',
                         'Reason': 'Icing'},
                     2: {'Sensor': 'Dir', 'Start': '2016-03-09 06:20:00', 'Stop': '2016-03-11',
                         'Reason': 'Icing'},
                     3: {'Sensor': 'Spd', 'Start': '2016-03-29', 'Stop': '2016-03-30 07:10:00',
                         'Reason': 'Icing'},
                     4: {'Sensor': 'Dir', 'Start': '2016-03-29 ', 'Stop': '2016-03-30 07:10:00',
                         'Reason': 'Icing'}}
    data_clnd6 = bw.apply_cleaning(data, pd.DataFrame(cleaning_dict).T)

    assert (data_clnd2.drop(['RECORD', 'Site', 'LoggerID'], axis=1).fillna(-999) ==
            data_clnd3.drop(['RECORD', 'Site', 'LoggerID'], axis=1).fillna(-999)).all().all()

    assert (data_clnd3.drop(['RECORD', 'Site', 'LoggerID'], axis=1).fillna(-999) ==
            data_clnd4.drop(['RECORD', 'Site', 'LoggerID'], axis=1).fillna(-999)).all().all()

    assert (data_clnd3.drop(['RECORD', 'Site', 'LoggerID'], axis=1).fillna(-999) ==
            data_clnd5.drop(['RECORD', 'Site', 'LoggerID'], axis=1).fillna(-999)).all().all()

    assert np.isnan(data_clnd6.Spd40mN['2016-03-09 06:20:00'])
    assert not np.isnan(data_clnd6.Spd40mN['2016-03-09 06:10:00'])
    assert np.isnan(data_clnd6.Spd40mN['2016-03-10 23:50:00'])
    assert not np.isnan(data_clnd6.Spd40mN['2016-03-11 00:00:00'])
    assert not np.isnan(data_clnd6.Spd40mN['2016-03-28 23:50'])
    assert np.isnan(data_clnd6.Spd40mN['2016-03-29 00:00'])


def test_load_csv():
    data = bw.load_csv(os.path.join(DEMO_DATA_FOLDER, 'demo_data.csv'))
    data2 = bw.load_csv(os.path.join(DEMO_DATA_FOLDER, 'demo_data2.csv'), dayfirst=True)
    data3 = bw.load_csv(os.path.join(DEMO_DATA_FOLDER, 'demo_data3.csv'), dayfirst=True)
    data4 = bw.load_csv(os.path.join(DEMO_DATA_FOLDER, 'demo_data4.csv'), dayfirst=True)

    assert (data['2016-01-09 15:30:00':'2016-01-10 23:50:00'].fillna(-999) ==
            data2['2016-01-09 15:30:00':'2016-01-10 23:50:00'].fillna(-999)).all().all()
    assert (data['2016-01-09 15:30:00':'2016-01-10 23:50:00'].fillna(-999) ==
            data3['2016-01-09 15:30:00':'2016-01-10 23:50:00'].fillna(-999)).all().all()
    assert (data['2016-01-09 15:30:00':'2016-01-10 23:50:00'].fillna(-999) ==
            data4['2016-01-09 15:30:00':'2016-01-10 23:50:00'].fillna(-999)).all().all()


def test_load_windographer_txt():
    data = bw.load_windographer_txt(os.path.join(DEMO_DATA_FOLDER, 'windographer_demo_data.txt'))
    data1 = bw.load_windographer_txt(os.path.join(DEMO_DATA_FOLDER, 'windographer_demo_data1.txt'), dayfirst=True)
    data2 = bw.load_windographer_txt(os.path.join(DEMO_DATA_FOLDER, 'windographer_demo_data2.txt'), dayfirst=True)

    assert (data['2016-01-09 15:30:00':'2016-01-10 23:50:00'].fillna(-999) ==
            data1['2016-01-09 15:30:00':'2016-01-10 23:50:00'].fillna(-999)).all().all()
    assert (data['2016-01-09 15:30:00':'2016-01-10 23:50:00'].fillna(-999) ==
            data2['2016-01-09 15:30:00':'2016-01-10 23:50:00'].fillna(-999)).all().all()


def test_load_campbell_scientific():
    data = bw.load_campbell_scientific(os.path.join(DEMO_DATA_FOLDER, 'campbell_scientific_demo_data.csv'))
    data1 = bw.load_campbell_scientific(os.path.join(DEMO_DATA_FOLDER, 'campbell_scientific_demo_data1.csv'), dayfirst=True)

    assert (data['2016-01-09 15:30:00':'2016-01-10 23:50:00'].fillna(-999) ==
            data1['2016-01-09 15:30:00':'2016-01-10 23:50:00'].fillna(-999)).all().all()


def test_load_brighthub():

    plant_uuid = '7a58497e-bee1-42a2-8084-c47a5cf213b7'
    measurement_station_uuid = '9344e576-6d5a-45f0-9750-2a7528ebfa14'
    test_period_demo_data = {'start_date': '2016-01-09T15:30:00', 'end_date': '2017-11-23T11:00:00'}

    # To get a specific plant
    assert bw.LoadBrightHub.get_plants(plant_uuid=plant_uuid)[
               'plant_type_id'].values[0] == 'onshore_wind'

    # To get a specific measurement station
    assert (bw.LoadBrightHub.get_measurement_stations(plant_uuid=plant_uuid).dropna(
        axis=1) == bw.LoadBrightHub.get_measurement_stations(measurement_station_uuid=measurement_station_uuid
                                                             ).dropna(axis=1)).all().all()

    # To get the data model for a specific measurement station
    assert bw.LoadBrightHub.get_data_model(measurement_station_uuid=measurement_station_uuid
                                           )['author'] == 'Brighthub'

    # To get start and end date of data for a specific measurement station
    assert bw.LoadBrightHub.get_start_end_dates(measurement_station_uuid=measurement_station_uuid
                                                ) == test_period_demo_data

    # To get data for a specific time period for a specific measurement station
    data_columns = bw.LoadBrightHub.get_data(measurement_station_uuid=measurement_station_uuid, date_from='2016-12-01',
                                             date_to='2017-01-01').columns
    for col in ['Spd80mN', 'Spd80mS', 'Dir78mS']:
        assert col in data_columns
