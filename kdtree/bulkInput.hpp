//
//  bulkInput.hpp
//  KDtree
//
//  Created by Deepanker Mishra on 27/03/18.
//  Copyright © 2018 Deepanker Mishra. All rights reserved.
//

#ifndef bulkInput_hpp
#define bulkInput_hpp

#include <iostream>
#include <string>
#include <fstream>
#include <cassert>
#include "KDTree.hpp"

int partition(std::vector<Point>& v, int l, int h, int dim);
void makeKDTree(std::vector<Point>& vp, int l, int h, int curdim, int totaldim, KDTree& kdt);
KDTree bulkInsert(char* filename, KDTree& kdt);
std::pair<unsigned int, std::vector<Point> > readFile(char* queryfile);
Point readQuery(char* queryfile);
#endif /* bulkInput_hpp */
