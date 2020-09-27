# Corcaigh-xit-BDP

http://multimedia.ucc.ie/Public/training/cycle2/IrlCPC-ProblemSet2017.pdf

The day has arrived for the people of the Republic of Cork to declare their indepen- dence. Politicians have decided that the border of the county should be protected from the rest of Ireland. Because neighbouring counties stubbornly refuse to pay for the construction of a wall, a decision has been made to plant mines along the county border. To implement this, local geographers have marked rectangular zones of height N and width M in which they defined cells of unit size. Each of these N × M cells may contain a landmine. They carefully recorded whether or not cells contained a mine and the total number of mines in the zone.
Although the location of the mines must remain secret, local authorities want to create maps from which their location can be inferred. D ́onal, a UCC student, was asked to produce these maps so that each cell contains the number of mines buried in the vicinity of that cell or the character ’x’ if the cell itself is mined. Each cell has between 3 and 8 neighbours, depending on its location in the grid.
Not Cork Not Cork
Cork Cork
Original maps on the left. On the right, the expected completed map. Can you help D ́onal to produce these maps ?
Input The first line contains two integers N and M, 1 ≤ N,M ≤ 1000, corre- sponding to the the height and width of the map respecitvely. The next N lines contain M space-separated characters. Each character is either an x if this cell contains a mine, or o to represent an empty cell.
Output The output consists of N lines of M space-separated characters. Each character either encodes for the number of adjacent cells containing mines, or the character ’x’ if the cell itself contains a mine.