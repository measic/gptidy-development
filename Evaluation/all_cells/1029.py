plt.figure(num=None, figsize=(18, 9))
plt.style.use('ggplot')
processors = [float(i) for i in results.keys()]
times = [float(i) for i in results.values()]
plt.bar(processors, times, align='center', alpha=0.3, color = 'black')
plt.title('Efficiency Graph of Multiprocessing for MonteCarlo')
plt.xlabel('Number of Processors')
plt.ylabel('Time (in seconds) to compute 1e7 simulations');