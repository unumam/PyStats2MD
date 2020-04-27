import pystats2md
from pystats2md.stats_subset import *
from pystats2md.stats_file import *
from pystats2md.report import *
from pystats2md.micro_bench import *

f = StatsFile('example/benchmarks.json')
r = Report()

r.add('# Database performance')

r.add(f.table(
    rows='database_name',
    cols='benchmark_name',
    cells='operations_per_second',
))

r.add('## Lets add some colors!')

r.add(f.table(
    rows='database_name',
    cols='benchmark_name',
    cells='operations_per_second',
).add_emoji())

r.add('## Or a ranking?')

r.add(f.table(
    rows='database_name',
    cols='benchmark_name',
    cells='operations_per_second',
).add_ranking())

r.add('## Define a baseline and see the gains!')

r.add(StatsSubset(f).to_table(
    row_name_property='database_name',
    col_name_property='benchmark_name',
    cell_content_property='operations_per_second',
    row_names=['SQLite', 'MySQL', 'PostgreSQL', 'MongoDB'],
    col_names=['Find Entry'],
).add_gains())

# r.add(f.chart(
#     bars='database_name',
#     ys='operations_per_second',
# ).filter(
#     benchmark_name='insert',
# ))

r.print_to('example/example1.md')

# print(StatsSubset.filter(
#     f.benchmarks,
#     benchmark_name='Insert Dump',
# database_name='MongoDB',
# dataset='Patent Citations Graph',
# device_name='macbook',
# ))

assert f.contains(MicroBench(
    benchmark_name='Insert Dump',
    func=lambda: print('RUNNING!!!'),
    database_name='MongoDB',
    dataset='Patent Citations Graph',
    device_name='macbook',
)) == True

assert f.existing_index(MicroBench(
    benchmark_name='Insert Dump',
    func=lambda: print('RUNNING!!!'),
    database_name='MongoDB',
    dataset='Movie Ratings',
    device_name='macbook',
)) == 0

assert f.existing_index(MicroBench(
    benchmark_name='Insert Dump',
    func=lambda: print('RUNNING!!!'),
    database_name='MongoDB',
    dataset='Patent Citations Graph',
    device_name='macbook',
)) == 1
