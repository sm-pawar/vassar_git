from dtaidistance import clustering
import matplotlib.pyplot as plt
from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
import pandas as pd
import numpy as np
s1 = np.array([3677.077436,3759.784327,3842.491217,3925.198107,4195.46842,4465.738733,4907.905428,5444.452714,5981,5155.461475,4329.922951,3973.955121,3617.98729,3262.01946,3530.50973,3799,4191.282034,4583.564069,5138.782034,5694,5956.516544,6219.033088,6271.514336,6323.995584,6394.874713,6465.753842,6370,6005.464522,5640.929044,5554.246823,5467.564602,5680.904219,5894.243835,6107.583452,6524,6378.83547,6233.67094,6125.11396,6016.55698,5908,5789.954593,5671.909185,5767.835686,5863.762187,6305,6297.114689,6289.229378,6284.462811,6279.696244,6274.929676,6331.964838,6389,5983.623005,6191.069556,6398.516107,6605.962659,7838,7750.601413,7663.202826,7575.80424,7527.40212,7479,7587.622923,7621.08546,7654.547997,7688.010535,8125,8202.46757,8279.935141,8331.623427,8383.311714,8435,8600.152512,8765.305023,8755,8477.287719,8199.575438,7921.863157,7754.431579,7587,7628.2,7669.4,7728.081433,7786.762865,7871.881433,7957,7959,7927.799695,7896.59939,7995.732927,8094.866463,8194,8212,7873.159274,7534.318547,7352.24096,7170.163372,6988.085785,6815.042893,6642,6264.77933,6206.889665,6149,6196.946658,6244.893315,6292.839973,6557.647123,6822.454273,7288.829194,7755.204115,8143.102057,8531,8344.386888,8039.78986,7735.192831,7475.832911,7216.472992,7279.075207,7341.677421,7404.279636,7998,7966.476029,7934.952057,7944.272322,7953.592588,7962.912853,8192,8114.763277,8037.526554,7889.139816,7740.753077,7732.705476,7724.657875,7716.610274,7768.305137,7820,7691.670006,7563.340012,7491,7488.58133,7486.16266,7483.74399,7637.390932,7815.195466,7993,8053.310688,8113.621375,8173.932063,8300.727177,8427.522292,8660.630911,8893.739529,9066,8783.237379,8500.474758,8347.061342,8193.647926,8040.23451,7946,7919.976862,7893.953723,7951.546114,8009.138505,8106.552989,8203.967472,8301.381956,8295.190978,8289,7262.666667,6495.877151,5729.087635,5186.140498,4643.193362,4593.080811,4542.968261,4492.85571,4774,4728.000754,4682.001509,4631.500754,4581,4511.666667,4442.333333,4424.099058,4405.864782,4500.866574,4595.868366,4690.870158,4884.439365,5078.008572,5199.68254,5321.356507,5196,4975.699615,4755.39923,4535.098846,4247.378657,4337.585771,4427.792886,4518,4837.853076,4902.568717,4967.284359,5032,5107.419081,5080.568931,5053.718781,4937.359696,4821.000611,4704.641525,4588.28244])
s2 = np.array([4894.335122,4837.167561,4780,4956.113892,5132.227785,5277.558928,5422.89007,5568.221213,5758.610607,5949,5075.980705,4457.645747,3839.31079,3749.170341,3659.029892,3568.889443,3942.944721,4317,4713.947487,5110.894975,5428.897221,5746.899468,6182.086082,6168.057388,6154.028694,6140,5448.229157,5120.771378,4793.313598,4757.732561,4722.151524,4856.934349,4991.717175,5126.5,5313.505238,5500.510476,5687.092689,5644.546344,5602,5448.813407,5295.626814,5353.467501,5411.308188,5469.148876,6055,6151.992742,6248.985484,6276.995787,6305.00609,6333.016393,6334.508197,6336,6062.034824,6337.728204,6613.421585,6889.114965,8241,8202.672118,8164.344236,8126.016354,7719.317757,7668.723328,7618.1289,7641.68604,7665.243181,7766.621591,7868,7927.499813,7986.999626,8046.499439,8120.103701,8193.707963,8280.501551,8367.295139,8234,8020.794071,7807.588143,7594.382214,7407.191107,7220,7084.6,7030.96653,6977.333061,6980.75828,6984.183499,6987.608719,7054,7082.452308,7110.904616,7244.16164,7377.418664,7510.675689,7815,7531.643565,7248.287129,6853.719353,6459.151578,6242.292999,6025.43442,6025.348674,6025.262928,6025.177182,6027,5723.48877,5419.97754,5320.428063,5220.878586,5618.068055,6015.257525,6412.446994,7225.723497,8039,8151.043738,7915.802598,7680.561457,7590.46639,7500.371322,7543.569212,7586.767102,7629.964992,7687,7564.950973,7442.901945,7500.112165,7557.322385,7614.532604,8077,8078.309594,8079.619189,8080.928783,8005,7975.989753,7946.979507,7917.96926,7906.627549,7895.285837,7818,7631.553302,7445.106605,7350.379894,7255.653182,7160.926471,7269.400482,7384.155877,7498.911272,7613.666667,7724.578888,7835.49111,7923.670873,8011.850635,8109.210822,8206.571008,8290,8228.321063,8166.642127,8117.854042,8069.065958,8020.277873,7862,7743.326116,7624.652232,7600.107748,7575.563264,7654.922398,7734.281532,7813.640666,7815.820333,7818,6845.09333,6107.105441,5369.117551,4817.122751,4265.127951,4158.47882,4051.829688,3945.180556,4097,4125.652093,4154.304186,4182.956279,4201,4235.25222,4269.504439,4325.336293,4381.168146,4437,4529.074053,4621.148106,4787.289845,4953.431585,5185,5076.75749,4968.514979,4781.25749,4594,4359.062397,4124.124795,4132.9242,4141.723605,4150.523011,4358.761505,4567,4633.735193,4646.686581,4659.63797,4643.603502,4627.569035,4611.534567,4755.250997,4819.091978,4882.932959])
##path = dtw.warping_path(s1, s2)
##dtwvis.plot_warping(s1, s2, path, filename="warp.png")
##
##distance = dtw.distance(s1, s2)
##print(distance)
##
##distance, paths = dtw.warping_paths(s1, s2)
##print(distance)
##print(paths)
##
##
##best_path = dtw.best_path(paths)
##dtwvis.plot_warpingpaths(s1, s2, paths, best_path, filename = 'best_path.png')

##df  = pd.read_csv('C:/Users/shubh/Downloads/Kollonkoil_model_part1_2_3_Merge_Updated_Apr14_NDVI_med_noise_cor.csv')
##
##filter_col = [col for col in df if col.startswith('VI')]
##
##ndvi_values = df[filter_col].values
##
##
### Custom Hierarchical clustering
##model1 = clustering.Hierarchical(dtw.distance_matrix_fast, {})
###cluster_idx = model1.fit(ndvi_values)
### Keep track of full tree by using the HierarchicalTree wrapper class
##model2 = clustering.HierarchicalTree(model1)
##cluster_idx = model2.fit(ndvi_values[:20,:])
###model2.plot("hierarchy.png")
##
##
##fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 10))
##show_ts_label = lambda idx: "ts-" + str(idx)
##model2.plot("hierarchy.png", axes=ax, show_ts_label=show_ts_label,
##           show_tr_label=True, ts_label_margin=-10,
##           ts_left_margin=10, ts_sample_length=1)


from dtaidistance import alignment

value, scores, paths = alignment.needleman_wunsch(s1[:10], s2[30:40])
algn, s1a, s2a = alignment.best_alignment(paths, s1[:10], s2[30:40], gap='-')