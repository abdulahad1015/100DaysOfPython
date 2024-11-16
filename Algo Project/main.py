import tkinter as tk
from tkinter import filedialog, messagebox
import math
import os


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair(px, py, output_text):
    if len(px) <= 3:
        min_dist = float('inf')
        for i in range(len(px)):
            for j in range(i + 1, len(px)):
                min_dist = min(min_dist, dist(px[i], px[j]))
        output_text.insert(tk.END, f"Brute force on {px}: min_dist = {min_dist}\n")
        output_text.update()
        return min_dist

    mid = len(px) // 2
    midpoint = px[mid]

    left_px = px[:mid]
    right_px = px[mid:]
    left_py = [p for p in py if p[0] <= midpoint[0]]
    right_py = [p for p in py if p[0] > midpoint[0]]

    output_text.insert(tk.END, f"Dividing points: Left = {left_px}, Right = {right_px}\n")
    output_text.update()

    d1 = closest_pair(left_px, left_py, output_text)
    d2 = closest_pair(right_px, right_py, output_text)
    d = min(d1, d2)

    output_text.insert(tk.END, f"Minimum distance from left and right: d1 = {d1}, d2 = {d2}, d = {d}\n")
    output_text.update()

    strip = [p for p in py if abs(p[0] - midpoint[0]) < d]
    output_text.insert(tk.END, f"Building strip: {strip} with d = {d}\n")
    output_text.update()

    min_d = d
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_d:
                break
            min_d = min(min_d, dist(strip[i], strip[j]))
            output_text.insert(tk.END, f"Checking strip points {strip[i]} and {strip[j]}: min_d = {min_d}\n")
            output_text.update()

    return min_d


def prod(x, y, output_text):
    if len(x) <= 1 or len(y) <= 1:
        result = int(x) * int(y)
        output_text.insert(tk.END, f"Base case multiplication: {x} * {y} = {result}\n")
        output_text.update()
        return result

    n = max(len(x), len(y))
    half = n // 2

    a = x[:-half]
    a1 = x[-half:]
    b = y[:-half]
    b1 = y[-half:]

    A = prod(a1, b1, output_text)
    B = prod(str(int(a1) + int(a)), str(int(b1) + int(b)), output_text)
    C = prod(a, b, output_text)

    result = C * 10 ** (2 * half) + (B - C - A) * 10 ** half + A
    output_text.insert(tk.END, f"Calculating prod({x}, {y}): C*10^(2*{half}) + (B - C - A)*10^{half} + A = {result}\n")
    output_text.update()
    return result


class AlgorithmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Application with Step-by-Step Output")
        self.root.geometry("600x400")

        self.file_path = tk.StringVar()
        tk.Label(root, text="Select Input File:").pack(pady=10)
        tk.Entry(root, textvariable=self.file_path, width=50).pack()
        tk.Button(root, text="Browse", command=self.browse_file).pack()

        self.algorithm = tk.StringVar(value="closest_pair")
        tk.Label(root, text="Select Algorithm:").pack(pady=10)
        tk.Radiobutton(root, text="Closest Pair of Points", variable=self.algorithm, value="closest_pair").pack()
        tk.Radiobutton(root, text="Integer Multiplication", variable=self.algorithm, value="karatsuba").pack()

        tk.Button(root, text="Run Algorithm", command=self.run_algorithm).pack(pady=10)

        self.output_text = tk.Text(root, height=15, width=70)
        self.output_text.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path.set(file_path)

    def run_algorithm(self):
        file_path = self.file_path.get()
        if not os.path.exists(file_path):
            messagebox.showerror("Error", "Please select a valid file.")
            return

        algorithm = self.algorithm.get()
        with open(file_path, 'r') as file:
            data = file.readlines()

        self.output_text.delete(1.0, tk.END)

        if algorithm == "closest_pair":
            points = [tuple(map(int, line.split())) for line in data]
            px = sorted(points, key=lambda x: x[0])
            py = sorted(points, key=lambda x: x[1])
            min_distance = closest_pair(px, py, self.output_text)
            self.output_text.insert(tk.END, f"\nClosest pair distance: {min_distance:.2f}")

        elif algorithm == "karatsuba":
            x, y = data[0].strip(), data[1].strip()
            result = prod(x, y, self.output_text)
            self.output_text.insert(tk.END, f"\nMultiplication result: {result}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AlgorithmApp(root)
    root.mainloop()
