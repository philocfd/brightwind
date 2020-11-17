import pytest
import brightwind as bw

DATA = bw.load_csv(bw.demo_datasets.demo_data)
DATA = bw.apply_cleaning(DATA, bw.demo_datasets.demo_cleaning_file)
WSPD_COLS = ['Spd80mN', 'Spd80mS', 'Spd60mN', 'Spd60mS', 'Spd40mN', 'Spd40mS']
WDIR_COLS = ['Dir78mS', 'Dir58mS', 'Dir38mS']


def test_plot_timeseries():
    bw.plot_timeseries(DATA[['Spd40mN', 'Spd60mS', 'T2m']])
    bw.plot_timeseries(DATA[['Spd40mN']], date_from='2017-09-01')
    bw.plot_timeseries(DATA.Spd40mN, date_from='2017-09-01')
    bw.plot_timeseries(DATA.Spd40mN, date_to='2017-10-01')
    bw.plot_timeseries(DATA.Spd40mN, date_from='2017-09-01', date_to='2017-10-01')
    bw.plot_timeseries(DATA.Spd40mN, date_from='2017-09-01', date_to='2017-10-01', y_limits=(0, None))
    bw.plot_timeseries(DATA.Spd40mN, date_from='2017-09-01', date_to='2017-10-01', y_limits=None)
    bw.plot_timeseries(DATA.Spd40mN, date_from='2017-09-01', date_to='2017-10-01', y_limits=(0, 25))
    bw.plot_timeseries(DATA.Spd40mN, date_from='2017-09-01', date_to='2017-10-01', y_limits=(None, 25))

    assert True


def test_plot_scatter():
    graph = bw.plot_scatter(DATA.Spd80mN, DATA.Spd80mS)
    graph = bw.plot_scatter(DATA.Spd80mN, DATA[['Spd80mS']])
    bw.plot_scatter(DATA.Dir78mS, DATA.Dir58mS, x_axis_title='Dir78mS', y_axis_title='Dir58mS',
                    x_limits=(50, 300), y_limits=(250, 300))
    bw.plot_scatter_wdir(DATA.Dir78mS, DATA.Dir58mS, x_axis_title='Reference', y_axis_title='Target',
                         x_limits=(50, 300), y_limits=(250, 300))
    bw.plot_scatter_wspd(DATA.Spd80mN, DATA.Spd80mS, x_axis_title='Speed at 80m North',
                         y_axis_title='Speed at 80m South', x_limits=(0, 25), y_limits=(0, 25))

    assert True
