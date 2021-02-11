from matplotlib import pyplot as plt

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

#primer subplot
plt.subplot(1,2,1)
plt.plot(months,temperature,)

ax = plt.subplot(1,2,1)
ax.set_xticks(months)
ax.set_xticklabels(month_names)
#ax.set_yticks([0.10, 0.25, 0.5, 0.75])
#ax.set_yticklabels(['10%', '25%', '50%', '75%'])

#segundo subplot
plt.subplot(1,2,2)
plt.plot(temperature,flights_to_hawaii,"o")
plt.subplots_adjust(wspace=0.35)

#mostrar los 2
plt.show()