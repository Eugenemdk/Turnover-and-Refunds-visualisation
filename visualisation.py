import matplotlib.pyplot as pyplot

turnover=[1000,4000,6000,7000,15000,18000,20000,25000,35000,40000]
refunds=[150,180,350,400,750,800,850,900,950,1100]

pyplot.title("Linear plot of refund to turnover",fontsize=17,fontweight="bold",color="black")
pyplot.xlabel("Turnover",fontsize=14,color="black")
pyplot.ylabel("Refunds",fontsize=14,color="black")
pyplot.plot(turnover,refunds)
pyplot.grid()
pyplot.show()
