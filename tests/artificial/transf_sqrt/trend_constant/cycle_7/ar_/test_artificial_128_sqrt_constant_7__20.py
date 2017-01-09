import Bench.TS_datasets as tsds
import tests.artificial.process_artificial_dataset as art




dataset = tsds.generate_random_TS(N = 128 , FREQ = 'D', seed = 0, trendtype = "constant", cycle_length = 7, transform = "sqrt", sigma = 0.0, exog_count = 20);

art.process_dataset(dataset);