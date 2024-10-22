from physics import calculate_weight_on_earth, calculate_weight_on_moon, time_to_fall, sound_travel_time

def main():
    mass = 70  # hmotnost v kg
    height = 10  # výška v metrech
    distance = 1000  # vzdálenost v metrech

    weight_earth = calculate_weight_on_earth(mass)
    weight_moon = calculate_weight_on_moon(mass)
    fall_time = time_to_fall(height)
    sound_time = sound_travel_time(distance)

    print(f"vaha na zemi: {weight_earth} N")
    print(f"vaha na mesici: {weight_moon} N")
    print(f"cas padu z {height} metru: {fall_time:.2f} sekund")
    print(f"cas, za ktery zvuk urazi {distance} metru: {sound_time:.2f} sekund")

if __name__ == "__main__":
    main()
