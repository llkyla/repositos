sample_time = 0.01
time_end = 30
model.reset()

t_data = np.arange(0, time_end, sample_time)
x_data = np.zeros_like(t_data)
y_data = np.zeros_like(t_data)
v_data = np.zeros_like(t_data)
w_data = np.zeros_like(t_data)


r = 8                     # radius of each circle
L = model.L               # wheelbase = 2m
delta_target = np.arctan(L / r)   # ~0.245 rad steering angle for r=8
w_max = model.w_max        # 1.22 rad/s

v_speed = 2 * np.pi * r / 15   # circumference / 15s per loop  ≈ 3.351 m/s
v_data[:] = v_speed

N = t_data.shape[0]
half = N // 2  # switch point at t=15s

# --- First circle: turn steering angle to -delta_target (steer left, go CCW)
ramp1_steps = int(np.ceil(delta_target / w_max / sample_time))
w_data[0:ramp1_steps] = -w_max
w_data[ramp1_steps:half] = 0

# --- Second circle: reverse steering to +delta_target (steer right, go CW)
ramp2_steps = int(np.ceil((2 * delta_target) / w_max / sample_time))
w_data[half:half + ramp2_steps] = w_max
w_data[half + ramp2_steps:] = 0


for i in range(t_data.shape[0]):
    x_data[i] = model.xc
    y_data[i] = model.yc
    model.step(v_data[i], w_data[i])

plt.axis('equal')
plt.plot(x_data, y_data)
plt.show()