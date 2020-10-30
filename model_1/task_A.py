import sys
import re


print(sum([int(num_str) for num_str in re.findall(r"-?\d+", " ".join(sys.stdin.readlines()))]))
