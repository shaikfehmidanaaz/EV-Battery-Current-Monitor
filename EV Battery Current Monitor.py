class EVBatteryCurrentMonitor:

    def __init__(self, rated_current):
        self.rated_current = rated_current

    def calculate_power(self, voltage, current):
        return voltage * current

    def check_current(self, current):
        if current > self.rated_current:
            return "OVER CURRENT"
        elif current < 0:
            return "INVALID CURRENT"
        else:
            return "NORMAL"

    def display_status(self, voltage, current):
        power = self.calculate_power(voltage, current)
        status = self.check_current(current)

        print("----- EV Battery Current Monitor -----")
        print(f"Battery Voltage : {voltage:.2f} V")
        print(f"Battery Current : {current:.2f} A")
        print(f"Battery Power   : {power:.2f} W")
        print(f"Current Limit   : {self.rated_current:.2f} A")
        print(f"Status          : {status}")

        if status == "OVER CURRENT":
            print("WARNING: Reduce charging/discharging current!")
        elif status == "INVALID CURRENT":
            print("ERROR: Current value cannot be negative.")
        else:
            print("Battery current is within the safe limit.")


# Example
rated_current = 100       # Maximum safe current in A
battery_voltage = 400     # Battery voltage in V
battery_current = 80      # Measured current in A

monitor = EVBatteryCurrentMonitor(rated_current)

monitor.display_status(
    battery_voltage,
    battery_current
)
