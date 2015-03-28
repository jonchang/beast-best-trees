#!/usr/bin/env python

# Copyright (C) 2015 Jonathan Chang <jonathan.chang@ucla.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import re
import heapq

import argh

__version__ = '0.1'

@argh.arg('treefile', help='.trees file to load')
@argh.arg('--max-trees', help='number of trees to retrieve')
@argh.arg('--burnin', help='number of trees to remove as burnin')
@argh.arg('--output', help='name of output file')
def cmd(treefile, max_trees=100, burnin=0, output="output.bestn.trees"):
    """Gets the best N trees based on posterior probability from a BEAST 1.x treelog.
    """
    # initialize heap with all small numbers
    heap = [float('-inf')] * max_trees
    heapq.heapify(heap)

    # keep track of nexus file state
    pre = []
    post = []
    trees_seen = 0

    # read the tree
    with open(treefile) as rfile:
        for line in rfile:
            if line.startswith('tree'): # inside tree
                trees_seen += 1
                if trees_seen <= burnin:
                    continue
                _, state, comment, tree = line.split(" ", 3)
                prob = float(re.search('posterior=(.+)\]', comment).group(1))
                heapq.heappushpop(heap, (prob, state, comment, tree))
            elif trees_seen > 0: # after trees
                post.append(line)
            else: # before trees
                pre.append(line)

    ntrees = 0

    with open(output, 'w') as wfile:
        wfile.writelines(pre)
        items = [heapq.heappop(heap) for i in range(len(heap))]
        for item in reversed(items): # access largest to smallest, so the best tree is first
            if item == float('-inf'):
                continue
            wfile.write(' '.join(['tree', item[1], item[2], item[3]]))
            ntrees += 1
        wfile.writelines(post)

    return 'Wrote {0} trees to {1}'.format(ntrees, output)

def main():
    argh.dispatch_command(cmd)

if __name__ == '__main__':
    main()
