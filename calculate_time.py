#!/usr/bin/env python3

import math
import time

# Parameters
distance = 12.0  # Target distance (meters)
radius = 0.5     # Wheel radius (meters)
desired_time = None  # Desired time to travel the distance (seconds)
target_velocity = 14000  # RPM value (if provided, overrides time calculation)


def calculate_travel_time(distance, radius, rpm=None, desired_time=None):
    if desired_time is not None:
        return desired_time
    elif rpm is not None:
        result = calculate_rpm_or_time(distance=distance, radius=radius, rpm=rpm)
        return result["time"]
    else:
        raise ValueError("Either 'desired_time' or 'rpm' must be specified")


def calculate_rpm_or_time(distance, radius, rpm=None, time=None):
    # Convert distance to angular distance in radians
    angular_distance = distance / radius  # in radians

    if time is not None:  # If time is provided, calculate RPM
        angular_velocity_rad_per_s = angular_distance / time
        rpm_calculated = angular_velocity_rad_per_s * (60 / (2 * math.pi))
        return {"rpm": rpm_calculated}

    elif rpm is not None:  # If RPM is provided, calculate time
        angular_velocity_rad_per_s = rpm * (2 * math.pi / 60)
        time_calculated = angular_distance / angular_velocity_rad_per_s
        return {"time": time_calculated}

    else:
        raise ValueError("Either 'rpm' or 'time' must be provided.")


def calculate_linear_velocity_from_rpm(rpm, radius):
    angular_velocity = rpm * (2 * math.pi / 60)  # Convert RPM to rad/s
    linear_velocity = angular_velocity * radius  # Convert rad/s to m/s
    return linear_velocity


def main():
    # Calculate travel time
    try:
        travel_time = calculate_travel_time(distance=distance, radius=radius, rpm=rpm, desired_time=desired_time)
        print(f"Calculated travel time: {travel_time:.2f} seconds")
    except ValueError as e:
        print(f"Error in calculation: {e}")
        return

    # Start tracking time
    start_time = time.time()
    print("Starting motion...")

    # Simulate motion
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= travel_time:
            break
        time.sleep(0.1)  

    print("Motion complete.")


if __name__ == "__main__":
    main()
