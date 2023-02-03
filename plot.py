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
    with open("wireguard_results/metrics.log", "r") as f:
        content = f.read()

    # Find all decimal values using regular expression
    decimal_values = re.findall(r"-?\d+\.\d+", content)

    # Convert the values to float
    decimal_values = [float(x) for x in decimal_values]

    resp_times = [num * 1000 for num in decimal_values]

    resp_times = [round(num, 3) for num in resp_times]
    
    # Convert the lists into DataFrames
    df = pd.DataFrame({"Time": resp_times})

    def raw_graph():
        # Generate a Seaborn line plot
        plt.figure(figsize=(14,4))
        ax = sns.lineplot(data=df, linewidth = 0.90)
        
        # Set labels for x and y axis
        ax.set(xlabel="Requests count", ylabel="Response times(ms)")
        
        # Save the plot to a file
        plt.savefig("graphs/wireguard/wireguard_raw.jpg")

    def histogram_graph():
        # Plot histogram
        plt.figure(figsize=(9,4))
        
        sns.histplot(data=df, x="Time", kde=True, color="blue", edgecolor="black", alpha=0.5, bins=30)
        
        # Add labels
        plt.xlabel('Response times(ms)')
        plt.ylabel('Requests count')
        
        # Save the plot to a file
        plt.savefig("graphs/wireguard/wireguard_histogram.jpg")
        
    def ecdf_graph():
        # Plot the ECDF
        # sns.lineplot(data=df.sort_values(by='Time'), 
        #              x='Time', y=np.arange(1, len(df)+1)/len(df),
        #              drawstyle='steps-post', color='blue')
        plt.figure(figsize=(9,4))
        sns.scatterplot(data=df.sort_values(by='Time'), 
                     x='Time', y=np.arange(1, len(df)+1)/len(df),
                     marker='.', s=220, linewidth=10000)
        
        plt.xlim(0, 9.33)
        plt.ylim(0, 0.35)
        
        # Add labels
        plt.xlabel('Log(response times(ms))')
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

    resp_times = [num * 1000 for num in decimal_values]

    resp_times = [round(num, 3) for num in resp_times]
    
    # Convert the lists into DataFrames
    df = pd.DataFrame({"Time": resp_times})
    
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
        
        sns.histplot(data=df, x="Time", kde=True, color="blue", edgecolor="black", alpha=0.5, bins=30)
        
        # Add labels
        plt.xlabel('Response times(ms)')
        plt.ylabel('Requests count')

        # Save the plot to a file
        plt.savefig("graphs/ovpn/openvpn_histogram.jpg")

    def ecdf_graph():
        # Plot the ECDF
        # sns.lineplot(data=df.sort_values(by='Time'), 
        #              x='Time', y=np.arange(1, len(df)+1)/len(df),
        #              drawstyle='steps-post', color='blue')
        plt.figure(figsize=(9,4))
        sns.scatterplot(data=df.sort_values(by='Time'), 
                     x='Time', y=np.arange(1, len(df)+1)/len(df),
                     marker='.', s=220, linewidth=10000)
        
        plt.xlim(0, 9.33)
        plt.ylim(0, 0.35)
        
        # Add labels
        plt.xlabel('Log(response times(ms))')
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

    resp_times = [num * 1000 for num in decimal_values]

    resp_times = [round(num, 3) for num in resp_times]

    # Convert the lists into DataFrames
    df = pd.DataFrame({"Time": resp_times})

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
        
        sns.histplot(data=df, x="Time", kde=True, color="blue", edgecolor="black", alpha=0.5, bins=30)
        
        # Add labels
        plt.xlabel('Response times(ms)')
        plt.ylabel('Requests count')

        # Save the plot to a file
        plt.savefig("graphs/softether/softether_histogram.jpg")

    def ecdf_graph():
        # Plot the ECDF
        # sns.lineplot(data=df.sort_values(by='Time'), 
        #              x='Time', y=np.arange(1, len(df)+1)/len(df),
        #              drawstyle='steps-post', color='blue')
        plt.figure(figsize=(9,4))
        sns.scatterplot(data=df.sort_values(by='Time'), 
                     x='Time', y=np.arange(1, len(df)+1)/len(df),
                     marker='.', s=220, linewidth=10000)
        
        plt.xlim(0, 9.8)
        plt.ylim(0, 0.35)
        
        # Add labels
        plt.xlabel('Log(response times(ms))')
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

    resp_times = [num * 1000 for num in decimal_values]

    resp_times = [round(num, 3) for num in resp_times]

    # Convert the lists into DataFrames
    df = pd.DataFrame({"Time": resp_times})

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
        
        sns.histplot(data=df, x="Time", kde=True, color="blue", edgecolor="black", alpha=0.5, bins=30)
        
        # Add labels
        plt.xlabel('Response times(ms)')
        plt.ylabel('Requests count')

        # Save the plot to a file
        plt.savefig("graphs/tinc/tinc_histogram.jpg")

    def ecdf_graph():
        # Plot the ECDF
        # sns.lineplot(data=df.sort_values(by='Time'), 
        #              x='Time', y=np.arange(1, len(df)+1)/len(df),
        #              drawstyle='steps-post', color='blue')
        plt.figure(figsize=(9,4))
        sns.scatterplot(data=df.sort_values(by='Time'), 
                     x='Time', y=np.arange(1, len(df)+1)/len(df),
                     marker='.', s=220, linewidth=10000)
        
        plt.xlim(0, 9.33)
        plt.ylim(0, 0.35)
        
        # Add labels
        plt.xlabel('Log(response times(ms))')
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

    resp_times = [num * 1000 for num in decimal_values]

    resp_times = [round(num, 3) for num in resp_times]

    # Convert the lists into DataFrames
    df = pd.DataFrame({"Time": resp_times})

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
        
        sns.histplot(data=df, x="Time", kde=True, color="blue", edgecolor="black", alpha=0.5, bins=30)
        
        # Add labels
        plt.xlabel('Response times(ms)')
        plt.ylabel('Requests count')

        # Save the plot to a file
        plt.savefig("graphs/zerotier/zerotier_histogram.jpg")
    def ecdf_graph():
        # Plot the ECDF
        # sns.lineplot(data=df.sort_values(by='Time'), 
        #              x='Time', y=np.arange(1, len(df)+1)/len(df),
        #              drawstyle='steps-post', color='blue')
        plt.figure(figsize=(9,4))
        sns.scatterplot(data=df.sort_values(by='Time'), 
                     x='Time', y=np.arange(1, len(df)+1)/len(df),
                     marker='.', s=220, linewidth=10000)
        
        plt.xlim(0, 9.33)
        plt.ylim(0, 0.35)
        
        # Add labels
        plt.xlabel('Log(response times(ms))')
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