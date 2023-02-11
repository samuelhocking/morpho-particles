from TimingTools import datetimeTimingTools
import sys

# print(f'len argvs: {len(sys.argv)}')
# print(sys.argv)

if len(sys.argv) == 1:
    datetimeTimingTools().writeDT()
else:
    datetimeTimingTools(sys.argv[1]).writeDT()