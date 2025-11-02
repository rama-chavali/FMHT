import matplotlib.pyplot as plt

# Path to your input .xy file
input_file = 'xvelocityalong10m.xy'

# Read data
x_vals = []
y_vals = []

with open(input_file, 'r') as f:
    for line in f:
        if line.strip():  # Skip empty lines
            try:
                x, y = map(float, line.strip().split())
                x_vals.append(x)
                y_vals.append(y)
            except ValueError:
                print(f"Skipping malformed line: {line.strip()}")

# Create plot
plt.figure(figsize=(6, 4))
plt.plot(x_vals, y_vals, linestyle='-')
plt.title('XY Plot')
plt.xlabel('X')
plt.ylabel('Y')


# Save to EPS
output_file = 'xvelocityalong10m.eps'
plt.savefig(output_file, format='eps')

print(f"Plot saved as: {output_file}")
