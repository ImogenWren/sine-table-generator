import numpy as np

# Parameters
N = 240         # number of samples
min_val = 600     # minimum integer value
max_val = 1023   # maximum integer value



def user_interface():
    N = int(input("\nEnter Number of Samples: N\n"))
    print(f"N = {N}")
    min_val = int(input("\nEnter the Minimum Value\n"))
    print(f"min_val = {min_val}")
    max_val = int(input("\nEnter the Maximum Value\n"))
    print(f"max_val = {max_val}\n")
    gen_sine(N, min_val, max_val)
    user = input("\npress enter to exit program\n")


# Generate sine wave
def gen_sine(N, min_val, max_val):
    x = np.arange(N)
    sine_wave = (np.sin(2 * np.pi * x / N) + 1) / 2  # normalize to 0..1
    sine_wave_scaled = np.round(sine_wave * (max_val - min_val) + min_val).astype(int)

    # Convert to list
    sine_list = sine_wave_scaled.tolist()
    for i in range(0, len(sine_list), 8):
        line = " ".join(str(v) + "," for v in sine_list[i:i + 8])
        print(line)
    #print(sine_list)





if __name__ == '__main__':
    user_interface()
    #gen_sine(N, min_val, max_val)


