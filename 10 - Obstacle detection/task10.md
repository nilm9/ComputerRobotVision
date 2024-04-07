# Robot Path Obstacle Detection

## Overview

This exercise involves processing an image sequence to detect obstacles in a robot's path using computer vision techniques.

## Task

Analyze a series of images taken from a robot-mounted camera. The camera captures images of the ground and any obstacles as the robot moves. 

## Steps

- Load the image sequence.
- For each image, divide it into tiles and extract salient points within these regions.
- Match salient points with those from the previous image's corresponding tile.
- Visualize matched points.
- Detect obstacles by analyzing spatial relationships of matched points across consecutive images.

## Methodology

1. **Extract and Match Points**: 
   - Identify salient points in each image tile.
   - Match these points to those in the same tile from the previous image.

2. **Detect Obstacles**:
   - Use singular value decomposition to understand the spatial distribution of matched points.
   - Apply a threshold to identify deviations from planarity.
   - Points on a plane suggest no obstacle, while non-planar arrangements indicate potential obstacles.

3. **Record Findings**:
   - Maintain a record of obstacle detection for each tile in each image.

## Result Interpretation

- Points are color-coded based on the detection outcome.
- Green points: no obstacle.
- Red points: obstacle detected.

## Note on Accuracy

The detection method prioritizes safety, potentially leading to false positives, which are less critical than false negatives in obstacle detection scenarios.


