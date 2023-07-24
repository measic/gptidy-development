import pandas as pd
import numpy as np

waypoint_distances = {}
waypoint_durations = {}
all_waypoints = set()

waypoint_data = pd.read_csv("my-waypoints-dist-dur.tsv", sep="\t")

for i, row in waypoint_data.iterrows():
    waypoint_distances[frozenset([row.waypoint1, row.waypoint2])] = row.distance_m
    waypoint_durations[frozenset([row.waypoint1, row.waypoint2])] = row.duration_s
    all_waypoints.update([row.waypoint1, row.waypoint2])