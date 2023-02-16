#!/usr/bin/env python3

import os
import re
import getopt, sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def wireguard():
    # Create a directory to store all the graphs
    wg_dir = "graphs/wireguard"
    os.makedirs(wg_dir, exist_ok=True)
    
    # Open the log file
    with open("wireguard_results/metrics_data.log", "r") as f:
        content = f.read()

    # Find all decimal values using regular expression
    decimal_values = re.findall(r"-?\d+\.\d+", content)

    # Convert the values to float
    decimal_values = [float(x) for x in decimal_values]

    resp_times_wg = [num * 1000 for num in decimal_values]

    resp_times_wg = [round(num, 3) for num in resp_times_wg]
    
    # Convert the lists into DataFrames
    df = pd.DataFrame({"Time": resp_times_wg})

    def raw_graph():
        # Generate a Seaborn line plot
        plt.figure(figsize=(14,4))
        
        ax = sns.lineplot(data=df, linewidth = 0.90)
        
        # Set labels for x and y axis
        ax.set(xlabel="Requests count", ylabel="Response times(ms)")
        
        # Save the plot to a file
        plt.savefig("graphs/wireguard/wireguard_raw.jpg")

    def histogram_graph():
        plt.figure(figsize=(9,4))
        
        # plot the logarithmic values using a distplot
        # sns.distplot(log_data, color="hotpink", bins=25, hist_kws={'rwidth': 0.8})
        ax = sns.distplot(x=np.log10(resp_times_wg), color="hotpink", bins=25, hist_kws={'rwidth': 0.8})

        plt.xlim(left=-0.1)
        
        # Add labels
        plt.xlabel('Log(response times(ms))')
        plt.ylabel('F(X)')
        
        # Save the plot to a file
        plt.savefig("graphs/wireguard/wireguard_histogram.jpg")
        
    def ecdf_graph():
        # Plot the ECDF
        plt.figure(figsize=(9,4))
        
        n = len(resp_times_wg)
        x = np.sort(resp_times_wg)
        y = np.arange(1, n+1) / n
        
        sns.scatterplot(x=x, y=y, s=25, linewidth = 0.08)
        
        plt.xlim(0, 30)
        plt.ylim(0.00, 0.4)
        
        plt.ylim(bottom=-0.01)
        
        # Add labels
        plt.xlabel('Response times(ms)')
        plt.ylabel('F(X)')

        # Save the plot to a file
        plt.savefig("graphs/wireguard/wireguard_ecdf.jpg")

    return raw_graph(), histogram_graph(), ecdf_graph()
 
def openvpn():
    # Create a directory to store all the graphs
    ovpn_dir = "graphs/ovpn"
    os.makedirs(ovpn_dir, exist_ok=True)
    
    # Open the log file
    with open("ovpn_results/metrics_data.log", "r") as f:
        content = f.read()

    # Find all decimal values using regular expression
    decimal_values = re.findall(r"-?\d+\.\d+", content)

    # Convert the values to float
    decimal_values = [float(x) for x in decimal_values]

    resp_times_ovpn = [num * 1000 for num in decimal_values]

    resp_times_ovpn = [round(num, 3) for num in resp_times_ovpn]
    
    # Convert the lists into DataFrames
    df = pd.DataFrame({"Time": resp_times_ovpn})
    
    def raw_graph():
        # Generate a Seaborn line plot
        plt.figure(figsize=(14,4))
        ax = sns.lineplot(data=df, linewidth = 0.90)
        
        # Set labels for x and y axis
        ax.set(xlabel="Requests count", ylabel="Response times(ms)")
        
        plt.ylim(bottom=0)
        
        # Save the plot to a file
        plt.savefig("graphs/ovpn/openvpn_raw.jpg")

    def histogram_graph():
        plt.figure(figsize=(9,4))
        
        # plot the logarithmic values using a distplot
        # sns.distplot(log_data, color="hotpink", bins=25, hist_kws={'rwidth': 0.8})
        ax = sns.distplot(x=np.log10(resp_times_ovpn), color="hotpink", bins=25, hist_kws={'rwidth': 0.8})

        plt.xlim(left=-0.1)
        
        # Add labels
        plt.xlabel('Log(response times(ms))')
        plt.ylabel('F(X)')

        # Save the plot to a file
        plt.savefig("graphs/ovpn/openvpn_histogram.jpg")

    def ecdf_graph():
        # Plot the ECDF
        plt.figure(figsize=(9,4))
        
        n = len(resp_times_ovpn)
        x = np.sort(resp_times_ovpn)
        y = np.arange(1, n+1) / n
        
        sns.scatterplot(x=x, y=y, s=25, linewidth = 0.08)
        
        plt.xlim(0, 30)
        plt.ylim(0.00, 0.4)
        
        plt.ylim(bottom=-0.01)
        
        # Add labels
        plt.xlabel('Response times(ms)')
        plt.ylabel('F(X)')

        # Save the plot to a file
        plt.savefig("graphs/ovpn/openvpn_ecdf.jpg")

    return raw_graph(), histogram_graph(), ecdf_graph()
    
def softether():
    # Create a directory to store all the graphs
    softether_dir = "graphs/softether"
    os.makedirs(softether_dir, exist_ok=True)
    
    # Open the log file
    with open("softether_results/metrics_data.log", "r") as f:
        content = f.read()

    # Find all decimal values using regular expression
    decimal_values = re.findall(r"-?\d+\.\d+", content)

    # Convert the values to float
    decimal_values = [float(x) for x in decimal_values]

    resp_times_se = [num * 1000 for num in decimal_values]

    resp_times_se = [round(num, 3) for num in resp_times_se]

    # Convert the lists into DataFrames
    df = pd.DataFrame({"Time": resp_times_se})

    def raw_graph():
        # Generate a Seaborn line plot
        plt.figure(figsize=(14,4))
        ax = sns.lineplot(data=df, linewidth = 0.90)
        
        # Set labels for x and y axis
        ax.set(xlabel="Requests count", ylabel="Response times(ms)")
        
        plt.ylim(bottom=0)
        
        # Save the plot to a file
        plt.savefig("graphs/softether/softether_raw.jpg")

    def histogram_graph():
        # Plot histogram
        plt.figure(figsize=(9,4))
        
        # plot the logarithmic values using a distplot
        # sns.distplot(log_data, color="hotpink", bins=25, hist_kws={'rwidth': 0.8})
        ax = sns.distplot(x=np.log10(resp_times_se), color="hotpink", bins=25, hist_kws={'rwidth': 0.8})

        plt.xlim(left=-0.1)

        # Add labels
        plt.xlabel('Log(response times(ms))')
        plt.ylabel('F(X)')

        # Save the plot to a file
        plt.savefig("graphs/softether/softether_histogram.jpg")

    def ecdf_graph():
        # Plot the ECDF
        plt.figure(figsize=(9,4))
        
        n = len(resp_times_se)
        x = np.sort(resp_times_se)
        y = np.arange(1, n+1) / n
        
        sns.scatterplot(x=x, y=y, s=25, linewidth = 0.08)
        
        plt.xlim(0, 30)
        plt.ylim(0.00, 0.4)
        
        plt.ylim(bottom=-0.01)
        
        # Add labels
        plt.xlabel('Response times(ms)')
        plt.ylabel('F(X)')

        # Save the plot to a file
        plt.savefig("graphs/softether/softether_ecdf.jpg")

    return raw_graph(), histogram_graph(), ecdf_graph()

def tinc():
    # Create a directory to store all the graphs
    tinc_dir = "graphs/tinc"
    os.makedirs(tinc_dir, exist_ok=True)
    
    # Open the log file
    with open("tinc_results/metrics_data.log", "r") as f:
        content = f.read()

    # Find all decimal values using regular expression
    decimal_values = re.findall(r"-?\d+\.\d+", content)

    # Convert the values to float
    decimal_values = [float(x) for x in decimal_values]

    resp_times_tinc = [num * 1000 for num in decimal_values]

    resp_times_tinc = [round(num, 3) for num in resp_times_tinc]

    # Convert the lists into DataFrames
    df = pd.DataFrame({"Time": resp_times_tinc})

    def raw_graph():
        # Generate a Seaborn line plot
        plt.figure(figsize=(14,4))
        ax = sns.lineplot(data=df, linewidth = 0.90)
        
        # Set labels for x and y axis
        ax.set(xlabel="Requests count", ylabel="Response times(ms)")
        
        plt.ylim(bottom=0)
        
        # Save the plot to a file
        plt.savefig("graphs/tinc/tinc_raw.jpg")

    def histogram_graph():
        # Plot histogram
        plt.figure(figsize=(9,4))
        
        # plot the logarithmic values using a distplot
        # sns.distplot(log_data, color="hotpink", bins=25, hist_kws={'rwidth': 0.8})
        ax = sns.distplot(x=np.log10(resp_times_tinc), color="hotpink", bins=25, hist_kws={'rwidth': 0.8})

        plt.xlim(left=-0.1)
        
        # Add labels
        plt.xlabel('Log(response times(ms))')
        plt.ylabel('F(X)')

        # Save the plot to a file
        plt.savefig("graphs/tinc/tinc_histogram.jpg")

    def ecdf_graph():
        # Plot the ECDF
        plt.figure(figsize=(9,4))
        
        n = len(resp_times_tinc)
        x = np.sort(resp_times_tinc)
        y = np.arange(1, n+1) / n
        
        sns.scatterplot(x=x, y=y, s=25, linewidth = 0.08)
        
        plt.xlim(0, 30)
        plt.ylim(0.00, 0.4)
        
        plt.ylim(bottom=-0.01)
        
        # Add labels
        plt.xlabel('Response times(ms)')
        plt.ylabel('F(X)')

        # Save the plot to a file
        plt.savefig("graphs/tinc/tinc_ecdf.jpg")

    return raw_graph(), histogram_graph(), ecdf_graph()
    
def zerotier():
    # Create a directory to store all the graphs
    zerotier_dir = "graphs/zerotier"
    os.makedirs(zerotier_dir, exist_ok=True)
    
    # Open the log file
    with open("zerotier_results/metrics_data.log", "r") as f:
        content = f.read()

    # Find all decimal values using regular expression
    decimal_values = re.findall(r"-?\d+\.\d+", content)

    # Convert the values to float
    decimal_values = [float(x) for x in decimal_values]

    resp_times_zt = [num * 1000 for num in decimal_values]

    resp_times_zt = [round(num, 3) for num in resp_times_zt]

    # Convert the lists into DataFrames
    df = pd.DataFrame({"Time": resp_times_zt})

    def raw_graph():
        # Generate a Seaborn line plot
        plt.figure(figsize=(14,4))
        ax = sns.lineplot(data=df, linewidth = 0.90)
        
        # Set labels for x and y axis
        ax.set(xlabel="Requests count", ylabel="Response times(ms)")
        
        plt.ylim(bottom=0)
        
        # Save the plot to a file
        plt.savefig("graphs/zerotier/zerotier_raw.jpg")

    def histogram_graph():
        # Plot histogram
        plt.figure(figsize=(9,4))
        
        # plot the logarithmic values using a distplot
        # sns.distplot(log_data, color="hotpink", bins=25, hist_kws={'rwidth': 0.8})
        ax = sns.distplot(x=np.log10(resp_times_zt), color="hotpink", bins=25, hist_kws={'rwidth': 0.8})

        plt.xlim(left=-0.1)
        
        # Add labels
        plt.xlabel('Log(response times(ms))')
        plt.ylabel('F(X)')

        # Save the plot to a file
        plt.savefig("graphs/zerotier/zerotier_histogram.jpg")
    def ecdf_graph():
        # Plot the ECDF
        plt.figure(figsize=(9,4))
        
        n = len(resp_times_zt)
        x = np.sort(resp_times_zt)
        y = np.arange(1, n+1) / n
        
        sns.scatterplot(x=x, y=y, s=25, linewidth = 0.08)
        
        plt.xlim(0, 30)
        plt.ylim(0.00, 0.4)
        
        plt.ylim(bottom=-0.01)
        
        # Add labels
        plt.xlabel('Response times(ms)')
        plt.ylabel('F(X)')

        # Save the plot to a file
        plt.savefig("graphs/zerotier/zerotier_ecdf.jpg")

    return raw_graph(), histogram_graph(), ecdf_graph()

def ecdfs_comparision_graph():
    fig, ax = plt.subplots()
    
    labels = ['Wireguard', 'OpenVPN', 'ZeroTier', 'Tinc', 'SoftEther']
    colors = ['green', 'red', 'black', 'purple', 'orange']
    file_paths = ["wireguard_results/metrics_data.log", "ovpn_results/metrics_data.log",
                  "zerotier_results/metrics_data.log", "tinc_results/metrics_data.log", 
                  "softether_results/metrics_data.log"]
    
    for i, file_path in enumerate(file_paths):
        with open(file_path, "r") as f:
            content = f.read()

        decimal_values = [float(x) for x in re.findall(r"-?\d+\.\d+", content)]
        resp_times = [round(num * 1000, 3) for num in decimal_values]
        n = len(resp_times)
        x = np.sort(resp_times)
        y = np.arange(1, n + 1) / n
        ax.plot(x, y, marker='.', linestyle='none', markersize=5, color=colors[i], label=labels[i])

    plt.xlim(0, 30)
    plt.ylim(-0.05, 0.4)
    ax.legend()
    
    # Save the plot to a file
    plt.savefig("graphs/combined_ecdf.jpg")
    
def box_plot():
    fig, ax = plt.subplots(1, 5, sharex=True, figsize=(15, 5))

    file_names = ["wireguard_results/metrics_data.log", "ovpn_results/metrics_data.log",
                  "zerotier_results/metrics_data.log", "tinc_results/metrics_data.log",
                  "softether_results/metrics_data.log"]
    
    labels = ['Wireguard', 'OpenVPN', 'ZeroTier', 'Tinc', 'Softether']

    colors = ['green', 'orange', 'black', 'purple', 'red']

    for i in range(len(file_names)):
        # Open the file
        with open(file_names[i], "r") as f:
            content = f.read()

        # Find all decimal values using regular expression
        decimal_values = re.findall(r"-?\d+\.\d+", content)

        # Convert the values to float
        decimal_values = [float(x) for x in decimal_values]

        resp_times = [num * 1000 for num in decimal_values]
        resp_times = [round(num, 3) for num in resp_times]

        bp = ax[i].boxplot(resp_times, vert=True, showfliers=True)

        for element in ['boxes', 'whiskers', 'caps']:
            plt.setp(bp[element], color=colors[i])

        median = bp['medians'][0].get_ydata()[0]

        ax[i].annotate(f"Median: {median:.2f}", xy=(1, median), xycoords='data',
                    xytext=(-31, 5), textcoords='offset points')

        first_quartile = bp['caps'][0].get_ydata()[0]
        third_quartile = bp['caps'][1].get_ydata()[0]

        ax[i].annotate(f"1st Quartile: {first_quartile:.2f}", xy=(1, first_quartile), xycoords='data',
                    xytext=(-35, 10), textcoords='offset points')

        ax[i].annotate(f"3rd Quartile: {third_quartile:.2f}", xy=(1, third_quartile), xycoords='data',
                    xytext=(-35, -30), textcoords='offset points')

        ax[i].set_title(labels[i], color=colors[i])

    # Save the plot to a file
    plt.savefig("graphs/boxplots.jpg")

def main():
    argumentList = sys.argv[1:]
    options = "wostzeb"
    long_options = ["wireguard", "openvpn", "softether", "tinc", "zerotier", "ecdf", "box"] 
    try:
        arguments, values = getopt.getopt(argumentList, options, long_options)

        for currentArgument, cureentValue in arguments:
    
            if currentArgument in ("-w", "--wireguard"):
                print ("Loading Wireguard Graph")
                wireguard()
                
            elif currentArgument in ("-o", "--openvpn"):
                print ("Loading openvpn Graph")
                openvpn()

            elif currentArgument in ("-s", "--softether"):
                print ("Loading softether Graph")
                softether()
                
            elif currentArgument in ("-t", "--tinc"):
                print ("Loading tinc graph")
                tinc()
            elif currentArgument in ("-z", "--zerotier"):
                print ("Loading zerotier Graph")
                zerotier()
            elif currentArgument in ("-e", "--ecdf"):
                print ("Loading combined ecdf's Graph")
                ecdfs_comparision_graph()
            elif currentArgument in ("-b", "--box"):
                print ("Loading box plots Graph")
                box_plot()
         
    except getopt.error as err:
        print (str(err))

if __name__ == "__main__":
    main()