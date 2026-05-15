import sys
from lcs import lcs


class DiffTool:
    def __init__(self, file1_path, file2_path):
        with open(file1_path, 'r') as f:
            self.lines_a = f.read().splitlines()
        with open(file2_path, 'r') as f:
            self.lines_b = f.read().splitlines()

    def compute_and_format(self):
        common = lcs(self.lines_a, self.lines_b)

        result = []
        i, j = 0, 0

        for line in common:
            while i < len(self.lines_a) and self.lines_a[i] != line:
                result.append(f"- {self.lines_a[i]}")
                i += 1
            while j < len(self.lines_b) and self.lines_b[j] != line:
                result.append(f"+ {self.lines_b[j]}")
                j += 1
            result.append(f"  {line}")
            i += 1
            j += 1

        while i < len(self.lines_a):
            result.append(f"- {self.lines_a[i]}")
            i += 1

        while j < len(self.lines_b):
            result.append(f"+ {self.lines_b[j]}")
            j += 1

        return "\n".join(result)

    def run(self):
        output = self.compute_and_format()
        print(output)


if __name__ == "__main__":
    tool = DiffTool(sys.argv[1], sys.argv[2])
    tool.run()