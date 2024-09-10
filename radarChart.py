import numpy as np
import matplotlib.pyplot as plt

def radarChart(userId , testResult, eResultPersent, iResultPersent, sResultPersent, nResultPersent, tResultPersent, fResultPersent, jResultPersent, pResultPersent):
    
    try:
        # Tries to clear every other data from other users 
        # so that the chart gets clear for the new user
        plt.figure().clear()
        plt.close()
        plt.cla()
        plt.clf()
        
    except:
        None
        
    # Colors that I wanted :
    backgroudGray = "#fbf9f4"
    blue = "#2a475e"
    gray = "#b3b3b3"
    ligthGray = "#f2efe8"
    colors = ["#FF5A5F", "#FFB400", "#007A87"]

    circle = list(np.linspace(0, 2*np.pi, 8, endpoint=False)) # Makes the circle and devide it to 8 sections
    dashes = np.linspace(0, 2 * np.pi)

    H1 = np.ones(len(dashes)) * 25
    H2 = np.ones(len(dashes)) * 50
    H3 = np.ones(len(dashes)) * 75

    # Defining a closed circle ( full circle )
    closedCircle = circle.copy()
    closedCircle.append(0.0)

    attributes = ['E','S','T','J','I','N','F','P'] # Giving the chart's categories
    closedValues = [eResultPersent, sResultPersent, tResultPersent, jResultPersent, iResultPersent, nResultPersent, fResultPersent, pResultPersent, eResultPersent]

    ax = plt.subplot(polar=True)
    plt.xticks(circle, attributes)


    ax.set_facecolor(ligthGray) # Makes the background light gray
    ax.scatter(closedCircle, closedValues, s=25, c=blue, zorder=10) # Shows the dots in the lines
    ax.scatter(0, 0 , s=20, c=gray, zorder=10) # Shows the dots in the center ot the chart

    ax.set_yticks([])
    ax.set_label(0)
    plt.yticks([25, 50, 75, 100], ["25%", "50%", "75%", "100%"]) # Sets where to show what value in the chart
    plt.ylim(0, 100) # Sets the value of the chart
    
    ax.yaxis.grid(False) # Removes the y axis grid lines

    # Add custom dashed lines for radial axis (y) at 25 50
    ax.plot(dashes, H1, ls=(0, (6, 6)), c=gray)
    ax.plot(dashes, H2, ls=(0, (6, 6)), c=colors[2], alpha= 0.3)

    # refills the OUTER background of the chart
    ax.fill(dashes, H3, backgroudGray)

    ax.plot(closedCircle, closedValues, c=colors[1], linewidth=2) # Puts the data into the chart
    ax.fill(closedCircle, closedValues, c=gray ,alpha=0.4) # Fill inside of the lines

    # Writes the title of the chart
    ax.set_title(
        f"Test Result {testResult}",
        x = 0.1,
        y = 1,
        ha="center",
        fontsize=16,
        color=blue,
        weight="bold",    
    )

    # Saving the chart as an png photo
    plt.savefig(str(userId) + ".png")
    
