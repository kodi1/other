#{ "hmin": 0, "vmin": 0, "hmax": 0.25, "vmax": 0.25 }

H=32
V=8

h_min = 0.0
h_step = 1.0 / H
h_max = h_step

for h in range(0, H):
  if h % 2 == 0:
    v_step = 1.0 / V
    v_max = v_step
    v_min = 0.0
    for v in range(0, V):
      print '{ "hmin": %f, "vmin": %f, "hmax": %f, "vmax": %f },' % (h_min, v_min, h_max, v_max)
      v_min += v_step
      v_max += v_step
  else:
    v_step = 1.0 / V
    v_max = 1.0
    v_min = v_max - v_step
    for v in range(0, V):
      print '{ "hmin": %f, "vmin": %f, "hmax": %f, "vmax": %f },' % (h_min, v_min, h_max, v_max)
      v_min -= v_step
      v_max -= v_step
  h_min += h_step
  h_max += h_step
