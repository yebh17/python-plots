# Python graphs plotter

Plots graphs for the above wireguard, openvpn, softether, tinc, zerotier vpn's respåonse times data

Usage: `./plot.py -[<option>]`

Options:
-    w/wireguard - Wireguard plots
-    o/openvpn - Openvpn plots
-    s/softether - Softether plots
-    t/tinc - Tinc plots
-    z/zerotier - Zerotier plots
-    e/ecdf - Combined ecdf plots
-    b/box - Box plots

Flowchart:

```
┌────────────────────────────────────┐
│      Read Data from Five Files     │
└────────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────────┐
│ Calculate Total, Maximum, Minimum, Average, │
│ and Standard Deviation Values and print them│                                           │         
└─────────────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────┐
│       Plot Raw Graphs             │
│  (requests count vs response time)│
└───────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────┐
│      Plot Histogram Graphs            │
│(logarithmic response time vs requests)│
└───────────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────┐
│     Plot Empirical Cumulative Distribution   │
│ Function (ECDF) Graphs (sorted response time │
│ vs cumulative values of requests)            │
└──────────────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────────┐
│    Plot Box Plots for Data from All Five Files        │
└───────────────────────────────────────────────────────┘
```