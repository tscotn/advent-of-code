from pathlib import Path
p = Path(__file__).with_name('input.txt')

lines = []
with p.open('r') as f:
    lines = [line[:-1] for line in f.readlines()]
