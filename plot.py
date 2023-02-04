#!/usr/bin/env python3

import os
import re
import getopt, sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from array import array

def wireguard():
    # Create a directory to store all the graphs
    wg_dir = "graphs/wireguard"
    os.makedirs(wg_dir, exist_ok=True)
    
    # Open the log file
    with open("wireguard_results/metrics.log", "r") as f:
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
        # divide each value with 10000
        # df["Time"] = df['Time']/10000
        ax = sns.lineplot(data=df, linewidth = 0.90)
        
        # Set labels for x and y axis
        ax.set(xlabel="Requests count", ylabel="Response times(ms)")
        
        # Save the plot to a file
        plt.savefig("graphs/wireguard/wireguard_raw.jpg")

    def histogram_graph():
        plt.figure(figsize=(9,4))

        # convert data to logarithmic values
        log_data = np.log(resp_times_wg)
        
        # plot the logarithmic values using a distplot
        sns.distplot(log_data, color="hotpink", bins=25, hist_kws={'rwidth': 0.8})
        
        # Add labels
        plt.xlabel('Log(response times(ms))')
        plt.ylabel('F(X)')
        
        # Save the plot to a file
        plt.savefig("graphs/wireguard/wireguard_histogram.jpg")
        
    def ecdf_graph():
        # Plot the ECDF
        plt.figure(figsize=(9,4))
        # sns.lineplot(data=df.sort_values(by='Time'), 
        #              x=np.arange(1, len(df)+1)/len(df), y='Time',
        #              drawstyle='steps-post', color='blue')

        n = len(resp_times_wg)
        x = np.sort(resp_times_wg)
        y = np.arange(1, n+1) / n
        plt.plot(x, y, marker='.', linestyle='none', markersize=13)
        
        plt.xlim(0, 30)
        plt.ylim(0, 0.4)
        
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
    with open("ovpn_results/metrics.log", "r") as f:
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
        
        # Save the plot to a file
        plt.savefig("graphs/ovpn/openvpn_raw.jpg")

    def histogram_graph():
        # Plot histogram
        plt.figure(figsize=(9,4))
        
        # convert data to logarithmic values
        log_data = np.log(resp_times_ovpn)
        
        # plot the logarithmic values using a distplot
        sns.distplot(log_data, color="hotpink", bins=25, hist_kws={'rwidth': 0.8})
        
        # Add labels
        plt.xlabel('Log(response times(ms))')
        plt.ylabel('F(X)')

        # Save the plot to a file
        plt.savefig("graphs/ovpn/openvpn_histogram.jpg")

    def ecdf_graph():
        # Plot the ECDF
        # sns.lineplot(data=df.sort_values(by='Time'), 
        #              x='Time', y=np.arange(1, len(df)+1)/len(df),
        #              drawstyle='steps-post', color='blue')
        plt.figure(figsize=(9,4))
        n = len(resp_times_ovpn)
        x = np.sort(resp_times_ovpn)
        y = np.arange(1, n+1) / n
        plt.plot(x, y, marker='.', linestyle='none', markersize=13)
        
        plt.xlim(0, 30)
        plt.ylim(0, 0.4)
        
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
    with open("softether_results/metrics.log", "r") as f:
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
        
        # Save the plot to a file
        plt.savefig("graphs/softether/softether_raw.jpg")

    def histogram_graph():
        # Plot histogram
        plt.figure(figsize=(9,4))
        
        # convert data to logarithmic values
        log_data = np.log(resp_times_se)
        
        # plot the logarithmic values using a distplot
        sns.distplot(log_data, color="hotpink", bins=25, hist_kws={'rwidth': 0.8})
        
        # Add labels
        plt.xlabel('Log(response times(ms))')
        plt.ylabel('F(X)')

        # Save the plot to a file
        plt.savefig("graphs/softether/softether_histogram.jpg")

    def ecdf_graph():
        # Plot the ECDF
        # sns.lineplot(data=df.sort_values(by='Time'), 
        #              x='Time', y=np.arange(1, len(df)+1)/len(df),
        #              drawstyle='steps-post', color='blue')
        plt.figure(figsize=(9,4))
        n = len(resp_times_se)
        x = np.sort(resp_times_se)
        y = np.arange(1, n+1) / n
        plt.plot(x, y, marker='.', linestyle='none', markersize=13)
        
        plt.xlim(0, 30)
        plt.ylim(0, 0.4)
        
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
    with open("tinc_results/metrics.log", "r") as f:
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
        
        # Save the plot to a file
        plt.savefig("graphs/tinc/tinc_raw.jpg")

    def histogram_graph():
        # Plot histogram
        plt.figure(figsize=(9,4))
        
        # convert data to logarithmic values
        log_data = np.log(resp_times_tinc)
        
        # plot the logarithmic values using a distplot
        sns.distplot(log_data, color="hotpink", bins=25, hist_kws={'rwidth': 0.8})
        
        # Add labels
        plt.xlabel('Log(response times(ms))')
        plt.ylabel('F(X)')

        # Save the plot to a file
        plt.savefig("graphs/tinc/tinc_histogram.jpg")

    def ecdf_graph():
        # Plot the ECDF
        # sns.lineplot(data=df.sort_values(by='Time'), 
        #              x='Time', y=np.arange(1, len(df)+1)/len(df),
        #              drawstyle='steps-post', color='blue')
        plt.figure(figsize=(9,4))
        n = len(resp_times_tinc)
        x = np.sort(resp_times_tinc)
        y = np.arange(1, n+1) / n
        plt.plot(x, y, marker='.', linestyle='none', markersize=13)
        
        plt.xlim(0, 30)
        plt.ylim(0, 0.4)
        
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
    with open("zerotier_results/metrics.log", "r") as f:
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
        
        # Save the plot to a file
        plt.savefig("graphs/zerotier/zerotier_raw.jpg")

    def histogram_graph():
        # Plot histogram
        plt.figure(figsize=(9,4))
        
        # convert data to logarithmic values
        log_data = np.log(resp_times_zt)
        
        # plot the logarithmic values using a distplot
        sns.distplot(log_data, color="hotpink", bins=25, hist_kws={'rwidth': 0.8})
        
        # Add labels
        plt.xlabel('Log(response times(ms))')
        plt.ylabel('F(X)')

        # Save the plot to a file
        plt.savefig("graphs/zerotier/zerotier_histogram.jpg")
    def ecdf_graph():
        # Plot the ECDF
        # sns.lineplot(data=df.sort_values(by='Time'), 
        #              x='Time', y=np.arange(1, len(df)+1)/len(df),
        #              drawstyle='steps-post', color='blue')
        plt.figure(figsize=(9,4))
        n = len(resp_times_zt)
        x = np.sort(resp_times_zt)
        y = np.arange(1, n+1) / n
        plt.plot(x, y, marker='.', linestyle='none', markersize=13)
        
        plt.xlim(0, 30)
        plt.ylim(0, 0.4)
        
        # Add labels
        plt.xlabel('Response times(ms)')
        plt.ylabel('F(X)')

        # Save the plot to a file
        plt.savefig("graphs/zerotier/zerotier_ecdf.jpg")

    return raw_graph(), histogram_graph(), ecdf_graph()

def main():
    argumentList = sys.argv[1:]
    options = "wostz"
    long_options = ["wireguard", "openvpn", "softether", "tinc", "zerotier"] 
    try:
        arguments, values = getopt.getopt(argumentList, options, long_options)

        for currentArgument, currentValue in arguments:
    
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
         
    except getopt.error as err:
        print (str(err))

if __name__ == "__main__":
    main()