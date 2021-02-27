import sys
import json
params = [tuple(i.strip().split(" + ")) for i in sys.stdin]
out = {"geographical": {x[0]: x[1] for x in params if "." not in x[1]},
       "physical": {x[0]: x[1] for x in params if not "." in x[1]}}
with open('research.json', "w") as out_file:
    json.dump(out, out_file, indent=4)